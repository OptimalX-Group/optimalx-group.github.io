"""
Fetches papers from Yue Yu's Google Scholar profile and updates papers.md
in the existing format: grouped by year (descending), title, authors, venue.
"""

import time
from collections import defaultdict
from scholarly import scholarly

SCHOLAR_ID = "bwhxFnEAAAAJ"
OUTPUT_FILE = "papers.md"

HEADER = """---
title: Papers
Permalink: /papers/
---

<br>
<h3>Papers</h3>

For metrics and citations, please refer to Yue's [Google Scholar profile](https://scholar.google.com/citations?user=bwhxFnEAAAAJ&hl=en).

"""


def fetch_publications():
    print(f"Fetching publications for scholar ID: {SCHOLAR_ID}")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    papers_by_year = defaultdict(list)

    for pub in author["publications"]:
        try:
            filled = scholarly.fill(pub)
            bib = filled.get("bib", {})

            title = bib.get("title", "Unknown Title")
            year = int(bib.get("pub_year", 0))
            authors = bib.get("author", "")
            venue = bib.get("venue", "") or bib.get("journal", "") or bib.get("booktitle", "")

            papers_by_year[year].append({
                "title": title,
                "authors": authors,
                "venue": venue,
            })

            time.sleep(1)  # Be polite to Google Scholar
        except Exception as e:
            print(f"  Skipping a publication due to error: {e}")

    return papers_by_year


def write_papers_md(papers_by_year):
    lines = [HEADER]

    for year in sorted(papers_by_year.keys(), reverse=True):
        if year == 0:
            continue
        lines.append(f"### {year}\n")
        for paper in papers_by_year[year]:
            lines.append(f"***{paper['title']}***  ")
            lines.append(f"{paper['authors']}  ")
            if paper["venue"]:
                lines.append(f"{paper['venue']}")
            lines.append("")  # blank line between papers

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Written to {OUTPUT_FILE}")


def main():
    papers_by_year = fetch_publications()
    total = sum(len(v) for v in papers_by_year.values())
    print(f"Fetched {total} publications.")
    write_papers_md(papers_by_year)


if __name__ == "__main__":
    main()
