from typing import Dict, TypeVar

Key = TypeVar("Key")
Value = TypeVar("Value")


def reverse_dict(input_dict: Dict[Key, Value]) -> Dict[Value, Key]:
    return {new_key: new_value for new_value, new_key in input_dict.items()}
