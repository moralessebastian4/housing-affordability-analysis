import pandas as pd
import matplotlib.pyplot as plt

income = pd.read_csv("MHI.csv")
housing = pd.read_csv("MSP.csv")

income["observation_date"] = pd.to_datetime(income["observation_date"])
housing["observation_date"] = pd.to_datetime(housing["observation_date"])

income["Year"] = income["observation_date"].dt.year
housing["Year"] = housing["observation_date"].dt.year

housing_yearly = housing.groupby("Year")["MSPUS"].mean().reset_index()

merged = pd.merge(income, housing_yearly, on="Year")

plt.figure(figsize=(10, 5))
plt.plot(merged["Year"], merged["MEHOINUSA672N"], label="Median Household Income")
plt.plot(merged["Year"], merged["MSPUS"], label="Median Home Price")

plt.title("Income vs Home Prices in the United States")
plt.xlabel("Year")
plt.ylabel("Dollars")
plt.legend()
plt.grid(True)

plt.show()

housing_affordability = merged["MSPUS"] / merged["MEHOINUSA672N"]
plt.figure(figsize=(10, 5))
plt.plot(merged["Year"], housing_affordability, label="Affordability Ratio (Income / Home Price)")
plt.title("Housing Affordability Ratio Over Time")
plt.xlabel("Year")
plt.ylabel("Affordability Ratio")
plt.legend()
plt.grid(True)
plt.show()