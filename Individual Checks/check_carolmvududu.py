import pandas as pd

# Load the survey data
df = pd.read_csv("Zim_cooking_fuels_-_all_versions_-_False_-_2026-11-12-06-31-58.csv", sep=';')

print("--- FIELDWORK DATA AUDIT (Enumerator 2) ---")

# 1. Check for missing expenditure (people who didn't buy fuel vs those who refused)
missing_exp = df[df['fuel_expenditure_usd'].isna()]
print(f"Total missing expenditure records: {len(missing_exp)}")
print(missing_exp[['case_id', 'domain', 'fuel_purchased', 'primary_fuel']])

# 2. Check for refusals
refusals = df[(df['primary_fuel'] == 'refused') | (df['has_improved_stove'] == 'refused')]
print(f"\nTotal refusals on key questions: {len(refusals)}")
print(refusals[['case_id', 'primary_fuel', 'has_improved_stove']])
