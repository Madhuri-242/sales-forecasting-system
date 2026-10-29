Design Decisions

1. Forecasting Approach

Forecast Amount = Opportunity Amount × Stage Probability

Reason:
A simple, transparent forecasting model that is easy to validate and explain.

2. Stage Probabilities

Prospecting = 10%
Qualification = 25%
Proposal = 50%
Negotiation = 75%
Closed Won = 100%
Closed Lost = 0%

Reason:
These probabilities represent the likelihood of converting an opportunity at each sales stage.

3. Deal Slippage

20% of opportunities are delayed beyond the expected close date.

Reason:
To simulate real-world sales delays and forecast uncertainty.

4. Stale Opportunities

Opportunities older than 120 days are marked as stale.

Reason:
Long-running deals often require special attention and may impact forecast accuracy.

5. Territory Changes

A subset of sales reps are reassigned to different territories.

Reason:
To simulate organizational changes and preserve history.

6. Validation Strategy

Validation checks include:
- Duplicate IDs
- Date ordering
- Missing values
- Foreign key integrity
- Forecast calculation verification
- Snapshot consistency

Reason:
To ensure generated data is accurate and internally consistent.

Limitations

- Simplified forecasting model
- Limited stage history transitions
- Territory changes are simulated
- Historical conversion logic is simplified