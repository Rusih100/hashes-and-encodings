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
