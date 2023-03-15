from src.format_stock_feature import format_stock_feature


def test_returns_list():
    assert format_stock_feature([], [], []) == []


def test_ignores_item_not_in_original_data():
    example_stock = [
        [
            1,
            "Louboutin Flip Flops",
            5
        ]
    ]

    assert format_stock_feature(example_stock, [], []) == []


def test_matches_stock_to_single_feature():
    example_stock = [
        [
            1,
            "Louboutin Flip Flops",
            5
        ]
    ]
    example_features = [
        [
            1,
            "Designer"
        ]
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
        [
            1,
            "Louboutin Flip Flops",
            5
        ], [
            2,
            'Eau de Fromage',
            10
        ]
    ]
    example_features = [
        [
            1,
            "Designer"
        ],
        [
            2,
            'Faux-Faux-Leather'
        ]
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
        [
            2,
            "Louboutin Flip Flops",
            5
        ], [
            1,
            'Eau de Fromage',
            10
        ]
    ]
    example_features = [
        [
            1,
            "Designer"
        ],
        [
            2,
            'Faux-Faux-Leather'
        ]
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
