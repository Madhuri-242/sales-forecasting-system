import pandas as pd

opp_df = pd.read_csv("opportunity.csv")

print("Total Records:", len(opp_df))

print("Duplicate Opportunity IDs:",
      opp_df["opp_id"].duplicated().sum())


invalid_dates = (
    pd.to_datetime(opp_df["expected_close_date"]) <
    pd.to_datetime(opp_df["create_date"])
)

print("Invalid Expected Close Dates:",
      invalid_dates.sum())

invalid_actual_dates = (
    pd.to_datetime(opp_df["actual_close_date"]) <
    pd.to_datetime(opp_df["create_date"])
)

print("Invalid Actual Close Dates:",
      invalid_actual_dates.sum())

print("\nMissing Values:")
print(opp_df.isnull().sum())
valid_stages = [
    "Prospecting",
    "Qualification",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost"
]
invalid_stage_count = (~opp_df["stage"].isin(valid_stages)).sum()
print("Invalid Stages:", invalid_stage_count)
print("Slipped Opportunities:",
      (opp_df["slippage_days"] > 0).sum())

account_df = pd.read_csv("account.csv")
sales_rep_df = pd.read_csv("sales_rep.csv")

invalid_accounts = (
    ~opp_df["account_id"].isin(account_df["account_id"])
).sum()

invalid_reps = (
    ~opp_df["rep_id"].isin(sales_rep_df["rep_id"])
).sum()

print("Invalid Account References:", invalid_accounts)
print("Invalid Sales Rep References:", invalid_reps)

expected_forecast = (
    opp_df["amount"] * opp_df["probability"]
)

incorrect_forecasts = (
    (opp_df["forecast_amount"] - expected_forecast).abs() > 0.01
).sum()

print("Incorrect Forecast Calculations:", incorrect_forecasts)

snapshot_df = pd.read_csv("forecast_snapshot.csv")

print("Total Forecast Snapshots:", len(snapshot_df))

snapshot_dates = pd.to_datetime(snapshot_df["snapshot_date"])
creation_dates = pd.to_datetime(
    opp_df.set_index("opp_id").loc[
        snapshot_df["opp_id"], "create_date"
    ].values
)

future_opportunities = (creation_dates > snapshot_dates).sum()

print("Opportunities Created After Snapshot:", future_opportunities)
print("Sales Reps:", len(pd.read_csv("sales_rep.csv")))
print("Accounts:", len(pd.read_csv("account.csv")))
print("Opportunities:", len(pd.read_csv("opportunity.csv")))
print("Forecast Snapshots:", len(pd.read_csv("forecast_snapshot.csv")))