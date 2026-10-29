# Design Decisions

## 1. Forecasting Approach

**Formula:**

Forecast Amount = Opportunity Amount × Stage Probability

**Reason:** A simple, transparent baseline forecasting approach was selected because it is easy to understand, reproduce, and validate. Each opportunity's expected contribution is calculated using its amount and assigned stage probability.

**Trade-off:** This approach is interpretable but does not learn from historical conversion rates or adjust forecasts based on sales activity, deal age, or other predictive features.

## 2. Stage Probabilities

| Opportunity Stage | Probability |
|---|---:|
| Prospecting | 10% |
| Qualification | 25% |
| Proposal | 50% |
| Negotiation | 75% |
| Closed Won | 100% |
| Closed Lost | 0% |

**Reason:** Fixed probabilities provide a consistent baseline for estimating expected bookings at different stages of the sales pipeline.

**Trade-off:** These are illustrative assumptions, not probabilities trained or calibrated using historical conversion data.

## 3. Deal Slippage

Approximately 20% of generated opportunities are assigned a delayed close date, with delays ranging from 15 to 90 days.

**Reason:** To simulate sales delays and demonstrate how expected and actual close dates can differ.

**Limitation:** Slippage is synthetically generated and does not represent measured real-world delay patterns.

## 4. Stale Opportunities

Opportunities older than 120 days are marked as stale.

**Reason:** To identify long-running opportunities that may need additional review.

**Limitation:** Opportunity age is calculated from the generated opportunity dates, rather than being recalculated as of each forecast snapshot. Therefore, the stale indicator should be interpreted as a simplified dataset attribute.

## 5. Territory Changes

A subset of sales representatives is assigned a historical territory change, recorded with the previous territory, new territory, and effective date.

**Reason:** To represent organizational changes and retain a basic history of territory reassignment.

**Limitation:** Territory changes are simulated and are not applied dynamically to historical forecast snapshots.

## 6. Data Generation and Reproducibility

Synthetic datasets are generated using Python, Pandas, NumPy, and Faker. Python's random module and NumPy are initialized with a fixed seed.

**Reason:** Fixed seeds help make randomly generated values reproducible during development and validation.

**Limitation:** Faker must also be seeded for generated names and company names to be reproducible. Reproducibility should be verified after all random generators are configured.

## 7. Validation Strategy

The validation process checks:

- Duplicate opportunity IDs.
- Expected and actual close-date ordering.
- Missing values.
- Valid opportunity stages.
- Account and sales-representative references.
- Forecast calculation consistency.
- Forecast snapshot consistency, including opportunities created after a snapshot date.

**Reason:** These checks help identify data-quality issues and verify that key relationships and calculations are internally consistent.

**Limitation:** Passing these checks does not prove that the synthetic data reflects real-world sales behavior or that the forecast is accurate.

## Known Limitations

- The forecasting approach uses fixed stage probabilities rather than a trained predictive model.
- Historical conversion rates and sales activity do not influence the forecast calculation.
- Stage history is limited and does not represent complete opportunity-stage transitions.
- Deal slippage, stale opportunities, and territory changes are simulated.
- Historical bookings and quota data have limited scope and coverage.
- Forecast snapshots reuse generated opportunity attributes rather than reconstructing the complete state of the pipeline at each historical date.
- Ground-truth labels identify intended anomaly categories but do not, by themselves, demonstrate that corresponding anomalies have been injected into the data.

## Future Improvements

- Estimate stage probabilities using historical conversion outcomes.
- Incorporate activity metrics and opportunity age into forecasting.
- Generate complete stage-transition histories.
- Reconstruct historical pipeline states for each snapshot date.
- Expand quota and historical booking coverage.
- Inject and validate actual anomalies against the ground-truth labels.
- Evaluate forecast accuracy using appropriate historical holdout data.