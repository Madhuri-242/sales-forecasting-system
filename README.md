Sales Forecasting System
Business Problem
Forecast bookings from opportunity stages, opportunity age, historical conversions and sales rep activity with scenario-based uncertainty.

Technologies Used
Python
Pandas
Faker
MySQL
Dataset Volume
Territories: 10
Sales Reps: 2000
Accounts: 2000
Opportunities: 20000
Forecast Snapshots: 8 Quarters
Activities: 2000+
Territory Changes: 200
Ground Truth Labels: 5 anomaly types
Entities
Territory
SalesRep
Account
Opportunity
Stage
StageHistory
Activity
Quota
HistoricalBooking
ForecastSnapshot
TerritoryHistory
Forecast Logic
Forecast Amount = Opportunity Amount × Stage Probability

Stage Probabilities
Prospecting = 0.10
Qualification = 0.25
Proposal = 0.50
Negotiation = 0.75
Closed Won = 1.00
Closed Lost = 0.00
Additional Features
Deal Slippage
Stale Opportunities
Territory Changes
Historical Bookings
Quota Tracking
Ground Truth Labels
Validation Checks
Fixed Seed
20261022

Validation Results
Duplicate Opportunity IDs: 0
Invalid Dates: 0
Invalid References: 0
Invalid Stages: 0
Missing Values: 0
Output Files
territory.csv
sales_rep.csv
account.csv
opportunity.csv
forecast_snapshot.csv
stage_history.csv
activity.csv
historical_booking.csv
quota.csv
territory_history.csv
ground_truth.csv