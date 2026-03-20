import matplotlib.pyplot as plt
import os

def plot_category_revenue(data, base_path):
    os.makedirs(os.path.join(base_path, "reports"), exist_ok=True)

    file_path = os.path.join(base_path, "reports", "category_revenue.png")

    data = data.sort_values()
    data.plot(kind="barh")

    plt.title("Receita por Categoria")
    plt.xlabel("Receita")
    plt.ylabel("Categoria")
    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()


def plot_revenue_over_time(data, base_path):
    file_path = os.path.join(base_path, "reports", "revenue_over_time.png")

    data.plot()

    plt.title("Receita ao Longo do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Receita")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()


def plot_top_products(data, base_path):
    file_path = os.path.join(base_path, "reports", "top_products.png")

    data.sort_values().plot(kind="barh")

    plt.title("Top Produtos")
    plt.xlabel("Receita")
    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()


def plot_top_customers(data, base_path):
    file_path = os.path.join(base_path, "reports", "top_customers.png")

    data.sort_values().plot(kind="barh")

    plt.title("Top Clientes")
    plt.xlabel("Receita")
    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()