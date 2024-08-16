from datetime import date
from typing import Any


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


def transform_dict(data_dict):
    data_dict['quantity'] = int(data_dict['quantity'])
    data_dict['price'] = int(data_dict['price'])
    data_dict['date'] = date.fromisoformat(data_dict['date'])
    return data_dict
