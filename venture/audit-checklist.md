# 10-Point Website Check

For each point, score Pass or Fail and note the business impact in one line.

1. **Mobile:** The site is usable on a phone and doesn't scroll sideways.
2. **Contact path:** Click-to-call works and the contact form actually delivers.
3. **Broken features:** No dead widgets, console errors or `#` links.
4. **Placeholder content:** No lorem ipsum, `[year]`, stock placeholders or "coming soon".
5. **Consistency:** One design across every page.
6. **Trust basics:** HTTPS, a current copyright year, address and hours visible.
7. **Local SEO:** Unique titles and meta descriptions, LocalBusiness schema, the town named in the text.
8. **Speed:** Loads in under 3 seconds on 4G, images compressed.
9. **Security hygiene:** No API keys or secrets in page source, and no calls to `localhost`.
10. **Legal and compliance:** A privacy policy is present and any required industry disclosures appear on every page.

---

## Worked example: this repo's J & K site (internal review only)
This is here to show how the checklist works and to test the process.
Don't send it to J & K unless the founder has a real relationship with them.

| # | Result | Finding |
|---|---|---|
| 1 | Pass (partial) | The Home nav doesn't collapse on mobile, while the other pages do. |
| 2 | **Fail** | The contact form has no action, so submissions go nowhere (`contact.html`). |
| 3 | **Fail** | The chat widget on Home posts to `http://localhost:18789` and fails for every visitor (`index.html:90`). The chat widgets on the other pages have no API key and always show an error. |
| 4 | **Fail** | `about.html` says "since [year]". Services and About use `via.placeholder.com` images. The blog's "Read More" buttons link to `#`. |
| 5 | **Fail** | Home uses Tailwind with a black and gold theme. Every other page uses Bootstrap with a white theme. |
| 6 | **Fail** | The footer says "2023". |
| 7 | **Fail** | No meta descriptions, no schema, no sitemap. |
| 8 | Not measured | Needs a Lighthouse run after deploy. |
| 9 | **Fail** | The chat code puts an API key in client-side JavaScript. Even as a placeholder, it invites someone to paste in a real key. |
| 10 | **Fail** | The Cetera FINRA/SIPC disclosure appears only on Home. Securities disclosures generally need to be on every page, and the client's compliance team decides the wording. |

Verdict: 9 of 10 fail. This is a typical Fix-Up job.
