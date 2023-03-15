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
        {
            "department_id": 1,
            "department_name":"Beauty"
        }
    ]

    assert format_staff(example_staff, example_department) == [["Duncan", "Crawley", 1]]


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
        {
            "department_id": 2,
            "department_name":"Beauty"
        },
        {
            "department_id": 1,
            "department_name":"Footwear"
        }
    ]
    expected = [["Duncan", "Crawley", 2], ["Cat", "Hoang", 1]]

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
        {
            "department_id": 1,
            "department_name":"Beauty"
        }
    ]
    expected = [["Duncan", "Crawley", 1]]

    assert format_staff(example_staff, example_department) == expected


def test_ignores_incorrect_data():
    example_staff = [
        {
            "staff_id": 1,
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
        {
            'department_id': 1,
            'department_name':'Beauty'
        },
        {
            "department_id": 2
        }
    ]
    expected = []

    assert format_staff(example_staff, example_department) == expected