# Daily Operating Cycle

Run once a day until net profit holds at $100/day or more for 14 days in a row. Then move to **Scale mode** (bottom of this page).

| # | Step | Owner | How | Output |
|---|---|---|---|---|
| 1 | Finance report | Finance | Founder logs yesterday's money in `ledger.csv` and contacts in `leads.csv`, then runs `python3 report.py <yesterday>` and `python3 report.py` | Cash, revenue, expenses, profit, runway, funnel |
| 2 | Choose the single highest-leverage action | CEO | Find the weakest step in the chain *contacts → replies → checks sent → sales → delivery → cash*. Fix the earliest step that's below target. | One action |
| 3 | Assign owner | CEO | Ops, Marketing or Product. Name it and give it a deadline. | Card under Next / In Progress in `board.md` |
| 4 | Execute or verify | Owner | Claude does build, check and writing work. The founder does anything customer-facing. Claude confirms it happened by checking the log files, not by taking anyone's word for it. | Action completed, or marked Blocked with a reason |
| 5 | Measure | Finance | Money, or the leading indicator for the funnel step being worked on | Numbered result in `cycle-log.md` |
| 6 | Update capital allocation | CEO | Keep the money unless a spend has a way to bring in cash within 7 days | Decision in `cycle-log.md` |
| 7 | Kill or double down | CEO | Compare each experiment in `experiments.md` with its kill date and the signal it was supposed to show | Decision on each experiment |

## Daily targets (starting point, adjust weekly)
| Funnel step | Target per day |
|---|---|
| Contacts (walk-in, call or email) | 30 |
| Replies | 2 or more |
| Website checks sent (within 24h of a request) | Every request |
| Sales | 1 every 3 days in weeks 1–2, then 1 every 2 days by week 4 or earlier |

## Scale mode (after 14 days at $100/day or more)
1. Write down every step as a checklist a contractor can follow. Most of this is already in `sop-delivery.md`.
2. Raise the price to $399 on new leads. Keep it there if the close rate stays within 5 points of what it was at $299.
3. Test paid acquisition only if LTV:CAC is above 3 with organic leads. Cap the test at 10% of the last 7 days' profit.
4. Hire a part-time outreach person on commission (for example $50 per closed sale) once the founder's hours are the limit.
