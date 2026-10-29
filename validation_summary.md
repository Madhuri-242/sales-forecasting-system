# Validation Summary

## 1. Dataset Statistics

| Metric | Validated Count |
|---|---:|
| Total Opportunities | 20,000 |
| Total Sales Representatives | 2,000 |
| Total Accounts | 2,000 |
| Total Forecast Snapshots | 103,628 |

## 2. Data Quality Validation Results

| Validation Check | Issues Found |
|---|---:|
| Duplicate Opportunity IDs | 0 |
| Invalid Expected Close Dates | 0 |
| Invalid Actual Close Dates | 0 |
| Missing Opportunity Values | 0 |
| Invalid Opportunity Stages | 0 |
| Invalid Account References | 0 |
| Invalid Sales Representative References | 0 |
| Incorrect Forecast Calculations | 0 |
| Opportunities Created After Snapshot Date | 0 |

## 3. Business Rule Implementation Status

| Feature | Status |
|---|---|
| Deal Slippage | Implemented in synthetic data generation |
| Stale Opportunity Tracking | Implemented |
| Territory Change History | Generated |
| Stage Probabilities | Applied using predefined values |
| Historical Bookings | Generated for closed-won opportunities |
| Quotas | Generated for sales representatives |
| Ground-Truth Labels | Generated for intended anomaly categories |

## 4. Validation Approach

The `validation.py` script checks opportunity-level data quality, selected foreign-key references, forecast calculation consistency, and whether opportunities existed by the dates associated with their forecast snapshots.

The checks returned zero issues for the conditions listed above.

## 5. Scope and Limitations

- Validation primarily checks `opportunity.csv` and selected relationships with other datasets.
- Not every CSV file has a dedicated set of validation checks.
- The checks do not establish that the synthetic data reflects real-world sales behavior or that forecasts are accurate.
- Ground-truth labels identify intended anomaly categories; corresponding anomalies have not necessarily been injected into the datasets.
- Business rule implementation does not imply that every rule has been independently validated.

## 6. Overall Status

**Result:** All checks implemented in `validation.py` passed for the reported run.

The results support the structural consistency of the tested data and calculations. Additional checks would be needed to validate every dataset, business rule, and forecasting assumption.

