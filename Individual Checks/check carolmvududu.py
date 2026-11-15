import pandas as pd

df = pd.read_csv("Zim_cooking_fuels_-_all_versions_-_False_-_2026-11-12-06-31-58.csv", sep=';')

# Check for duplicates
duplicate_count = df['case_id'].duplicated().sum()
print(f"Number of duplicate case IDs: {duplicate_count}")
