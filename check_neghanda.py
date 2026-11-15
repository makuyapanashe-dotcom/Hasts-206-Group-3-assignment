import pandas as pd

df = pd.read_csv("Zim_cooking_fuels_-_all_versions_-_False_-_2026-11-12-06-31-58.csv", sep=';')

# Print a crosstab of fuel types by domain
fuel_by_domain = pd.crosstab(df['primary_fuel'], df['domain'])
print(fuel_by_domain)
