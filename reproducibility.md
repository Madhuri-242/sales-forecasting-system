# Reproducibility Report

## 1. Configuration

- **Generator:** `generator.py`
- **Configured Random Seed:** `20261022`
- **Libraries:** Python, Pandas, NumPy, Faker

Python's `random` module and NumPy are initialized with a fixed seed to improve reproducibility of the generated datasets.

## 2. Record Count Verification

### Run 1
- Sales Representatives: 2,000
- Accounts: 2,000
- Opportunities: 20,000
- Forecast Snapshots: 103,628

### Run 2
- Sales Representatives: 2,000
- Accounts: 2,000
- Opportunities: 20,000
- Forecast Snapshots: 103,628

## 3. Results

Both runs produced the same record counts for the listed datasets.

However, matching record counts alone do not establish that every generated value is identical between runs. Faker is not currently seeded separately, so generated names and company names may differ.

## 4. Limitations

- Faker requires separate seeding to make generated names and company names reproducible.
- Reproducibility of complete file contents has not been established solely by comparing record counts.
- Output consistency should be verified by comparing generated files or their checksums across independent runs.

## 5. Conclusion

The generator uses a fixed seed for Python's `random` module and NumPy, and two runs produced matching dataset record counts. Full dataset reproducibility remains to be verified because Faker is not separately seeded.