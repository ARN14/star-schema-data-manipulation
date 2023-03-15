from src.format_features import format_features

def test_returns_list():
    assert format_features([]) == []


def test_returns_empty_list_when_no_features_found():
    example = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley"
        }
    ]

    assert format_features(example) == []


def test_extracts_single_feature():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer"],
            "department": "Footwear", "amount": 5
        }
    ]

    assert format_features(example) == [["Designer"]]


def test_extracts_multiple_features():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear", "amount": 5
        }
    ]

    assert format_features(example) == [["Designer"], ["Faux-Faux-Leather"]]


def test_extracts_features_from_multiple_dictionaries():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear", "amount": 5
        },
        {
            "item_id": 2,
            "item_name": "Eau de Fromage",
            "features": ["Fragrance"],
            "department": "Beauty",
            "amount": 10
        }
    ]

    assert format_features(example) == [["Designer"], ["Faux-Faux-Leather"], ["Fragrance"]]


def test_returned_features_dont_repeat():
    example = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer", "Faux-Faux-Leather"],
            "department": "Footwear", "amount": 5
        },
        {
            "item_id": 2,
            "item_name": "Eau de Fromage",
            "features": ["Fragrance", "Designer"],
            "department": "Beauty",
            "amount": 10
        }
    ]

    assert format_features(example) == [["Designer"], ["Faux-Faux-Leather"], ["Fragrance"]]