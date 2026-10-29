import random
import numpy as np
random.seed(20261022)
np.random.seed(20261022)
from datetime import date, timedelta
import pandas as pd
from faker import Faker
fake = Faker()

# Territory
territories = []
for i in range(1, 11):
    territories.append({
        "territory_id": f"TER-{i:03}",
        "territory_name": f"Territory {i}"
    })
territory_df = pd.DataFrame(territories)

# Sales Reps
sales_reps = []
for i in range(1, 2001):
    sales_reps.append({
        "rep_id": f"REP-{i:06}",
        "rep_name": fake.name(),
        "territory_id": f"TER-{((i-1)%10)+1:03}"
    })
sales_rep_df = pd.DataFrame(sales_reps)
print(sales_rep_df.head())

##Accounts
accounts = []
for i in range(1, 2001):
    accounts.append({
        "account_id": f"ACC-{i:06}",
        "account_name": fake.company(),
        "territory_id": f"TER-{((i-1)%10)+1:03}"
    })
account_df = pd.DataFrame(accounts)

print(account_df.head())
stages = [
    "Prospecting",
    "Qualification",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost"
]
stage_probability = {
    "Prospecting": 0.10,
    "Qualification": 0.25,
    "Proposal": 0.50,
    "Negotiation": 0.75,
    "Closed Won": 1.00,
    "Closed Lost": 0.00
}

##oppurtunities
opportunities = []
for i in range(1, 20001):
    create_date = date(2025, 1, 1) + timedelta(days=random.randint(0, 600))
    expected_close_date = create_date + timedelta(days=random.randint(30, 180))
    # 20% deals slip
    if random.random() < 0.20:
        actual_close_date = expected_close_date + timedelta(days=random.randint(15, 90))
    else:
        actual_close_date = expected_close_date
    slippage_days = (actual_close_date - expected_close_date).days
    opportunity_age = (actual_close_date - create_date).days
    is_stale = "Y" if opportunity_age > 120 else "N"
    opportunities.append({
        "opp_id": f"OPP-2026-{i:06}",
        "account_id": f"ACC-{random.randint(1,2000):06}",
        "rep_id": f"REP-{random.randint(1,2000):06}",
        "amount": random.randint(5000, 500000),
        "stage": random.choice(stages),
        "create_date": create_date,
        "expected_close_date": expected_close_date,
        "actual_close_date": actual_close_date,
        "slippage_days": slippage_days,
        "opportunity_age": opportunity_age,
        "is_stale": is_stale
    })
opportunity_df = pd.DataFrame(opportunities)
print(opportunity_df.head())
opportunity_df["probability"] = opportunity_df["stage"].map(stage_probability)
opportunity_df["forecast_amount"] = (
    opportunity_df["amount"] *
    opportunity_df["probability"]
)
print(
    opportunity_df[
        ["opp_id", "amount", "stage",
         "probability", "forecast_amount"]
    ].head()
)

##Forecast snapshot

## Forecast snapshot

snapshot_dates = [
    "2025-03-31",
    "2025-06-30",
    "2025-09-30",
    "2025-12-31",
    "2026-03-31",
    "2026-06-30",
    "2026-09-30",
    "2026-12-31"
]

snapshots = []
counter = 1

for snapshot_date in snapshot_dates:
    snapshot_date_obj = pd.to_datetime(snapshot_date).date()

    for _, row in opportunity_df.iterrows():
        if row["create_date"] <= snapshot_date_obj:
            snapshots.append({
                "snapshot_id": f"FCST-{counter:06}",
                "opp_id": row["opp_id"],
                "snapshot_date": snapshot_date,
                "forecast_amount": row["forecast_amount"],
                "probability": row["probability"]
            })
            counter += 1

snapshot_df = pd.DataFrame(snapshots)

print("Total Snapshots:", len(snapshot_df))


##Stagehistory
stage_history = []
for i, row in opportunity_df.head(1000).iterrows():
    stage_history.append({
        "stage_history_id": f"STG-{row['opp_id']}-001",
        "opp_id": row["opp_id"],
        "stage_name": row["stage"],
        "change_date": row["create_date"]
    })
stage_history_df = pd.DataFrame(stage_history)
print(stage_history_df.head())
activity_types = ["Call", "Email", "Meeting", "Demo"]

##Activity
activities = []
for i, row in opportunity_df.head(2000).iterrows():
    activities.append({
        "activity_id": f"ACT-{i+1:06}",
        "opp_id": row["opp_id"],
        "rep_id": row["rep_id"],
        "activity_type": random.choice(activity_types),
        "activity_date": row["create_date"]
    })
activity_df = pd.DataFrame(activities)
print(activity_df.head())
activity_df.to_csv("activity.csv", index=False)

print("Total Snapshots:", len(snapshot_df))
print("Total Opportunities:", len(opportunity_df))
territory_df.to_csv("territory.csv", index=False)
sales_rep_df.to_csv("sales_rep.csv", index=False)
account_df.to_csv("account.csv", index=False)
opportunity_df.to_csv("opportunity.csv", index=False)
snapshot_df.to_csv("forecast_snapshot.csv", index=False)
stage_history_df.to_csv("stage_history.csv", index=False)
print("CSV files created successfully")

##ground truth
ground_truth = [
    {"issue_id":"GT-001","opp_id":"OPP-2026-000001","issue_type":"LEAKAGE"},
    {"issue_id":"GT-002","opp_id":"OPP-2026-000002","issue_type":"INVALID_DATE"},
    {"issue_id":"GT-003","opp_id":"OPP-2026-000003","issue_type":"PROBABILITY_MISMATCH"},
    {"issue_id":"GT-004","opp_id":"OPP-2026-000004","issue_type":"DUPLICATE_OPPORTUNITY"},
    {"issue_id":"GT-005","opp_id":"OPP-2026-000005","issue_type":"CURRENCY_MISMATCH"}
]
ground_truth_df = pd.DataFrame(ground_truth)
print(ground_truth_df)
ground_truth_df.to_csv("ground_truth.csv", index=False)

bookings = []
for i, row in opportunity_df.iterrows():
    if row["stage"] == "Closed Won":
        bookings.append({
            "booking_id": f"BOOK-{i+1:06}",
            "opp_id": row["opp_id"],
            "booking_amount": row["amount"],
            "booking_date": row["actual_close_date"]
        })
booking_df = pd.DataFrame(bookings)
print(booking_df.head())
booking_df.to_csv("historical_booking.csv", index=False)

quotas = []
for i in range(1, 2001):
    quotas.append({
        "quota_id": f"QUOTA-REP-{i:06}-2026Q1",
        "rep_id": f"REP-{i:06}",
        "quarter": "2026Q1",
        "target_amount": random.randint(500000, 2000000)
    })
quota_df = pd.DataFrame(quotas)
print(quota_df.head())
quota_df.to_csv("quota.csv", index=False)

territory_history = []
for i in range(1, 201):   # 200 reps change territory
    old_territory = f"TER-{random.randint(1,10):03}"
    new_territory = f"TER-{random.randint(1,10):03}"
    while new_territory == old_territory:
        new_territory = f"TER-{random.randint(1,10):03}"
    territory_history.append({
        "history_id": f"TH-{i:06}",
        "rep_id": f"REP-{i:06}",
        "old_territory_id": old_territory,
        "new_territory_id": new_territory,
        "change_date": "2026-01-01"
    })
territory_history_df = pd.DataFrame(territory_history)
print(territory_history_df.head())
territory_history_df.to_csv("territory_history.csv", index=False)