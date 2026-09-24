#!/usr/bin/env python3
"""Daily P&L and funnel report from ledger.csv and leads.csv.

Usage: python3 report.py [YYYY-MM-DD]   (defaults to today)
"""
import csv
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
STAGES = ["contacted", "replied", "audit_sent", "call"]  # furthest stage reached
# outcome column: open | won | lost


def load(name):
    with open(HERE / name, newline="") as f:
        return list(csv.DictReader(f))


def main():
    day = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    week_start = day - timedelta(days=day.weekday())
    ledger = load("ledger.csv")

    balance, problems, unflagged = 0.0, [], []
    rev_day = exp_day = rev_week = 0.0
    exp_by_exp = defaultdict(float)
    for i, row in enumerate(ledger, start=2):
        amt = float(row["amount_usd"])
        d = date.fromisoformat(row["date"])
        cat = row["category"]
        if cat == "expense" and amt > 0:
            problems.append(f"line {i}: expense amount must be negative")
        balance += amt
        if abs(balance - float(row["balance_usd"])) > 0.005:
            problems.append(f"line {i}: balance_usd {row['balance_usd']} != computed {balance:.2f}")
        if cat == "expense":
            exp_by_exp[row["experiment"]] += -amt
            if row["experiment"] in ("", "-"):
                unflagged.append(f"line {i}: {row['description']} (no experiment / 7-day cash path)")
        if d == day:
            rev_day += amt if cat == "revenue" else 0
            exp_day += -amt if cat == "expense" else 0
        if week_start <= d <= day and cat == "revenue":
            rev_week += amt

    # Trailing 7-day burn for runway.
    burn7 = sum(-float(r["amount_usd"]) for r in ledger
                if r["category"] == "expense"
                and day - timedelta(days=6) <= date.fromisoformat(r["date"]) <= day) / 7
    runway = f"{balance / burn7:.0f} days" if burn7 > 0 else "unlimited ($0 burn)"

    print(f"=== Daily report {day} ===")
    print(f"Revenue today:   ${rev_day:,.2f}   (week to date ${rev_week:,.2f})")
    print(f"Expenses today:  ${exp_day:,.2f}")
    print(f"Net today:       ${rev_day - exp_day:,.2f}")
    print(f"Cash on hand:    ${balance:,.2f}")
    print(f"Runway:          {runway}")

    leads = load("leads.csv")
    print("\n=== Funnel by experiment ===")
    if not leads:
        print("No leads logged yet.")
    by_exp = defaultdict(list)
    for r in leads:
        by_exp[r["channel"]].append(r)
    for exp, rows in sorted(by_exp.items()):
        n = len(rows)
        won = sum(r["outcome"] == "won" for r in rows)

        def reached(stage):
            return sum(r["outcome"] == "won" or STAGES.index(r["stage"]) >= STAGES.index(stage)
                       for r in rows)

        replied, audits = reached("replied"), reached("audit_sent")
        rev = sum(float(r["revenue_usd"] or 0) for r in rows)
        spend = exp_by_exp.get(exp, 0.0)
        win_rate = f"{won / audits:.0%}" if audits else "n/a"
        print(f"{exp}: contacted {n} | replied {replied} ({replied / n:.0%}) | "
              f"audits {audits} | won {won} (audit->win {win_rate})")
        print(f"    spend ${spend:.2f} | CPL ${spend / n:.2f} | CAC "
              f"{'$%.2f' % (spend / won) if won else 'n/a'} | revenue ${rev:,.2f}")

    if problems or unflagged:
        print("\n=== FLAGS ===")
        for p in problems + unflagged:
            print("!", p)


if __name__ == "__main__":
    main()
