
import pandas as pd
from pathlib import Path

# STEP 1: Create output folder
Path("outputs").mkdir(exist_ok=True)

# STEP 2: Load original dataset
df = pd.read_csv(
    "data/health_facilities_original.csv",
    keep_default_na=False
)

print("SIERRA LEONE HEALTHCARE DATA CLEANING")
print("=" * 50)
print("Original records:", len(df))

# STEP 3: Replace blank text with missing values
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()
    df[col] = df[col].replace("", pd.NA)

print("\nMissing values before further cleaning:")
print(df.isna().sum())

# STEP 4: Remove completely identical rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates().copy()

print("\nExact duplicates removed:", duplicates)

# STEP 5: Standardize selected text columns
columns_to_standardize = [
    "district", "community", "facility",
    "fac_name", "type", "ownership", "functional"
]

for col in columns_to_standardize:
    df[col] = df[col].str.strip()

# STEP 6: Validate GPS coordinates
df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
df["long"] = pd.to_numeric(df["long"], errors="coerce")

# Approximate bounding box of Sierra Leone
invalid_coordinates = (
    ~df["lat"].between(6.9, 10.1) |
    ~df["long"].between(-13.5, -10.2)
)

print("Invalid or missing GPS locations:",
      invalid_coordinates.sum())

# Keep facilities but mark invalid coordinates as missing
df.loc[invalid_coordinates, ["lat", "long"]] = pd.NA

# STEP 7: Investigate repeated facility identifiers
repeated_ids = df[
    df["dhis2_id"].notna() &
    df["dhis2_id"].duplicated(keep=False)
].copy()

print("Records with repeated DHIS2 identifiers:",
      len(repeated_ids))

repeated_ids.to_csv(
    "outputs/repeated_dhis2_ids.csv",
    index=False
)

# STEP 8: Save cleaned dataset
df.to_csv(
    "outputs/health_facilities_cleaned.csv",
    index=False
)

# STEP 9: Save data-quality summary
summary = pd.DataFrame({
    "column": df.columns,
    "missing_values": df.isna().sum().values,
    "data_type": df.dtypes.astype(str).values
})

summary.to_csv(
    "outputs/data_quality_summary.csv",
    index=False
)

# STEP 10: Final verification
print("\nCLEANING SUMMARY")
print("=" * 50)
print("Final records:", len(df))
print("Final columns:", len(df.columns))
print("Remaining exact duplicates:",
      df.duplicated().sum())

print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")

