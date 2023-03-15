from src.format_stock import format_stock


def test_returns_list():
    assert format_stock([]) == []


def test_returns_empty_list_when_no_item_found():
    example = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department": "Beauty"
        }
    ]

    assert format_stock(example) == []


def test_extracts_item_and_price_from_single_dictionary():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear",
            "amount": 5
        }
    ]

    assert format_stock(example) == [["Louboutin Flip Flops", 5]]


def test_extracts_multiple_items():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear",
            "amount": 5
        },
        {
            "item_id": 2,
            "item_name": "Eau de Fromage",
            "features": ["Fragrance", "Designer"],
            "department": "Beauty",
            "amount": 10
        }
    ]

    expected = [["Louboutin Flip Flops", 5], ["Eau de Fromage", 10]]
    assert format_stock(example) == expected


def test_ignores_empty_strings():
    example = [
        {
            "item_id": 1,
            "item_name": "",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear",
            "amount": 5
        }
    ]

    assert format_stock(example) == []


def test_adds_items_with_0_amount():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear",
            "amount": 0
        }
    ]

    assert format_stock(example) == [["Louboutin Flip Flops", 0]]
