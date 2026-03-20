import streamlit as st
import pandas as pd
import os

# configuração da página
st.set_page_config(page_title="Ecommerce Dashboard", layout="wide")

# caminho base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# carregar dados
file_path = os.path.join(BASE_DIR, "data", "processed", "final_dataset.csv")
df = pd.read_csv(file_path)

# título
st.title("Ecommerce Data Analysis")

# KPI
total_revenue = df["revenue"].sum()
st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")

# tratar data
df["order_date"] = pd.to_datetime(df["order_date"])

# sidebar (filtros)
st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["category"].dropna().unique())
)

if category != "All":
    df = df[df["category"] == category]

# layout em colunas
col1, col2 = st.columns(2)

# receita por categoria
with col1:
    st.subheader("Revenue by Category")
    category_data = df.groupby("category")["revenue"].sum().sort_values()
    st.bar_chart(category_data)

# receita ao longo do tempo
with col2:
    st.subheader("Revenue Over Time")
    time_data = df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()
    time_data.index = time_data.index.astype(str)
    st.line_chart(time_data)

# linha inferior
col3, col4 = st.columns(2)

# top produtos
with col3:
    st.subheader("Top Products")
    top_products = (
        df.groupby("product_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_products)

# top clientes
with col4:
    st.subheader("Top Customers")
    top_customers = (
        df.groupby("customer_id")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_customers)