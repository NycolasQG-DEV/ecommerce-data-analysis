import pandas as pd

def revenue_by_category(df):
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)

def top_products(df):
    return df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(10)


def top_customers(df):
    return df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False).head(10)

def revenue_over_time(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()

def top_products(df):
    return df.groupby("product_name")["revenue"].sum().sort_values(ascending=False).head(10)

def top_customers(df):
    return df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False).head(10)
