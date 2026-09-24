# Procedure: Website Check and Fix-Up Delivery

## A. Free website check (turnaround: 24 hours from request)
1. Founder adds the lead to `leads.csv` and sends Claude the URL.
2. Claude scores the site against `audit-checklist.md` and writes a one-page report: 10 rows, each with pass/fail, what we found, and why it costs the business.
3. **Founder checks it by hand.** Open the site on a phone and on a desktop, and confirm every "Fail" is really there. Never send a claim you haven't seen yourself.
4. Send the report with the closing script in `outreach.md`. Set the lead's stage to `audit_sent`.

## B. Fix-Up delivery (5 business days from deposit)
| Day | Step | Owner |
|---|---|---|
| 0 | Deposit clears in Stripe and gets logged in `ledger.csv`. Collect access (host login or site files), logo, hours and photos. | Founder |
| 1–2 | Rebuild or repair the pages. Put in a working form. Add schema, titles, meta descriptions and sitemap. | Claude |
| 3 | QA against the quality standard (C). Send the client a preview link. | Founder |
| 4 | One round of revisions. | Claude + Founder |
| 5 | Deploy. Test the form live. Collect the balance. Offer the Care Plan. | Founder |

## C. Quality standard (every item must pass before delivery)
- [ ] Every item that failed in the website check now passes, or has a documented reason it can't.
- [ ] A test form submission reaches the client's inbox, and the client confirms it.
- [ ] Click-to-call works on a real phone.
- [ ] No horizontal scroll at 375px width. Lighthouse mobile scores 90 or higher for Performance and Accessibility, and 95 or higher for SEO.
- [ ] No placeholder text or images, no `#` links, no console errors.
- [ ] No secrets in client-side code.
- [ ] In regulated industries (insurance, finance, medical), the client has approved all disclosure wording in writing.

## D. Customer satisfaction criteria
- The client signs off in writing on the preview ("approved"). That triggers the balance invoice.
- 7 days after delivery, ask: "On a scale of 1–10, how likely are you to recommend us?" Record the answer in `leads.csv` notes.
  - A score of 9 or higher: ask for a Google review and a referral.
  - A score of 6 or lower: fix the problem within 48 hours.
- Refund policy: the deposit is refunded in full if we miss the 5-day deadline without the client's agreement.
