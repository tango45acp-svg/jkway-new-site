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
| Stripe fees on $299 (charged as $150 + $149) | $9.27 |
| Net per Fix-Up | $289.73 (96.9% margin) |
| Net per Care Plan per month | $47.28 |
| Human hours per Fix-Up | 3–5 (AI drafts, human reviews and deploys) |

**How we reach $100/day net (about $3,000/month):**
- **Option A:** 10.5 Fix-Ups a month, about 2.5 a week.
- **Option B:** 6 Fix-Ups plus 27 Care Plans. That's 6 × 289.73 + 27 × 47.28 = $1,738 + $1,277 = $3,015. This option is recurring, so it's the target by month 3.

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

## Operating rules (CEO)
- Only KPIs: **net daily profit** and **cash runway**.
- Reject any idea that needs more than $100 or takes more than 14 days to first dollar.
- No ad spend until organic demand is proven and unit economics are positive.
- Every expense must name an experiment and a way to bring in more cash within 7 days. `report.py` flags any that don't.
- Kill experiments on their kill date (`experiments.md`).

## Files
| File | Purpose | Owner |
|---|---|---|
| `board.md` | Task board: Done, In Progress, Blocked, Next | CEO |
| `experiments.md` | Experiments, kill dates, time-to-first-revenue, rejected ideas | CEO |
| `ledger.csv` | Every dollar with a running balance. The only source of truth for cash. | Finance |
| `leads.csv` | Every contact with its stage and outcome | Marketing |
| `report.py` | `python3 report.py [YYYY-MM-DD]` prints the daily P&L, runway, funnel, CPL/CAC and flags | Finance |
| `metrics.md` | Unit economics, break-even, LTV, metric definitions | Finance |
| `offer.md` | Packages, scope, terms | Product |
| `sop-delivery.md` | Check and Fix-Up procedure, quality standard, satisfaction criteria | Product |
| `audit-checklist.md` | The 10-point website check, with a worked example | Product |
| `outreach.md` | Scripts, follow-up schedule, organic channel plan | Marketing |
| `landing/index.html` | Sales page (fill in the `{{...}}` placeholders) | Marketing |
| `daily-report.md` | CEO report template | CEO |

## Daily routine (15 min)
1. Founder adds yesterday's money to `ledger.csv` (expenses as negative amounts) and yesterday's contacts to `leads.csv`.
2. Run `python3 report.py`. Fix any flags.
3. CEO review: update `board.md`, check each experiment against its kill date, and set the top 3 actions.
