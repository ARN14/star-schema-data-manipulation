from src.format_departments import format_departments

def test_returns_list():
    assert format_departments([]) == []


def test_returns_empty_list_when_no_department_found():
    example = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley"
        },
        {
            "staff_id": 2,
            "first_name": "Cat",
            "last_name": "Hoang"
        }
    ]

    assert format_departments(example) == []


def test_extracts_department_from_single_dictionary():
    example = [
        {
            "staff_id": 1,
            "first_name": "Duncan",
            "last_name": "Crawley",
            "department": "Beauty"
        }
    ]
    expected = [["Beauty"]]

    assert format_departments(example) == expected


def test_extracts_department_from_multiple_dictionaries():
    example = [
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
    expected = [["Beauty"], ["Footwear"]]

    assert format_departments(example) == expected


def test_ignores_dictionaries_without_department():
    example = [
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
        },
        {
            "staff_id": 3,
            "first_name": "Vincents",
            "last_name": "Guille",
            "department": "Health"
        }
    ]
    expected = [["Beauty"], ["Health"]]

    assert format_departments(example) == expected


def test_ignores_repeat_departments():
    example = [
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
    expected = [["Beauty"]]

    assert format_departments(example) == expected