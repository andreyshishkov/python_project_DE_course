from typing import Any


def read_sales_data(file_path: str) -> list[dict[str, Any]]:
    with open(file_path) as file:
        lines = file.readlines()

    headers = ['product_name', 'quantity', 'price', 'date']
    data = []
    for line in lines:
        sale = line.split(', ')
        sale_dict = dict(zip(headers, sale))
        data.append(sale_dict)

    return data

