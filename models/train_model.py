import pandas as pd

# Load dataset
df = pd.read_csv("data/student_dataset.csv")

# Encode target first
df["placement_status"] = df["placement_status"].map({
    "Placed": 1,
    "Not Placed": 0
})

print("Placement Distribution:")
print(df["placement_status"].value_counts())

print("\nTop Correlations with Placement:")
correlation = df.corr(numeric_only=True)["placement_status"]
print(correlation.sort_values(ascending=False))