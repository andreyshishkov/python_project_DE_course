from analysis_tools import read_sales_data, total_sales_per_product
from datetime import date


def test_read_sales_data():
    test_path = 'tests/test_sample_small.txt'
    true_data = [
        {
            'product_name': 'яблоки',
            'quantity': 10,
            'price': 15,
            'date': date.fromisoformat('2024-06-21'),
        },
        {
            'product_name': 'груши',
            'quantity': 16,
            'price': 11,
            'date': date.fromisoformat('2024-06-22'),
        },
    ]
    func_result = read_sales_data(test_path)
    assert true_data == func_result


def test_total_sales_per_product():
    true_result = {
        'яблоки': 390,
        'груши': 176,
        'сливы': 705,
        'печенье': 368,
        'конфеты Рот-Фронт': 242,
    }

    test_path = 'tests/test_data.txt'
    data = read_sales_data(test_path)
    result = total_sales_per_product(data)
    assert true_result == result
