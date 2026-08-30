# Google Ads 3-Way Relevance Audit

Cross-checks keyword intent, ad copy, and landing page content to flag relevance mismatches driving Quality Score problems. Outputs a prioritized action list: reroute, rewrite, or pause. No company data or product examples — replace the calibration example in Step 4 with your own product category before use.

## Required inputs

Two Google Ads exports:
1. **Keyword + Quality Score report** — columns: `Keyword status`, `Keyword`, `Final URL`, `Quality Score`, `Ad relevance`, `Exp. CTR`, `Landing page exp.`, `Match type`, `Campaign`, `Ad group`
2. **Ad copy report** — columns: `Keyword text`, `Ad status`, `Final URL`, `Headline 1`–`15`, `Description 1`–`5`, `Path 1`, `Path 2`, `Campaign`, `Ad group`

## Step 1: Load and validate

Google Ads exports have their header row at index 2 (row 3 in the spreadsheet), not row 0.

```python
import pandas as pd

df_kw = pd.read_excel('keyword_file.xlsx', header=2)
df_ad = pd.read_excel('ad_copy_file.xlsx', header=2)

required_kw_cols = ['Keyword status', 'Keyword', 'Final URL', 'Quality Score',
                     'Ad relevance', 'Exp. CTR', 'Landing page exp.', 'Match type',
                     'Campaign', 'Ad group']
required_ad_cols = ['Keyword text', 'Ad status', 'Final URL']

missing_kw = [c for c in required_kw_cols if c not in df_kw.columns]
missing_ad = [c for c in required_ad_cols if c not in df_ad.columns]
if missing_kw or missing_ad:
    raise ValueError(f"Missing columns — keyword file: {missing_kw}, ad file: {missing_ad}")
```

## Step 2: Join keyword to ad copy

Join on keyword text + Final URL. An enabled keyword with no matching ad copy is a real campaign-health issue (an ad group with no active ad serving it), not an export gap — flag it separately rather than dropping it silently.

```python
merged = df_kw.merge(
    df_ad,
    left_on=['Keyword', 'Final URL'],
    right_on=['Keyword text', 'Final URL'],
    how='left',
    indicator=True
)

no_ad_copy = merged[(merged['Keyword status'] == 'Enabled') & (merged['_merge'] == 'left_only')]
```

## Step 3: Build landing page inventory, scrape with caching

Scrape every unique Final URL once. Cache by URL hash so repeated keywords mapping to the same page don't re-fetch.

```python
import requests
from bs4 import BeautifulSoup
import hashlib, os, json

CACHE_DIR = '.lp_cache'
os.makedirs(CACHE_DIR, exist_ok=True)

def scrape_landing_page(url):
    cache_key = hashlib.md5(url.encode()).hexdigest()
    cache_path = os.path.join(CACHE_DIR, f'{cache_key}.json')
    if os.path.exists(cache_path):
        return json.load(open(cache_path))

    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, 'html.parser')
    content = {
        'url': url,
        'title': soup.title.string if soup.title else '',
        'h1': [h.get_text(strip=True) for h in soup.find_all('h1')],
        'body_text': soup.get_text(separator=' ', strip=True)[:3000],
    }
    json.dump(content, open(cache_path, 'w'))
    return content

lp_inventory = {url: scrape_landing_page(url) for url in merged['Final URL'].unique()}
```

## Step 4: LLM-based 3-way relevance scoring

The prompt receives the full LP inventory, not just the matched page — so it can recommend rerouting to a better-fit page already in the account before recommending a pause. This is the key design decision: pause is the last resort, not the default.

```python
SCORING_PROMPT = """
You are auditing a Google Ads campaign for relevance across three elements:
keyword intent, ad copy, and landing page content.

Keyword: {keyword}
Match type: {match_type}
Ad headlines: {headlines}
Ad descriptions: {descriptions}
Landing page title: {lp_title}
Landing page content (excerpt): {lp_content}

Full inventory of other landing pages in this account (for reroute candidates):
{lp_inventory_summary}

Score relevance 1-5 for:
1. Keyword -> Ad copy alignment
2. Keyword -> Landing page alignment
3. Ad copy -> Landing page alignment

A mismatch means the keyword's job-to-be-done doesn't match what the ad/page
delivers -- not that the wording differs. Example calibration: "project
management software" (keyword) landing on a "time tracking tool" page is a
mismatch (different job-to-be-done). "task tracking software" landing on the
same page is fine (same intent category, different phrasing). Replace this
example with one from your own product line before running.

Then apply this decision tree:
- If any score <= 2 AND a better-fit page exists in the inventory -> REROUTE (name the specific URL)
- If any score <= 2 AND no better-fit page exists -> PAUSE
- If ad-copy-to-LP score <= 2 but keyword-to-LP is fine -> COPY REWRITE
- Otherwise -> no action needed

Return JSON: {{"kw_ad_score": int, "kw_lp_score": int, "ad_lp_score": int,
"recommendation": "reroute|pause|rewrite|none", "reroute_url": str|null, "reasoning": str}}
"""
```

## Step 5: Output — two-tab Excel, prioritized

Tab 1: action list, sorted by severity (pause > reroute > rewrite), color-coded. Tab 2: full underlying data for reference.

```python
import pandas as pd

def write_report(results_df, raw_df, filename='ads_relevance_audit.xlsx'):
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    action_list = results_df[results_df['recommendation'] != 'none'].sort_values(
        by='recommendation', key=lambda s: s.map({'pause': 0, 'reroute': 1, 'rewrite': 2})
    )
    action_list.to_excel(writer, sheet_name='Action List', index=False)
    raw_df.to_excel(writer, sheet_name='Full Data', index=False)

    workbook = writer.book
    sheet = writer.sheets['Action List']
    fmt_pause = workbook.add_format({'bg_color': '#F8696B'})
    fmt_reroute = workbook.add_format({'bg_color': '#FFC000'})
    fmt_rewrite = workbook.add_format({'bg_color': '#FFEB84'})

    rec_col = action_list.columns.get_loc('recommendation')
    for row_num, rec in enumerate(action_list['recommendation'], start=1):
        fmt = {'pause': fmt_pause, 'reroute': fmt_reroute, 'rewrite': fmt_rewrite}.get(rec)
        if fmt:
            sheet.write(row_num, rec_col, rec, fmt)

    writer.close()
```

## If rebuilding as a Claude skill

Trigger phrasing that worked well: "run the search audit", "audit my keywords", "check keyword relevance", "3-way check", "QS analysis", "quality score audit", "landing page mismatch", "keyword to landing page mapping".
