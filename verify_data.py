
import pandas as pd
from pathlib import Path

# Load original and cleaned datasets
original = pd.read_csv(
    "data/health_facilities_original.csv"
)

cleaned = pd.read_csv(
    "outputs/health_facilities_cleaned.csv"
)

Path("outputs").mkdir(exist_ok=True)

print("=" * 55)
print("FINAL DATA QUALITY VERIFICATION")
print("=" * 55)

# 1. Compare record counts
print("\n1. RECORD COUNT")
print("Original:", len(original))
print("Cleaned:", len(cleaned))
print("Records removed:", len(original) - len(cleaned))

# 2. Check duplicate rows
print("\n2. DUPLICATE ROWS")
print("Original:", original.duplicated().sum())
print("Cleaned:", cleaned.duplicated().sum())

# 3. Check missing values
print("\n3. MISSING VALUES AFTER CLEANING")
print(cleaned.isna().sum())

# 4. Validate geographical coordinates
invalid_gps = (
    ~cleaned["lat"].between(6.9, 10.1) |
    ~cleaned["long"].between(-13.5, -10.2)
)

print("\n4. GPS VALIDATION")
print("Invalid or missing coordinates:",
      invalid_gps.sum())

print("Zero coordinates remaining:",
      ((cleaned["lat"] == 0) |
       (cleaned["long"] == 0)).sum())

# 5. Check missing facility identifiers
missing_ids = (
    cleaned["dhis2_id"].isna() |
    cleaned["dhis2_id"].astype(str)
    .str.strip().str.lower()
    .isin(["no data", ""])
)

print("\n5. FACILITY IDENTIFIERS")
print("Missing/placeholder DHIS2 IDs:",
      missing_ids.sum())

# 6. Check district coverage
print("\n6. DISTRICT COVERAGE")
print("Original districts:",
      original["district"].nunique())
print("Cleaned districts:",
      cleaned["district"].nunique())

# 7. Create verification summary
summary = pd.DataFrame({
    "Metric": [
        "Total records",
        "Duplicate rows",
        "Zero-coordinate records",
        "Districts represented",
        "Missing/placeholder DHIS2 IDs"
    ],
    "Original": [
        len(original),
        original.duplicated().sum(),
        ((original["lat"] == 0) |
         (original["long"] == 0)).sum(),
        original["district"].nunique(),
        original["dhis2_id"].astype(str)
        .str.strip().str.lower()
        .isin(["no data", "", "nan"]).sum()
    ],
    "Cleaned": [
        len(cleaned),
        cleaned.duplicated().sum(),
        ((cleaned["lat"] == 0) |
         (cleaned["long"] == 0)).sum(),
        cleaned["district"].nunique(),
        missing_ids.sum()
    ]
})

summary.to_csv(
    "outputs/verification_summary.csv",
    index=False
)

print("\n7. VERIFICATION SUMMARY")
print(summary.to_string(index=False))

print("\nVerification completed!")
