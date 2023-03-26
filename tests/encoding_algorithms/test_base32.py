import base64
from random import randbytes, randint

import pytest

from encoding_algorithms.base32 import base32_decode, base32_encode


class TestBase32:
    @pytest.mark.parametrize(  # Тестовые данные из RFC 4648
        "input_bytes, expected_bytes",
        [
            (b"", b""),
            (b"f", b"MY======"),
            (b"fo", b"MZXQ===="),
            (b"foo", b"MZXW6==="),
            (b"foob", b"MZXW6YQ="),
            (b"fooba", b"MZXW6YTB"),
            (b"foobar", b"MZXW6YTBOI======"),
        ],
    )
    def test_encode(self, input_bytes: bytes, expected_bytes: bytes):
        assert base32_encode(input_bytes) == expected_bytes

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "input_bytes", [(randbytes(randint(0, 20))) for i in range(15)]
    )
    def test_encode_random(self, input_bytes: bytes):
        assert base32_encode(input_bytes) == base64.b32encode(input_bytes)

    @pytest.mark.parametrize(
        "input_bytes, expected_bytes",
        [
            (b"", b""),
            (b"MY======", b"f"),
            (b"MZXQ====", b"fo"),
            (b"MZXW6===", b"foo"),
            (b"MZXW6YQ=", b"foob"),
            (b"MZXW6YTB", b"fooba"),
            (b"MZXW6YTBOI======", b"foobar"),
        ],
    )
    def test_decode(self, input_bytes: bytes, expected_bytes: bytes):
        assert base32_decode(input_bytes) == expected_bytes

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "input_bytes", [(randbytes(randint(0, 20))) for j in range(15)]
    )
    def test_reversibility_random(self, input_bytes: bytes):
        assert base32_decode(base32_encode(input_bytes)) == input_bytes
