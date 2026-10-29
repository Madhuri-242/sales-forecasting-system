# AI Usage Disclosure

## AI Tool Used
- Microsoft Copilot (GPT)

## How AI Assisted
AI was used as a support tool during development to:
- Suggest database schema design and entity relationships.
- Assist with synthetic dataset generation logic.
- Suggest baseline forecasting calculations.
- Help develop data validation checks.
- Assist with project documentation and organization.

## What I Personally Reviewed
I reviewed the following components to understand their logic and implementation:
- SQL table definitions and relationships.
- Foreign key constraints.
- Opportunity generation logic.
- Forecast calculation logic.
- Forecast snapshot generation.
- Data validation rules.

## What I Personally Modified
My contributions included:
- Adjusting dataset sizes to 2,000 sales representatives, 2,000 accounts, and 20,000 opportunities.
- Implementing opportunity slippage logic.
- Adding stale opportunity tracking.
- Adding territory history tracking.
- Creating and verifying MySQL tables.

## Validation Performed
I ran validation checks covering:
- Duplicate opportunity IDs.
- Invalid dates.
- Missing values.
- Invalid stages and foreign-key references.
- Forecast calculation consistency.
- Forecast snapshot consistency.

## Limitations and Responsibility
AI-assisted suggestions were reviewed and tested where applicable. I remain responsible for understanding the submitted code, its assumptions, its limitations, and the accuracy of the documentation. The current forecasting calculation is a baseline stage-probability-weighted estimate, not a trained forecasting model.

This disclosure summarizes the AI assistance used during development. The separate prompt-history document records the prompts available for submission and identifies any gaps in the historical record.