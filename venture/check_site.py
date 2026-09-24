#!/usr/bin/env python3
"""Automated first pass of the 10-point website check (audit-checklist.md).

Usage: python3 check_site.py https://example.com [more urls or local .html files]

Covers the points that can be detected from page source. Every FAIL must still
be confirmed by eye on a phone and a desktop before it goes to a prospect
(sop-delivery.md, section A step 3). Points 1, 5 and 8 need a human/Lighthouse.
"""
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path


def fetch(target):
    if Path(target).exists():
        return Path(target).read_text(errors="replace"), None, target
    url = target if "://" in target else "https://" + target
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 site-check"})
    start = time.time()
    with urllib.request.urlopen(req, timeout=20) as r:
        html = r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")
        return html, time.time() - start, r.geturl()


def check(html, seconds, final_url):
    low = html.lower()
    results = []

    def add(point, ok, finding):
        results.append((point, "PASS" if ok else "FAIL", finding))

    has_viewport = 'name="viewport"' in low or "name=viewport" in low
    add("1 Mobile (viewport tag only; verify on phone)", has_viewport,
        "viewport meta present" if has_viewport else "no viewport meta tag: likely unusable on phones")

    forms = re.findall(r"<form\b[^>]*>", low)
    dead_forms = [f for f in forms if not re.search(r"action\s*=\s*['\"][^'\"#]+", f)
                  and "netlify" not in f]
    has_tel = "href=\"tel:" in low or "href='tel:" in low
    add("2 Contact path", has_tel and not dead_forms,
        "; ".join(filter(None, ["no click-to-call link" if not has_tel else "",
                                f"{len(dead_forms)} form(s) with no action (submissions likely go nowhere)"
                                if dead_forms else ""])) or "click-to-call present, forms have actions")

    dead_links = len(re.findall(r"href\s*=\s*['\"]#['\"]", low))
    add("3 Broken features", dead_links == 0,
        f"{dead_links} link(s) pointing to '#'" if dead_links else "no '#' links found")

    placeholders = [p for p in ("lorem ipsum", "[year]", "via.placeholder.com", "placeholder.com/",
                                "coming soon", "your_", "todo") if p in low]
    add("4 Placeholder content", not placeholders,
        "found: " + ", ".join(placeholders) if placeholders else "none found")

    years = [int(y) for y in re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(\d{4})", low)]
    years += [int(y) for y in re.findall(r"(\d{4})\s+all rights reserved", low)]
    https = final_url.startswith("https://") if "://" in final_url else None
    stale = years and max(years) < date.today().year - 1
    trust_bits = []
    if https is False:
        trust_bits.append("not HTTPS")
    if stale:
        trust_bits.append(f"copyright year {max(years)}")
    add("6 Trust basics", not trust_bits, "; ".join(trust_bits)
        or ("copyright year OK (local file: HTTPS not checked)" if https is None else "HTTPS / year OK"))

    seo_missing = [n for n, pat in (("meta description", r'name=["\']description["\']'),
                                    ("LocalBusiness schema", r"localbusiness|insuranceagency|\"@type\""),
                                    ("<title>", r"<title>[^<]+</title>")) if not re.search(pat, low)]
    add("7 Local SEO", not seo_missing, "missing: " + ", ".join(seo_missing) if seo_missing else "basics present")

    if seconds is not None:
        add("8 Speed (HTML fetch only; run Lighthouse)", seconds < 1.5, f"HTML fetched in {seconds:.1f}s")

    secrets = [s for s in ("localhost", "127.0.0.1", "api_key", "apikey", "sk-", "bearer ")
               if s in low]
    add("9 Security hygiene", not secrets,
        "found in page source: " + ", ".join(secrets) if secrets else "nothing obvious")

    has_privacy = "privacy" in low
    add("10 Legal (privacy link only)", has_privacy,
        "privacy policy link present" if has_privacy else "no privacy policy link")
    return results


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for target in sys.argv[1:]:
        print(f"\n=== {target} ===")
        try:
            html, seconds, final_url = fetch(target)
        except Exception as e:  # unreachable site is itself a finding
            print(f"FAIL  could not load: {e}")
            continue
        results = check(html, seconds, final_url)
        fails = sum(r[1] == "FAIL" for r in results)
        for point, status, finding in results:
            print(f"{status:4}  {point}: {finding}")
        print(f"--> {fails} automated FAIL(s). Qualified lead if >= 2. Points 1, 5, 8 need manual check.")


if __name__ == "__main__":
    main()
