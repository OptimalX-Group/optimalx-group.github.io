import re
from collections import defaultdict

def extract_year(line):
    line = line.strip()
    if re.fullmatch(r"\d{4}", line):
        return line
    m = re.fullmatch(r"\d+\*?\s+(\d{4})", line)
    if m:
        return m.group(1)
    return None

def format_publications():
    with open("input.txt", "r", encoding="utf-8") as f:
        raw = [l.rstrip() for l in f.readlines()]

    by_year = defaultdict(list)
    i = 0

    while i < len(raw):
        if raw[i].strip() == "":
            i += 1
            continue

        title = raw[i].strip()
        authors = raw[i+1].strip()
        venue = raw[i+2].strip()
        i += 3

        year = None
        while i < len(raw) and year is None:
            year = extract_year(raw[i])
            i += 1

        if year:
            by_year[year].append((title, authors, venue))

    with open("output.txt", "w", encoding="utf-8") as f:
        for year in sorted(by_year.keys(), reverse=True):
            f.write(f"## {year}\n\n")
            for t,a,v in by_year[year]:
                f.write(f"***{t}***  \n")
                f.write(f"{a}  \n")
                f.write(f"{v}\n\n")

format_publications()
