# Venture: Local Website Fix-Up Service ($100 seed)

> Kept in `venture/` on branch `claude/100-startup-business-agent-sorb0y`.
> **Don't merge this folder into `main`.** `main` publishes the J & K site to
> GitHub Pages, and this material shouldn't appear on that domain.

## The decision (CEO)
We sell **fixed-price fixes for small local business websites**, plus an optional monthly care plan.

Why this model:
| Criterion | Result |
|---|---|
| Startup cost | $0. Hosting runs on the free tiers of GitHub Pages, Netlify or Cloudflare Pages, and the client pays for their own domain. |
| Time to first dollar | Days. It's one conversation and one invoice. |
| Gross margin | About 95%. The only direct cost is Stripe's 2.9% + $0.30. |
| Delivery capacity | High. AI does most of the build, and a human reviews and ships. |
| Proof we can deliver | This repo. The J & K site has the same problems most local sites have (see `audit-checklist.md`). |

Models we rejected: paid ads (not enough capital), dropshipping (ad spend and refund risk), trading with the seed money (that's speculation, not a business), and content/affiliate (months before the first dollar).

## Unit economics (Finance)
| Item | Value |
|---|---|
| Website Fix-Up (one-time) | $299 |
| Care Plan (monthly) | $49 |
| Stripe fee on $299 | $8.97 ($299 × 2.9% + $0.30) |
| Net per Fix-Up | $290.03 |
| Net per Care Plan per month | $47.28 |
| Human hours per Fix-Up | 3–5 (AI drafts, human reviews and deploys) |

**How we reach $100/day net (about $3,000/month):**
- **Option A:** 10.5 Fix-Ups a month, about 2.5 a week.
- **Option B:** 6 Fix-Ups plus 27 Care Plans. That's 6 × 290.03 + 27 × 47.28 = $1,740 + $1,277 = $3,017. This option is recurring, so it's the target by month 3.

**Sales funnel assumptions.** Nothing is proven yet; replace these with real numbers after week 1.
- Cold contact → reply: 5–10%
- Reply → free audit delivered: 60%
- Audit → paid Fix-Up: 20–30%
- That works out to roughly 60–100 contacts per sale. Each week needs about 150–250 contacts through walk-ins, phone calls and email.

## Org chart and ownership
| Role | Owner | What they do |
|---|---|---|
| CEO | Claude plus the founder | Strategy, capital decisions, daily P&L review |
| Operations | Founder (human) | Accounts, deploys, client calls |
| Marketing | Founder sends, Claude drafts | Lead list, outreach, follow-ups |
| Product | Claude builds, founder QAs | Audits, site builds, delivery |
| Finance | Founder records, Claude reconciles | `ledger.csv`, `daily-report.md` |

**What Claude can't do:** send email, make calls, open Stripe or bank accounts, or receive money.
Every step that touches a customer or cash runs through the founder. Claude does the drafting, building and auditing, and verifies work from what the founder reports back.

## Files
- `ledger.csv`: every dollar in and out. This is the only source of truth for cash.
- `daily-report.md`: the daily CEO report template.
- `offer.md`: packages, scope and terms.
- `outreach.md`: lead sourcing, scripts and follow-up cadence.
- `audit-checklist.md`: the free 10-point audit used as a lead magnet, with a worked example on the J & K site.
- `landing/index.html`: the sales page. Fill in the `{{...}}` placeholders, then deploy it from its own repo.
