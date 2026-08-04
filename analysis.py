import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset\Bank Customer Churn Prediction.csv")
print(df.head())
print("Rows and Columns:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())
# Churn Analysis

print("\nChurn Count:")
print(df["churn"].value_counts())

print("\nChurn Percentage:")
print(df["churn"].value_counts(normalize=True) * 100)

print("\nTotal Customers:")
print(len(df))

print("\nChurned Customers:")
print(df["churn"].sum())

print("\nChurn Rate:")
print(df["churn"].mean() * 100)
# Step 6: Data Cleaning

print("\n--- Data Cleaning ---")

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())
# Duplicate rows check
print("\nDuplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)
print("\nData Types:")
print(df.dtypes)
df.to_csv("Dataset/cleaned_bank_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")
# Step 7: Exploratory Data Analysis

# Churn Count
churn_counts = df["churn"].value_counts()

# Bar Chart
plt.bar(["Not Churned", "Churned"], churn_counts)

plt.title("Customer Churn Analysis")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")

plt.show()
# Country-wise Churn Analysis

country_churn = df.groupby("country")["churn"].sum()

print("\nCountry-wise Churn:")
print(country_churn)

# Bar Chart
country_churn.plot(kind="bar")

plt.title("Country-wise Customer Churn")
plt.xlabel("Country")
plt.ylabel("Number of Churned Customers")

plt.show()
# Country-wise Churn Analysis

country_churn = df.groupby("country")["churn"].sum()

print("\nCountry-wise Churn:")
print(country_churn)

# Bar Chart
country_churn.plot(kind="bar")

plt.title("Country-wise Customer Churn")
plt.xlabel("Country")
plt.ylabel("Number of Churned Customers")

plt.show()
# Gender-wise Churn Analysis

gender_churn = df.groupby("gender")["churn"].sum()

print("\nGender-wise Churn:")
print(gender_churn)

# Bar Chart
gender_churn.plot(kind="bar")

plt.title("Gender-wise Customer Churn")
plt.xlabel("Gender")
plt.ylabel("Number of Churned Customers")

plt.show()
# Age-wise Churn Analysis

age_churn = df.groupby("age")["churn"].sum()

print("\nAge-wise Churn:")
print(age_churn)

# Line Chart
age_churn.plot(kind="line", marker="o")

plt.title("Age-wise Customer Churn")
plt.xlabel("Age")
plt.ylabel("Number of Churned Customers")

plt.grid(True)
plt.show()
# Active Member vs Churn Analysis

active_churn = df.groupby("active_member")["churn"].sum()

print("\nActive Member vs Churn:")
print(active_churn)

# Bar Chart
active_churn.plot(kind="bar")

plt.title("Active Member vs Customer Churn")
plt.xlabel("Active Member (0 = No, 1 = Yes)")
plt.ylabel("Number of Churned Customers")

plt.show()
# Number of Products vs Churn Analysis

product_churn = df.groupby("products_number")["churn"].sum()

print("\nProducts Number vs Churn:")
print(product_churn)

# Bar Chart
product_churn.plot(kind="bar")

plt.title("Number of Products vs Customer Churn")
plt.xlabel("Number of Products")
plt.ylabel("Number of Churned Customers")

plt.show()
# Credit Score vs Churn Analysis

# Credit Score ko 3 groups me divide karna
df["credit_score_group"] = pd.cut(
    df["credit_score"],
    bins=[0, 580, 669, 739, 799, 850],
    labels=["Poor", "Fair", "Good", "Very Good", "Excellent"]
)

credit_churn = df.groupby("credit_score_group", observed=False)["churn"].sum()

print("\nCredit Score Group vs Churn:")
print(credit_churn)

# Bar Chart
credit_churn.plot(kind="bar")

plt.title("Credit Score Group vs Customer Churn")
plt.xlabel("Credit Score Group")
plt.ylabel("Number of Churned Customers")

plt.show()
# Step 8: SQL Database Creation

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("SQL/banking_churn.db")

# Save DataFrame into SQL table
df.to_sql("customers", connection, if_exists="replace", index=False)

print("\nSQL Database created successfully!")

# Close connection
connection.close()
