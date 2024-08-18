from datetime import date
from typing import Any
from collections import defaultdict


def read_sales_data(file_path: str) -> list[dict[str, Any]]:
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()

    headers = ['product_name', 'quantity', 'price', 'date']
    data = []
    for line in lines:
        line = line.strip('\n')
        sale = line.split(', ')
        sale_dict = dict(zip(headers, sale))
        sale_dict = transform_dict(sale_dict)
        data.append(sale_dict)

    return data


def total_sales_per_product(sales_data: list[dict[str, Any]]) -> dict[str, int]:
    total_sales = defaultdict(int)
    for record in sales_data:
        product_name = record['product_name']
        sale = record['quantity'] * record['price']
        total_sales[product_name] += sale

    return dict(total_sales)


def sales_over_time(sales_data: list[dict[str, Any]]) -> dict[date, int]:
    date_sales = defaultdict(int)
    for record in sales_data:
        timestamp = record['date']
        sale = record['quantity'] * record['price']
        date_sales[timestamp] += sale
    return dict(date_sales)


def transform_dict(data_dict):
    data_dict['quantity'] = int(data_dict['quantity'])
    data_dict['price'] = int(data_dict['price'])
    data_dict['date'] = date.fromisoformat(data_dict['date'])
    return data_dict
