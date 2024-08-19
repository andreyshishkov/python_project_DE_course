import seaborn as sns
import matplotlib.pyplot as plt


def make_sale_product_plot(sale_product_data: dict[str, int]) -> None:
    plt.figure(figsize=(15, 10))
    sns.barplot(sale_product_data)
    plt.xlabel('Продукт')
    plt.ylabel('Суммарная выручка')
    plt.title('Распределение выручки по продуктам')

    plt.savefig('sale-product-distribution.png')
