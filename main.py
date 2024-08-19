from analysis_tools import read_sales_data, sales_over_time, total_sales_per_product
from datetime import date
from make_plots import make_sale_product_plot, make_sale_date_plot


def get_max_sales_product(sales_per_product: dict[str, int]) -> str:
    product_of_max_sale, max_sale = max(sales_per_product.items(), key=lambda x: x[1])
    return product_of_max_sale


def get_date_of_max_sale(sales_per_date: dict[date, int]) -> date:
    date_of_max_sale, max_sale = max(sales_per_date.items(), key=lambda x: x[1])
    return date_of_max_sale


def main():
    data_path = 'tests/test_data.txt'
    sales_data = read_sales_data(data_path)

    sales_per_product = total_sales_per_product(sales_data)
    max_sales_product = get_max_sales_product(sales_per_product)
    print(f'Продукт, принесший максимальную выручку: {max_sales_product}')

    sales_per_date = sales_over_time(sales_data)
    max_sales_date = get_date_of_max_sale(sales_per_date)
    print(f'Дата наибольшей суммы продаж: {max_sales_date}')

    make_sale_product_plot(sales_per_product)
    make_sale_date_plot(sales_per_date)

    print('Графики распределения выручки по продуктам и дате успешно созданы')


if __name__ == '__main__':
    main()
