
import pandas as pd
from pathlib import Path

# Load the cleaned dataset
df = pd.read_csv("outputs/health_facilities_cleaned.csv")

Path("outputs").mkdir(exist_ok=True)

print("=" * 50)
print("SIERRA LEONE HEALTHCARE DATA ANALYSIS")
print("=" * 50)

# Facility distribution by district
district_counts = df["district"].value_counts()

print("\nTOP 5 DISTRICTS:")
print(district_counts.head(5))

print("\nBOTTOM 5 DISTRICTS:")
print(district_counts.tail(5))

# Facility types
print("\nHEALTHCARE FACILITY TYPES:")
print(df["type"].value_counts())

# Functionality
print("\nFACILITY FUNCTIONALITY:")
print(df["functional"].value_counts(dropna=False))

# Ownership
print("\nFACILITY OWNERSHIP:")
print(df["ownership"].value_counts(dropna=False))

# Save district summary
district_counts.rename_axis("district").reset_index(
    name="facility_count"
).to_csv(
    "outputs/district_analysis.csv",
    index=False
)

print("\nDistrict analysis saved successfully!")
