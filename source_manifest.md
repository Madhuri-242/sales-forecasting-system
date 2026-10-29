# Source Manifest

## 1. Project Information

- **Project Name:** Sales Forecasting System
- **Project Type:** Synthetic Sales Forecasting Dataset
- **Data Source:** Synthetic data generated using Python Faker, Python's random module, NumPy, and predefined business rules.
- **External Data Used:** None. No real customer or proprietary business data is included.
- **Database:** MySQL schema provided in `schema.sql`.
- **Data Generator:** `generator.py`
- **Validation Script:** `validation.py`

## 2. Random Seed and Reproducibility

- **Configured Seed:** `20261022`
- Python's `random` module and NumPy are initialized with the configured seed.
- Faker is not currently seeded separately, so generated names and company names may vary between runs. Fully reproducible output requires seeding Faker as well.

## 3. Generated Files

| File | Purpose |
|---|---|
| `territory.csv` | Synthetic sales territories |
| `sales_rep.csv` | Synthetic sales representatives |
| `account.csv` | Synthetic customer accounts |
| `opportunity.csv` | Opportunity details, stages, amounts, dates, and forecast values |
| `forecast_snapshot.csv` | Forecast records across eight snapshot dates |
| `stage_history.csv` | Limited opportunity stage-history records |
| `activity.csv` | Synthetic sales activity records |
| `historical_booking.csv` | Booking records generated for closed-won opportunities |
| `quota.csv` | Sales quota records |
| `territory_history.csv` | Simulated territory reassignment records |
| `ground_truth.csv` | Labels identifying intended anomaly categories |

## 4. Data Generation

The datasets are generated locally using Python and predefined rules. Opportunity amounts, stages, dates, close-date slippage, and other attributes are synthetically assigned.

The datasets are intended for demonstrating data generation, baseline sales forecasting, database design, and validation. They do not represent actual business performance.

## 5. Validation

The `validation.py` script checks selected data-quality rules, including:
- Duplicate opportunity IDs.
- Date ordering.
- Missing values.
- Valid opportunity stages.
- Account and sales-representative references.
- Forecast calculation consistency.
- Forecast snapshot consistency.

These checks verify selected structural and calculation rules; they do not establish real-world forecasting accuracy.

## 6. Known Data Limitations

- Data is synthetic and generated from simplified business rules.
- Python's random module and NumPy are seeded, but Faker is not yet seeded separately.
- Historical stage transitions and quota coverage are limited.
- Ground-truth anomaly labels do not necessarily correspond to anomalies injected into the datasets.

