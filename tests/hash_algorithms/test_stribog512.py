import pytest

from hash_algorithms import stribog512


class TestStribog512:
    @pytest.mark.parametrize(
        "input_bytes, expected_hash",
        [
            (
                b"012345678901234567890123456789012345678901234567890123456789012",
                "1b54d01a4af5b9d5cc3d86d68d285462b19abc2475222f35c085122be4ba1ffa"
                "00ad30f8767b3a82384c6574f024c311e2a481332b08ef7f41797891c1646f48",
            ),
            (
                b"\xd1\xe5 \xe2\xe5\xf2\xf0\xe8, \xd1\xf2\xf0\xe8\xe1\xee\xe6\xe8 "
                b"\xe2\xed\xf3\xf6\xe8, \xe2\xe5\xfe\xf2\xfa \xf1 \xec\xee\xf0\xff "
                b"\xf1\xf2\xf0\xe5\xeb\xe0\xec\xe8 \xed\xe0 \xf5\xf0\xe0\xe1\xf0\xfb\xff "
                b"\xef\xeb\xfa\xea\xfb \xc8\xe3\xee\xf0\xe5\xe2\xfb",
                "1e88e62226bfca6f9994f1f2d51569e0daf8475a3b0fe61a5300eee46d961376"
                "035fe83549ada2b8620fcd7c496ce5b33f0cb9dddc2b6460143b03dabac9fb28",
            ),
        ],
    )
    def test_hashing(self, input_bytes: bytes, expected_hash: str):
        assert stribog512(input_bytes).hex() == expected_hash
