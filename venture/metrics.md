# Metrics and Unit Economics

## Unit economics: Website Fix-Up
| Line | $ |
|---|---|
| Price | 299.00 |
| Stripe fees (two charges of $150 and $149: 2.9% + $0.30 each) | 9.27 |
| Delivery tools (Formspree free, Netlify free, Claude) | 0.00 |
| **Contribution per sale** | **289.73** |
| **Contribution margin** | **96.9%** (target is above 70%) |
| Founder time | about 4 hours, so about $72/hour effective |

## Unit economics: Care Plan
| Line | $ / month |
|---|---|
| Price | 49.00 |
| Stripe fee | 1.72 |
| **Contribution** | **47.28 (96.5%)** |

## Break-even
- Fixed costs right now are **$0/month**, so the business breaks even at 0 sales. The first sale is profit.
- If we buy a $12 domain later, break-even is 1 sale.
- **Goal: $100/day, or about $3,000/month.** Any one of these gets there:
  - 11 Fix-Ups a month
  - 6 Fix-Ups plus 27 Care Plans
  - 64 Care Plans
- Months 1–2 will be Fix-Ups. Care Plans build the recurring base.

## Lifetime value (assumptions, to be replaced with real data)
- Care Plan attach rate: 40% (assumed)
- Care Plan retention: 8 months (assumed)
- **LTV per customer** = 289.73 + 0.40 × 8 × 47.28 = **$441**

## Funnel metrics (calculated by `report.py` from `leads.csv` and `ledger.csv`)
| Metric | Definition |
|---|---|
| Cost per lead (CPL) | Expenses tagged to an experiment ÷ leads contacted in that experiment |
| Reply rate | Replied (or any later status) ÷ contacted |
| Check → win rate | Won ÷ checks sent |
| Customer acquisition cost (CAC) | Expenses tagged to an experiment ÷ customers won in it. It's $0 today. **Founder hours are tracked separately in `leads.csv` notes.** |
| LTV:CAC | Must stay above 3 before any paid acquisition |

## Status values in `leads.csv`
`stage` is the furthest step the lead has reached: `contacted` → `replied` → `audit_sent` → `call`.
`outcome` is `open`, `won` or `lost`.

## Spend rule
Any expense entry must name the experiment it serves and how it will bring in more cash within 7 days.
The report flags any expense that doesn't meet this rule.
