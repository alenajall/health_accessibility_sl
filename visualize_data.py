
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create output folder
Path("outputs").mkdir(exist_ok=True)

# Load cleaned healthcare dataset
df = pd.read_csv(
    "outputs/health_facilities_cleaned.csv"
)

sns.set_theme(style="whitegrid")


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(
        f"outputs/{filename}",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


# CHART 1: Healthcare facilities by district
plt.figure(figsize=(12, 7))

district_counts = df["district"].value_counts()

sns.barplot(
    x=district_counts.values,
    y=district_counts.index,
    color="steelblue"
)

plt.title("Healthcare Facilities by District in Sierra Leone")
plt.xlabel("Number of Healthcare Facilities")
plt.ylabel("District")

save_chart("facilities_by_district.png")


# CHART 2: Healthcare facilities by type
plt.figure(figsize=(10, 6))

type_counts = df["type"].value_counts()

sns.barplot(
    x=type_counts.index,
    y=type_counts.values,
    color="seagreen"
)

plt.title("Healthcare Facilities by Type")
plt.xlabel("Facility Type")
plt.ylabel("Number of Facilities")
plt.xticks(rotation=30)

save_chart("facilities_by_type.png")


# CHART 3: Functional status
plt.figure(figsize=(8, 6))

status_counts = df["functional"].fillna(
    "Unknown"
).value_counts()

plt.pie(
    status_counts.values,
    labels=status_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Functional Status of Healthcare Facilities")

save_chart("facility_functionality.png")


# CHART 4: Healthcare facility ownership
plt.figure(figsize=(10, 6))

ownership_counts = df["ownership"].fillna(
    "Unknown"
).value_counts()

sns.barplot(
    x=ownership_counts.values,
    y=ownership_counts.index,
    color="mediumpurple"
)

plt.title("Healthcare Facilities by Ownership")
plt.xlabel("Number of Facilities")
plt.ylabel("Ownership")

save_chart("facility_ownership.png")

print("\nAll four charts generated successfully!")
