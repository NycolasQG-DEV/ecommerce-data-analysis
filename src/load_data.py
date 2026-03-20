import pandas as pd
import os

def load_data(base_path):
    return {
        "orders": pd.read_csv(os.path.join(base_path, "data/raw/orders.csv")),
        "items": pd.read_csv(os.path.join(base_path, "data/raw/order_items.csv")),
        "products": pd.read_csv(os.path.join(base_path, "data/raw/products.csv")),
    }