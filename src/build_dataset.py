def build_dataset(orders, items, products):

    df = items.merge(orders, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")

    df["revenue"] = df["price_at_purchase"] * df["quantity"]

    return df