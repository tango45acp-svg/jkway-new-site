# Task Board

Update this board in every session. Each card has an owner and a date.

## Done
- [x] 2026-09-24 **CEO**: Chose the business model: a website fix-up service (see README).
- [x] 2026-09-24 **Product**: Offer, packages and terms (`offer.md`).
- [x] 2026-09-24 **Product**: Quality standard and delivery procedure (`sop-delivery.md`).
- [x] 2026-09-24 **Product**: 10-point website check checklist, tested on the J & K site (`audit-checklist.md`).
- [x] 2026-09-24 **Marketing**: Outreach scripts and organic channel plan (`outreach.md`).
- [x] 2026-09-24 **Marketing**: Sales page template (`landing/index.html`).
- [x] 2026-09-24 **Finance**: Ledger, lead log and report script (`ledger.csv`, `leads.csv`, `report.py`).

- [x] 2026-09-24 **Product**: Automated website checker (`check_site.py`) built and tested. Sales page now passes it.
- [x] 2026-09-24 **CEO**: Daily cycle written up (`daily-cycle.md`, `cycle-log.md`).

- [x] 2026-09-25 **Ops**: GitHub push fixed. The branch is in sync with GitHub.
- [x] 2026-09-25 **Product**: Customer-facing check report template with a 20-minute procedure (`audit-report-template.md`).

## In Progress
- [ ] **Marketing (founder)**: **Day 1 priority.** Experiment 1: 30 contacts in person or by phone. Before each one, run `python3 check_site.py <url>` and contact only businesses with 2 or more FAILs. Log each contact in `leads.csv`. *Assigned 2026-09-24, due 2026-09-25. **Overdue.** 0 rows as of Day 3. Weekend version: build a list of 30 qualified leads today, then contact them Monday 2026-09-28.*

## Blocked
- [ ] **Marketing**: The sales page can't go live until the founder provides name, phone, email, town and a Formspree form endpoint.

## Next (in priority order)
1. **Ops (founder)**: Create a Stripe account and two Payment Links: $150 deposit and $150 balance. $0 cost, about 20 minutes.
2. **Ops (founder)**: Create a free Formspree form, then send Claude the endpoint and contact details.
3. **Product (Claude)**: Fill in the sales page and deploy it to Netlify or Cloudflare Pages on the free tier. About 30 minutes after the details arrive.
4. **Marketing (founder)**: Run E1. Contact 30 local businesses and log each one in `leads.csv`.
5. **Marketing (founder)**: Run E2. Post the free-check offer in 3 local Facebook groups and on Nextdoor, where the rules allow business posts.
6. **Product (Claude)**: Deliver a website check within 24 hours of each reply.
