import seaborn as sns
from datetime import date
import matplotlib.pyplot as plt


def make_sale_product_plot(sale_product_data: dict[str, int]) -> None:
    plt.figure(figsize=(15, 10))
    sns.barplot(sale_product_data)
    plt.xlabel('Продукт')
    plt.ylabel('Суммарная выручка')
    plt.title('Распределение выручки по продуктам')

    plt.savefig('sale-product-distribution.png')


def make_sale_date_plot(sale_date_data: dict[date, int]) -> None:
    plt.figure(figsize=(15, 10))
    sns.barplot(sale_date_data)
    plt.xlabel('Дата')
    plt.ylabel('Суммарная выручка')
    plt.title('Распределение выручки по датам')

    plt.savefig('sale-date-distribution.png')
