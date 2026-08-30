#!/usr/bin/env python3
"""
Verbatim quote validation gate for the VOC messaging skill.

Confirms every candidate VOC quote is an EXACT substring of its call's raw transcript.
Quotes that fail are dropped, never reworded. This is the guard against the fabricated-quote
failure where an AI tool emits plausible-but-fabricated customer quotes.

Usage:
    python validate_quotes.py --records /tmp/voc_records.json --transcripts /tmp/transcripts

Inputs:
    --records      JSON list of per-call compact records. Each record must have:
                     { "call_id": "...", "title": "...",
                       "quote_candidates": [ {"speaker": "...", "text": "...", "theme": "..."}, ... ] }
    --transcripts  Directory of raw transcripts named "<call_id>.txt" (as returned by
                   get_transcript, saved verbatim).

Output:
    Prints a JSON report to stdout and writes /tmp/voc_validated_quotes.json containing
    ONLY the quotes that passed. Non-zero exit if the inputs are malformed.

Matching is deliberately strict-but-fair:
    - Whitespace (spaces, tabs, newlines) is collapsed to single spaces on both sides.
    - Case is preserved (a quote is a quote); comparison is case-insensitive ONLY as a
      secondary pass that is reported separately, never auto-accepted.
    - No fuzzy/edit-distance matching. Close is not verbatim.
"""

import argparse
import json
import os
import re
import sys


def normalize(s: str) -> str:
    # Collapse all runs of whitespace to a single space and strip ends.
    # Leaves interior words and punctuation untouched.
    return re.sub(r"\s+", " ", s).strip()


def load_transcript(transcripts_dir: str, call_id: str) -> str:
    path = os.path.join(transcripts_dir, f"{call_id}.txt")
    if not os.path.isfile(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", required=True)
    ap.add_argument("--transcripts", required=True)
    args = ap.parse_args()

    try:
        with open(args.records, "r", encoding="utf-8") as fh:
            records = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR reading records: {e}", file=sys.stderr)
        return 2

    if not isinstance(records, list):
        print("ERROR: records file must be a JSON list.", file=sys.stderr)
        return 2

    passed = []
    stats = {
        "calls": 0,
        "candidates": 0,
        "exact_pass": 0,
        "case_insensitive_only": 0,  # matched only when ignoring case -> reported, NOT accepted
        "failed": 0,
    }
    failures = []
    case_flags = []

    for rec in records:
        call_id = str(rec.get("call_id", "")).strip()
        title = rec.get("title", "")
        raw = load_transcript(args.transcripts, call_id)
        norm_raw = normalize(raw)
        norm_raw_lc = norm_raw.lower()
        stats["calls"] += 1

        if not raw:
            for q in rec.get("quote_candidates", []):
                stats["candidates"] += 1
                stats["failed"] += 1
                failures.append({"call_id": call_id, "reason": "transcript_missing",
                                 "text": q.get("text", "")})
            continue

        for q in rec.get("quote_candidates", []):
            stats["candidates"] += 1
            text = q.get("text", "")
            norm_q = normalize(text)
            if not norm_q:
                stats["failed"] += 1
                failures.append({"call_id": call_id, "reason": "empty", "text": text})
                continue

            if norm_q in norm_raw:
                stats["exact_pass"] += 1
                passed.append({
                    "call_id": call_id,
                    "title": title,
                    "company": rec.get("company", ""),
                    "speaker": q.get("speaker", ""),
                    "theme": q.get("theme", ""),
                    "text": text,
                })
            elif norm_q.lower() in norm_raw_lc:
                # Matched only after lowercasing -> suspicious (model altered casing).
                # Report for human review; do NOT auto-accept.
                stats["case_insensitive_only"] += 1
                case_flags.append({"call_id": call_id, "text": text,
                                   "note": "matches only case-insensitively; review before use"})
            else:
                stats["failed"] += 1
                failures.append({"call_id": call_id, "reason": "not_found", "text": text})

    with open("/tmp/voc_validated_quotes.json", "w", encoding="utf-8") as fh:
        json.dump(passed, fh, ensure_ascii=False, indent=2)

    report = {
        "stats": stats,
        "validated_count": len(passed),
        "case_insensitive_flags": case_flags,
        "failures": failures,
        "note": ("Only 'exact_pass' quotes are written to /tmp/voc_validated_quotes.json "
                 "and are eligible for output. Failed and case-only quotes are dropped; "
                 "do NOT reword them to pass."),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if len(passed) < 15:
        print(f"\nWARNING: only {len(passed)} verbatim-validated quotes. "
              f"Output what survived; do not paraphrase to reach 15.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
