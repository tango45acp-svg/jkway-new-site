# Outreach Playbook

## Lead sourcing (free)
1. Search Google Maps for "[trade] near [town]" across plumbers, HVAC, salons, auto shops, restaurants, insurance agents, contractors and churches.
2. Qualify a business as a lead if it has **no website**, or its site shows any of these:
   - it isn't mobile-friendly
   - the copyright year is before 2024
   - a form doesn't work
   - there's placeholder text
   - the site is "not secure" (http only)
   - it loads slowly
3. Log each lead in a spreadsheet with these columns: business, contact, phone, email, url, issue_found, date_contacted, status.
   **Only log real businesses you've actually looked at. Don't bulk-scrape.**

Target: 30–50 contacts a day, starting with the founder's own town, where walk-ins and phone calls convert best.

## Script 1: Walk-in or phone call (highest conversion)
> Hi, I'm {{name}}. I'm local and I fix small business websites. I noticed {{specific issue, e.g. "your contact form doesn't send"}} on your site. I'll put together a free one-page report on what's broken, and there's no obligation. Who should I send it to?

## Script 2: Cold email (keep it CAN-SPAM compliant)
Subject: Quick issue on {{business}}'s website

> Hi {{first name}},
>
> I was looking at {{url}} and noticed {{specific issue}}. For example, {{concrete detail}}.
> That probably costs you a few calls a month.
>
> I put together a free one-page report on what I'd fix. Want me to send it over?
>
> {{name}}, {{phone}}
> {{physical mailing address}}
> Reply "no thanks" and I won't email again.

Rules:
- Send from a personal mailbox, 20–40 a day, and write every message by hand. Never buy lists.
- Honor opt-outs immediately.

## The daily 10-email batch (45 minutes, E3)
1. **15 min:** Search Google Maps for one trade in one town. For each business website, run `python3 check_site.py <url>` and keep the ones with 2 or more FAILs. Stop at 10.
2. **5 min:** Find a contact email for each: the site's contact page, or the Google Business Profile.
3. **20 min:** Send Script 2. Personalize the `{{specific issue}}` line from the checker output, but only with something you've seen yourself.
4. **5 min:** Add 10 rows to `leads.csv` with `channel=E3`, `stage=contacted`, `outcome=open`, then commit.

## Follow-up cadence
- Day 3: "Just bumping this in case it got buried."
- Day 7: Send the audit anyway, attached, with the $299 offer.
- Day 14: A final note, then mark the lead closed.

## Closing (after the audit)
> Everything in this report is covered by the $299 Fix-Up, delivered in 5 business days. It's half upfront and half on delivery. Here's the payment link: {{stripe link}}.

## Organic channels while cash is under $500 (no ad spend)
| Channel | How to use it | Rules |
|---|---|---|
| Local Facebook groups | Look for "Business Spotlight" or "Shop Local" threads. Post: "Free 10-point website check for {{town}} businesses. I'll tell you exactly what's broken, with no pitch unless you ask." | Read each group's rules first, and only post where promotion is allowed. |
| Nextdoor | Create a free business page and post the same free-check offer once. | One post per area. |
| LinkedIn | Connect with local business owners and chamber of commerce members. Post one teardown a week once E4 starts. | Anonymize every site unless the owner agrees to be named. |
| Reddit | Only subreddits that allow self-promotion (for example r/smallbusiness promo threads). | Mostly answer questions. Offer the check only when someone asks. |
| Chamber of commerce and BNI | Attend free visitor meetings and offer checks to members. | |

Every contact goes into `leads.csv`, with the `channel` column set to the experiment ID (E1–E4).
