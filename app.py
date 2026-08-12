import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Banking Customer Churn Analytics",
    layout="wide"
)

st.title("🏦 Banking Customer Churn Analytics")
st.write("Data Analytics Dashboard using Python and Streamlit")

# Load Dataset
df = pd.read_csv("Dataset/Bank Customer Churn Prediction.csv")

# KPI
total_customers = len(df)
churned_customers = int(df["churn"].sum())
churn_rate = df["churn"].mean() * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", total_customers)
col2.metric("Churned Customers", churned_customers)
col3.metric("Churn Rate", f"{churn_rate:.2f}%")

st.divider()

# Country-wise Churn
st.subheader("🌍 Country-wise Customer Churn")

country_churn = df.groupby("country")["churn"].sum()

fig, ax = plt.subplots()
country_churn.plot(kind="bar", ax=ax)
ax.set_xlabel("Country")
ax.set_ylabel("Churned Customers")
ax.set_title("Country-wise Customer Churn")
st.pyplot(fig)

# Gender-wise Churn
st.subheader("👥 Gender-wise Customer Churn")

gender_churn = df.groupby("gender")["churn"].sum()

fig, ax = plt.subplots()
gender_churn.plot(kind="bar", ax=ax)
ax.set_xlabel("Gender")
ax.set_ylabel("Churned Customers")
ax.set_title("Gender-wise Customer Churn")
st.pyplot(fig)

# Active Member vs Churn
st.subheader("🏃 Active Member vs Customer Churn")

active_churn = df.groupby("active_member")["churn"].sum()

fig, ax = plt.subplots()
active_churn.plot(kind="bar", ax=ax)
ax.set_xlabel("Active Member (0 = No, 1 = Yes)")
ax.set_ylabel("Churned Customers")
ax.set_title("Active Member vs Customer Churn")
st.pyplot(fig)

# Products vs Churn
st.subheader("📦 Number of Products vs Customer Churn")

product_churn = df.groupby("products_number")["churn"].sum()

fig, ax = plt.subplots()
product_churn.plot(kind="bar", ax=ax)
ax.set_xlabel("Number of Products")
ax.set_ylabel("Churned Customers")
ax.set_title("Products Number vs Customer Churn")
st.pyplot(fig)

# Data Preview
st.subheader("📊 Dataset Preview")
st.dataframe(df.head(10))