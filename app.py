import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('superstore.csv', encoding='ISO-8859-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sidebar Filter
kategori = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

df_filtered = df[df['Category'].isin(kategori)]

# Metrik Total Profit
total_profit = df_filtered['Profit'].sum()
st.metric("Total Profit", f"${total_profit:,.2f}")

# Trend penjualan bulanan
df_filtered['Order Month'] = df_filtered['Order Date'].dt.to_period('M')
monthly_sales = df_filtered.groupby('Order Month')['Sales'].sum()
st.line_chart(monthly_sales)

# Profitabilitas per kategori
category_profit = df_filtered.groupby('Category')['Profit'].sum()
st.bar_chart(category_profit)