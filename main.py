
import pandas as pd

# Load the original healthcare dataset
df = pd.read_csv("data/health_facilities_original.csv")

# Display basic dataset information
print("SIERRA LEONE HEALTHCARE DATASET")
print("=" * 40)

print("Total facilities:", df.shape[0])
print("Total columns:", df.shape[1])

print("\nFirst five records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nFacilities by district:")
print(df["district"].value_counts())
