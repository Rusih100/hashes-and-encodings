import pytest

from core.utils import reverse_dict


@pytest.mark.parametrize(
    "input_dict, expected_dict",
    [
        (
            {0b00000: b"A", 0b00001: b"B", 0b00010: b"C", 0b00011: b"D"},
            {b"A": 0b00000, b"B": 0b00001, b"C": 0b00010, b"D": 0b00011},
        ),
        ({"A": 1}, {1: "A"}),
        ({}, {}),
    ],
)
def test_reverse_dict(input_dict: dict, expected_dict: dict):
    assert reverse_dict(input_dict) == expected_dict
