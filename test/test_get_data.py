from src.get_data import get_staff_data, get_sales_data, get_items_data


def test_sales_table_has_correct_length():
    assert len(get_sales_data()) == 22


def test_sales_table_has_correct_keys():
    for item in get_sales_data():
        assert isinstance(item, dict)
        assert "sales_id" in item
        assert "item_name" in item
        assert "salesperson" in item
        assert "price" in item
        assert "quantity" in item
        assert "created_at" in item


def test_sales_table_has_correct_values():
    sales_data = get_sales_data()

    assert sales_data[0]["sales_id"] == 1
    assert sales_data[1]["item_name"] == "Eau de Fromage"
    assert sales_data[2]["salesperson"] == "Sutherlan Housbey"
    assert sales_data[3]["quantity"] == 19


def test_sales_table_has_correctly_formatted_price():
    sales_data = get_sales_data()

    for item in sales_data:
        assert type(item["price"]) == float

    assert sales_data[1]["price"] == 29.95
    assert sales_data[5]["price"] == 94.16


def test_sales_table_has_correctly_formatted_date():
    sales_data = get_sales_data()

    for item in sales_data:
        assert type(item["created_at"]) == str

    assert sales_data[6]["created_at"] == "2023-01-27 14:10:36"
    assert sales_data[7]["created_at"] == "2023-01-08 04:05:06"


def test_items_table_has_correct_length():
    assert len(get_items_data()) == 25


def test_items_table_has_correct_keys_and_values():
    items_data = get_items_data()

    assert items_data[0]["item_id"] == 1
    assert items_data[1]["item_name"] == "Eau de Fromage"
    assert items_data[3]["features"] == ["Roller-Application", "Multipack"]
    assert items_data[4]["department"] == "Footwear"
    assert items_data[5]["amount"] == 75


def test_staff_table_has_correct_length():
    assert len(get_staff_data()) == 17


def test_staff_table_has_correct_keys_and_values():
    items_data = get_staff_data()

    assert items_data[0]["staff_id"] == 1
    assert items_data[1]["first_name"] == "Cat"
    assert items_data[2]["last_name"] == "Guille"
    assert items_data[3]["department"] == "Kids"
