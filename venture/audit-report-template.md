# Website Check for {{BUSINESS}}
{{URL}} · checked {{DATE}} by {{YOUR_NAME}}, {{PHONE}}

**Summary:** Your site passes {{PASS_COUNT}} of 10 checks. The {{TOP_N}} issues below are the ones most likely costing you calls.

| # | Check | Result | What we found | Why it matters |
|---|---|---|---|---|
| 1 | Works on phones | {{P/F}} | {{finding}} | Most people searching for local businesses do it on a phone |
| 2 | Customers can reach you | {{P/F}} | {{finding}} | A form that doesn't send means leads you never hear about |
| 3 | Nothing broken | {{P/F}} | {{finding}} | Broken buttons make visitors think the business is closed |
| 4 | No placeholder content | {{P/F}} | {{finding}} | "[year]" or stock photos look unfinished |
| 5 | Consistent look | {{P/F}} | {{finding}} | Pages that don't match look like several different companies |
| 6 | Trust basics | {{P/F}} | {{finding}} | Browsers warn on non-HTTPS sites, and an old year looks abandoned |
| 7 | Shows up in local search | {{P/F}} | {{finding}} | Missing titles and descriptions mean Google shows competitors instead |
| 8 | Speed | {{P/F}} | {{finding}} | Many visitors leave if a page takes over 3 seconds |
| 9 | Security | {{P/F}} | {{finding}} | Exposed keys and test code are a security risk |
| 10 | Legal pages | {{P/F}} | {{finding}} | Privacy policy and any required industry disclosures |

**What I'd fix:** everything marked Fail, for a flat $299, done in 5 business days.
You pay half to start and half when you approve the finished site: {{STRIPE_DEPOSIT_LINK}}

Or keep this report and fix it yourself. Either way is fine.

---
### How to produce this report (20 minutes)
1. Run `python3 check_site.py {{URL}}` (2 minutes). Copy its results into rows 2, 3, 4, 6, 7, 9 and 10.
2. Open the site on your phone (row 1) and click through every page (row 5).
3. Run PageSpeed Insights at https://pagespeed.web.dev for the mobile score (row 8).
4. **Confirm each Fail with your own eyes.** Delete any finding you couldn't reproduce.
5. Replace every `{{…}}`, export to PDF (Google Docs is free), send it, and set the lead's stage to `audit_sent`.
