import pytest

from hash_algorithms import stribog256


class TestStribog256:
    @pytest.mark.parametrize(
        "input_bytes, expected_hash",
        [
            (
                b"012345678901234567890123456789012345678901234567890123456789012",
                "9d151eefd8590b89daa6ba6cb74af9275dd051026bb149a452fd84e5e57b5500",
            ),
            (
                b"\xd1\xe5 \xe2\xe5\xf2\xf0\xe8, \xd1\xf2\xf0\xe8\xe1\xee\xe6\xe8 "
                b"\xe2\xed\xf3\xf6\xe8, \xe2\xe5\xfe\xf2\xfa \xf1 \xec\xee\xf0\xff "
                b"\xf1\xf2\xf0\xe5\xeb\xe0\xec\xe8 \xed\xe0 \xf5\xf0\xe0\xe1\xf0\xfb\xff "
                b"\xef\xeb\xfa\xea\xfb \xc8\xe3\xee\xf0\xe5\xe2\xfb",
                "9dd2fe4e90409e5da87f53976d7405b0c0cac628fc669a741d50063c557e8f50",
            ),
        ],
    )
    def test_hashing(self, input_bytes: bytes, expected_hash: str):
        assert stribog256(input_bytes).hex() == expected_hash
