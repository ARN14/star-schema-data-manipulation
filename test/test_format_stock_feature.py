from src.format_stock_feature import format_stock_feature


def test_returns_list():
    assert format_stock_feature([], [], []) == []


def test_ignores_item_not_in_original_data():
    example_stock = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "amount_in_stock": 5
        }
    ]

    assert format_stock_feature(example_stock, [], []) == []


def test_matches_stock_to_single_feature():
    example_stock = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "amount_in_stock": 5
        }
    ]
    example_features = [
        {
            "feature_id": 1,
            "feature_name": "Designer"
        }
    ]
    original_data = [
        {
            "item_id": 1,
            "item_name": "Louboutin Flip Flops",
            "features": ["Designer"],
            "department": "Footwear",
            "amount": 5
        }
    ]

    expected = [[1, 1]]
    assert format_stock_feature(example_stock,
                                example_features,
                                original_data) == expected


def test_works_for_larger_data():
    example_stock = [
        {
            'item_id': 1,
            'item_name': 'Louboutin Flip Flops',
            'amount_in_stock': 5
        }, {
            'item_id': 2,
            'item_name': 'Eau de Fromage',
            'amount_in_stock': 10
        }
    ]
    example_features = [
        {
            'feature_id': 1,
            'feature_name': 'Designer'
        },
        {
            'feature_id': 2,
            'feature_name': 'Faux-Faux-Leather'
        }
    ]
    original_data = [
        {
            'item_id': 1,
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount': 5
        },
        {
            'item_id': 2,
            'item_name': 'Eau de Fromage',
            'features': ['Designer'],
            'department': 'Beauty',
            'amount': 10
        }
    ]

    expected = [[1, 1], [1, 2], [2, 1]]

    assert format_stock_feature(example_stock,
                                example_features,
                                original_data) == expected


def test_works_when_ids_are_unordered():
    example_stock = [
        {
            'item_id': 2,
            'item_name': 'Louboutin Flip Flops',
            'amount_in_stock': 5
        }, {
            'item_id': 1,
            'item_name': 'Eau de Fromage',
            'amount_in_stock': 10
        }
    ]
    example_features = [
        {
            'feature_id': 1,
            'feature_name': 'Designer'
        },
        {
            'feature_id': 2,
            'feature_name': 'Faux-Faux-Leather'
        }
    ]
    original_data = [
        {
            'item_id': 1,
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount': 5
        },
        {
            'item_id': 2,
            'item_name': 'Eau de Fromage',
            'features': ['Designer'],
            'department': 'Beauty',
            'amount': 10
        }
    ]

    expected = [[2, 1], [2, 2], [1, 1]]

    assert format_stock_feature(example_stock,
                                example_features,
                                original_data) == expected
