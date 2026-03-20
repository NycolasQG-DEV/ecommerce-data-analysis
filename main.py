import os
from src.load_data import load_data
from src.build_dataset import build_dataset
from src.analysis import revenue_by_category
from src.visualization import plot_category_revenue

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data = load_data(BASE_DIR)

df = build_dataset(data["orders"], data["items"], data["products"])

category_rev = revenue_by_category(df)

from src.analysis import (
    revenue_by_category,
    revenue_over_time,
    top_products,
    top_customers
)

from src.visualization import (
    plot_category_revenue,
    plot_revenue_over_time,
    plot_top_products,
    plot_top_customers
)

category = revenue_by_category(df)
time = revenue_over_time(df)
products = top_products(df)
customers = top_customers(df)

plot_category_revenue(category, BASE_DIR)
plot_revenue_over_time(time, BASE_DIR)
plot_top_products(products, BASE_DIR)
plot_top_customers(customers, BASE_DIR)

output_path = os.path.join(BASE_DIR, "data", "processed", "final_dataset.csv")
df.to_csv(output_path, index=False)

