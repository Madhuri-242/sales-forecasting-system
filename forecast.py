
import pandas as pd

# Load the existing opportunity dataset
opportunity_df = pd.read_csv("opportunity.csv")

# Calculate the forecast amount for each opportunity
opportunity_df["calculated_forecast"] = (
    opportunity_df["amount"] * opportunity_df["probability"]
)

# Select the columns needed for the forecast output
forecast_df = opportunity_df[
    ["opp_id", "stage", "amount", "probability", "calculated_forecast"]
].copy()

# Save to a new file to preserve existing datasets
forecast_df.to_csv("forecast_output.csv", index=False)

# Display a summary
print("Forecast calculation completed successfully!")
print("Total opportunities:", len(forecast_df))
print(
    "Total forecast amount:",
    round(forecast_df["calculated_forecast"].sum(), 2)
)
print("Output file: forecast_output.csv")
