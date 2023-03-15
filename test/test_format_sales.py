from src.format_sales import format_sales

def test_returns_list():
    assert format_sales([], [], []) == []


def test_returns_empty_list_when_no_sale_found():
    stock = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "amount_in_stock":5
        }
    ]
    staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department_id": 1
        }
    ]
    data = [
        {
            "sales_id": 1,
            "item_name": "Louboutin Flip Flops",
            "salesperson": "Cat Hoang",
            "price": 22.49,
            "quantity": 1,
            "created_at": "2023-01-03 10:34:56"
        }
    ]

    assert format_sales(stock, staff, data) == []


def test_returns_correct_list_for_one_sale():
    stock = [
        {
            "item_id": 2,
            "item_name": "Louboutin Flip Flops",
            "amount_in_stock":5
        }
    ]
    staff = [
        {
            "staff_id": 5,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department_id": 1
        }
    ]
    data = [
        {
            "sales_id": 1,
            "item_name": "Louboutin Flip Flops",
            "salesperson": "Duncan Crawley",
            "price": 22.49,
            "quantity": 10,
            "created_at": "2023-01-03 10:34:56"
        }
    ]

    assert format_sales(stock, staff, data) == [[2, 5, 22.49, 10, "2023-01-03 10:34:56"]]


def test_adds_multiple_distinct_sales():
    stock = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "amount_in_stock":5
        },
        {
            "item_id": 2,
            "item_name": "Eau de Fromage",
            "amount_in_stock": 10
        }
    ]
    staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department_id": 1
        },
        {
            "staff_id": 2,
            "first_name": "Cat",
            "last_name": "Hoang",
            "department_id": 2
        }
    ]
    data = [
        {
            "sales_id": 1,
            "item_name": "Louboutin Flip Flops",
            "salesperson": "Duncan Crawley",
            "price": 22.49,
            "quantity": 10,
            "created_at": "2023-01-03 10:34:56"
        },
        {
            "sales_id": 2,
            "item_name": "Louboutin Flip Flops",
            "salesperson": "Cat Hoang",
            "price": 22.49,
            "quantity": 2,
            "created_at": "2023-01-03 10:35:00"
        },
        {
            "sales_id": 3,
            "item_name": "Eau de Fromage",
            "salesperson": "Duncan Crawley",
            "price": 30.00,
            "quantity": 1,
            "created_at": "2023-11-20 09:04:10"
        }
    ]

    expected = [
        [1, 1, 22.49, 10, "2023-01-03 10:34:56"],
        [1, 2, 22.49, 2, "2023-01-03 10:35:00"],
        [2, 1, 30.00, 1, "2023-11-20 09:04:10"]
    ]

    assert format_sales(stock, staff, data) == expected


def test_ignores_incomplete_data():
    stock = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "amount_in_stock":5
        }
    ]
    staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department_id": 1
        }
    ]
    data = [
        {
            "sales_id": 1,
            "item_name": "Louboutin Flip Flops",
            "salesperson": "Duncan Crawley",
            "quantity": 10,
            "created_at": "2023-01-03 10:34:56"
        },
        {
            "sales_id": 2,
            "item_name": "Eau de Fromage",
            "salesperson": "Duncan Crawley",
            "price": 30.00,
            "created_at": "2023-11-20 09:04:10"
        }
    ]

    assert format_sales(stock, staff, data) == []