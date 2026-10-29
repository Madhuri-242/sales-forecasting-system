# AI Prompt History

## Purpose

This document records the AI assistance used during development of the Synthetic Sales Forecasting System. Some entries below are reconstructed summaries of the development requests rather than exact verbatim prompts. They are identified as reconstructed to distinguish them from the original prompt history.

**AI Tool:** Microsoft Copilot (GPT)  
**Project:** Synthetic Sales Forecasting System

---

## 1. Database Schema Design

**Prompt record type:** Reconstructed summary

**Prompt summary:** Help design a MySQL database schema for a sales forecasting system, including territories, sales representatives, accounts, opportunities, opportunity stages, forecast snapshots, stage history, activities, historical bookings, quotas, and territory history.

**Outcome:** A proposed relational schema was used as a starting point for `schema.sql`. Table relationships and foreign-key definitions were reviewed during development.

**Personal review:** Reviewed table definitions, relationships, and foreign-key constraints.

## 2. Synthetic Dataset Generation

**Prompt record type:** Reconstructed summary

**Prompt summary:** Help create a Python data generator using Faker, Pandas, NumPy, and business rules to generate synthetic sales territories, sales representatives, accounts, and opportunities.

**Outcome:** Development of `generator.py` to generate synthetic CSV datasets. Dataset sizes were adjusted to 2,000 sales representatives, 2,000 accounts, and 20,000 opportunities.

**Personal modifications:** Added deal-slippage logic, stale-opportunity tracking, and territory history generation.

## 3. Forecast Calculation

**Prompt record type:** Reconstructed summary

**Prompt summary:** Help implement a simple, explainable sales forecast using opportunity amount and probability assigned to the opportunity stage.

**Outcome:** The baseline formula was implemented:

`Forecast Amount = Opportunity Amount × Stage Probability`

The forecasting approach uses fixed stage probabilities and does not train a predictive model.

**Personal review:** Reviewed the formula and compared calculated forecast values with the expected values.

## 4. Forecast Snapshot Generation

**Prompt record type:** Reconstructed summary

**Prompt summary:** Help generate forecast snapshots across multiple reporting dates while ensuring that opportunities are not included before their creation dates.

**Outcome:** `generator.py` produces `forecast_snapshot.csv` with 103,628 records across eight snapshot dates.

**Personal review:** Checked snapshot record counts and verified that no included opportunity was created after its snapshot date.

## 5. Data Validation

**Prompt record type:** Reconstructed summary

**Prompt summary:** Help develop validation checks for duplicate opportunity IDs, invalid dates, missing values, invalid stages, account and sales-representative references, forecast calculations, and snapshot consistency.

**Outcome:** Validation logic was implemented in `validation.py`. The reported run found zero issues for the checks performed.

**Personal review:** Ran the validation script and documented its reported results in `validation_summary.md`.

## 6. Documentation

**Prompt record type:** Reconstructed summary

**Prompt summary:** Help organize technical documentation explaining project assumptions, data sources, database design, validation results, reproducibility, AI assistance, and known limitations.

**Outcome:** Documentation was prepared or revised across `README.md`, `data_dictionary.md`, `design_decisions.md`, `source_manifest.md`, `validation_summary.md`, `reproducibility.md`, and `ai_usage.md`.

**Personal review:** Reviewed the documentation for consistency with the implemented code and disclosed known limitations.

## 7. Forecast Script Verification

**Prompt record type:** Actual prompt from the development conversation

**Prompt:** Help me troubleshoot step by step without overwriting existing project files.

**Outcome:** The existing CSV files were inspected before changes were made. The empty `forecast.py` file was populated with a baseline forecast calculation that reads `opportunity.csv` and writes the results to `forecast_output.csv`. The script reported 20,000 opportunities and a total forecast amount of ₹2,184,647,801.90.

---

## Limitations of This Record

This document is not a complete verbatim export of every AI interaction. Reconstructed entries summarize the types of assistance used during development and must not be treated as exact original prompts.

The project author is responsible for reviewing the implementation, verifying the results, understanding the design decisions, and disclosing any limitations in the submitted solution.