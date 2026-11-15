import pandas as pd

df = pd.read_csv("Zim_cooking_fuels_-_all_versions_-_False_-_2026-11-12-06-31-58.csv", sep=';')
df['exp_clean'] = pd.to_numeric(df['fuel_expenditure_usd'], errors='coerce')

# Check for outliers (valid range is 0 to 500)
invalid_values = df[(df['exp_clean'] > 500) | (df['exp_clean'] < 0)]
print(f"Number of invalid expenditure values (>500 or <0): {len(invalid_values)}")
