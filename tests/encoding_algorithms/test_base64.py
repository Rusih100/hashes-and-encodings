import base64
from random import randbytes, randint
from typing import Any

import pytest

from encoding_algorithms import base64_decode, base64_encode


class TestBase64:
    @pytest.mark.parametrize(  # Тестовые данные из RFC 4648
        "input_bytes, expected_bytes",
        [
            (b"", b""),
            (b"f", b"Zg=="),
            (b"fo", b"Zm8="),
            (b"foo", b"Zm9v"),
            (b"foob", b"Zm9vYg=="),
            (b"fooba", b"Zm9vYmE="),
            (b"foobar", b"Zm9vYmFy"),
        ],
    )
    def test_encode(self, input_bytes: bytes, expected_bytes: bytes):
        assert base64_encode(input_bytes) == expected_bytes

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "input_bytes", [(randbytes(randint(0, 30))) for _ in range(30)]
    )
    def test_encode_random(self, input_bytes: bytes):
        assert base64_encode(input_bytes) == base64.b64encode(input_bytes)

    @pytest.mark.parametrize(
        "input_bytes, expected_bytes",
        [
            (b"", b""),
            (b"Zg==", b"f"),
            (b"Zm8=", b"fo"),
            (b"Zm9v", b"foo"),
            (b"Zm9vYg==", b"foob"),
            (b"Zm9vYmE=", b"fooba"),
            (b"Zm9vYmFy", b"foobar"),
        ],
    )
    def test_decode(self, input_bytes: bytes, expected_bytes: bytes):
        assert base64_decode(input_bytes) == expected_bytes

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "input_bytes", [(randbytes(randint(0, 30))) for _ in range(30)]
    )
    def test_reversibility_random(self, input_bytes: bytes):
        assert base64_decode(base64_encode(input_bytes)) == input_bytes

    @pytest.mark.parametrize(
        "input_data", ["Hello", 123, list(), dict(), tuple(), None]
    )
    def test_incorrect_types_encode(self, input_data: Any):
        with pytest.raises(TypeError) as exp_info:
            base64_encode(input_data)

    @pytest.mark.parametrize(
        "input_data", ["Hello", 123, list(), dict(), tuple(), None]
    )
    def test_incorrect_types_decode(self, input_data: Any):
        with pytest.raises(TypeError) as exp_info:
            base64_decode(input_data)
