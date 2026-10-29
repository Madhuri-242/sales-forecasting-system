# Sales Forecasting System

## 1. Business Problem

Sales teams need reliable booking forecasts based on opportunity stages, deal age, historical conversion patterns, and sales representative activity. Forecasts should also communicate uncertainty across different business scenarios.

This project builds a synthetic sales dataset and a baseline stage-weighted forecasting workflow. It also includes data-quality validation and a relational MySQL schema.

**Current scope:** The implemented forecast is a baseline calculation using opportunity amount and stage probability. Historical conversion modelling and scenario-based uncertainty are future enhancements, not currently implemented features.

## 2. Technologies Used

- Python
- Pandas
- NumPy
- Faker
- MySQL

## 3. Dataset Volume

| Entity or dataset | Volume |
|---|---:|
| Territories | 10 |
| Sales representatives | 2,000 |
| Accounts | 2,000 |
| Opportunities | 20,000 |
| Forecast snapshots | 103,628 records across 8 quarterly dates |
| Activities | 2,000 |
| Territory changes | 200 |
| Ground-truth labels | 5 |

*Note: There are eight configured snapshot dates. The number of snapshot records varies because an opportunity is included only when its creation date is on or before the snapshot date.*

## 4. Data Model

The project includes the following entities:

- Territory
- SalesRep
- Account
- Opportunity
- Stage
- StageHistory
- Activity
- Quota
- HistoricalBooking
- ForecastSnapshot
- TerritoryHistory

The generated CSV files provide synthetic records for the data model. `schema.sql` defines the intended relational database structure.

## 5. Forecast Logic

The baseline forecast calculation is:

```text
Forecast Amount = Opportunity Amount × Stage Probability
```

### Stage probabilities

| Opportunity stage | Probability |
|---|---:|
| Prospecting | 0.10 |
| Qualification | 0.25 |
| Proposal | 0.50 |
| Negotiation | 0.75 |
| Closed Won | 1.00 |
| Closed Lost | 0.00 |

The probability is assigned according to the opportunity's generated stage. The current implementation does not train a predictive model on historical conversion rates or incorporate activity metrics into the forecast calculation.

## 6. Additional Dataset Features

The synthetic datasets include:

- **Deal slippage:** Generated delays between expected and actual closing dates.
- **Stale opportunities:** Opportunities marked stale when the generated opportunity age exceeds 120 days.
- **Territory changes:** Synthetic representative territory-change records.
- **Historical bookings:** Records generated for opportunities assigned the Closed Won stage.
- **Quota tracking:** Representative sales targets for 2026 Q1.
- **Ground-truth labels:** Five reference labels covering intended anomaly categories.

## 7. Validation

The `validation.py` script checks for duplicate opportunity identifiers, invalid dates, missing values, invalid stages, invalid account and representative references, incorrect forecast calculations, and opportunities appearing after a snapshot date.

### Previously recorded validation results

| Validation check | Result |
|---|---:|
| Duplicate opportunity IDs | 0 |
| Invalid expected close dates | 0 |
| Invalid actual close dates | 0 |
| Invalid account references | 0 |
| Invalid sales representative references | 0 |
| Invalid stages | 0 |
| Missing opportunity values | 0 |
| Incorrect forecast calculations | 0 |
| Opportunities created after snapshot date | 0 |

These results reflect a previously reported run. Re-run the validation script to confirm the results for the current files.

## 8. Output Files

The generator creates the following CSV files:

- `territory.csv`
- `sales_rep.csv`
- `account.csv`
- `opportunity.csv`
- `forecast_snapshot.csv`
- `stage_history.csv`
- `activity.csv`
- `historical_booking.csv`
- `quota.csv`
- `territory_history.csv`
- `ground_truth.csv`

## 9. Setup and Execution

Run the following commands from the project directory in a Python environment.

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Generate synthetic datasets

```bash
python generator.py
```

### Validate generated data

```bash
python validation.py
```

The scripts write CSV files to the current working directory. The current Python workflow generates CSVs; it does not automatically load them into MySQL.

## 10. Reproducibility

The generator uses a fixed seed of `20261022` for Python's `random` module and NumPy. Faker should also be seeded explicitly if identical synthetic names are required across runs.

## 11. Known Limitations

1. Historical snapshots reuse the generated opportunity's current stage probability and forecast amount. They do not reconstruct historical stage values, creating a risk of temporal data leakage.
2. Opportunity stages are randomly assigned rather than generated through realistic stage transitions.
3. Closing dates are generated for all opportunities, including those not marked Closed Won.
4. Stage history covers only a subset of opportunities and does not contain complete stage-transition sequences.
5. Activities cover a subset of opportunities and currently use the opportunity creation date.
6. Quota data currently covers only 2026 Q1.
7. Ground-truth labels are reference records; the corresponding anomalies are not yet deliberately injected into the generated data.
8. Currency mismatch cannot currently be represented using the generated opportunity data because currency fields and conversion rates are not included.
9. The system does not yet implement historical conversion modelling, activity-based forecasting, or scenario-based uncertainty.

## 12. Future Enhancements

- Inject and validate the five intended anomaly types.
- Reconstruct leakage-free historical forecast snapshots.
- Model historical conversion rates by stage and other relevant dimensions.
- Incorporate representative activity and opportunity-age features into forecasting.
- Add best-case, base-case, and worst-case forecast scenarios.
- Extend quota coverage to additional quarters.
- Add CSV-to-MySQL loading instructions and verification queries.

## 13. Data Disclaimer

All generated records are synthetic and intended for development, testing, and demonstration purposes. They do not represent actual customers, employees, or sales transactions.
