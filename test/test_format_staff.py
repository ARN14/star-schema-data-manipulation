from src.format_staff import format_staff


def test_returns_list():
    assert format_staff([], []) == []


def test_matches_correct_department():
    example_staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department": "Beauty"
        }
    ]
    example_department = [
        [
            1,
            "Beauty"
        ]
    ]

    expected = [["Duncan", "Crawley", 1]]

    assert format_staff(example_staff, example_department) == expected


def test_searches_multiple_departments():
    example_staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department": "Beauty"
        },
        {
            "staff_id": 2,
            "first_name": "Cat",
            "last_name": "Hoang",
            "department": "Footwear"
        }
    ]
    example_department = [
        [
            2,
            "Beauty"
        ],
        [
            1,
            "Footwear"
        ]
    ]
    expected = [["Duncan", "Crawley", 2], ["Cat", "Hoang", 1]]

    assert format_staff(example_staff, example_department) == expected


def test_matches_multiple_staff_to_one_department():
    example_staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department": "Beauty"
        },
        {
            "staff_id": 2,
            "first_name": "Cat",
            "last_name": "Hoang",
            "department": "Beauty"
        }
    ]
    example_department = [
        [
            5,
            "Beauty"
        ]
    ]
    expected = [["Duncan", "Crawley", 5], ["Cat", "Hoang", 5]]

    assert format_staff(example_staff, example_department) == expected


def test_ignores_staff_when_department_not_found():
    example_staff = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department": "Beauty"
        },
        {
            "staff_id": 2,
            "first_name": "Cat",
            "last_name": "Hoang",
            "department": "Footwear"
        }
    ]
    example_department = [
        [
            1,
            "Beauty"
        ]
    ]
    expected = [["Duncan", "Crawley", 1]]

    assert format_staff(example_staff, example_department) == expected
