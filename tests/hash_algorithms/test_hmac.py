import hashlib
import hmac as lib_hmac
from random import randbytes, randint

import pytest

from hash_algorithms import hmac
from hash_algorithms.sha import sha256, sha512


class TestHMAC:
    @pytest.mark.parametrize(
        "key, message, expected_hash",
        [
            (
                b"\x0b" * 20,
                b"Hi There",
                "b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7",
            ),
            (
                b"Jefe",
                b"what do ya want for nothing?",
                "5bdcc146bf60754e6a042426089575c75a003f089d2739839dec58b964ec3843",
            ),
            (
                b"\xaa" * 20,
                b"\xdd" * 50,
                "773ea91e36800e46854db8ebd09181a72959098b3ef8c122d9635514ced565fe",
            ),
            (
                b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19",
                b"\xcd" * 50,
                "82558a389a443c0ea4cc819899f2083a85f0faa3e578f8077a2e3ff46729665b",
            ),
            (
                b"\xaa" * 131,
                b"Test Using Larger Than Block-Size Key - Hash Key First",
                "60e431591ee0b67f0d8a26aacbf5b77f8e0bc6213728c5140546040f0ee37f54",
            ),
            (
                b"\xaa" * 131,
                b"This is a test using a larger than block-size key and a larger than block-size data. The key needs "
                b"to be hashed before being used by the HMAC algorithm.",
                "9b09ffa71b942fcb27635fbcd5b0e944bfdc63644f0713938a7f51535c3a35e2",
            ),
        ],
    )
    def test_hashing_sha256(
        self, key: bytes, message: bytes, expected_hash: str
    ):
        assert hmac(key, message, 512, sha256).hex() == expected_hash

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "key, message",
        [
            (randbytes(randint(0, 200)), randbytes(randint(0, 200))) for _ in range(30)
        ]
    )
    def test_random_hashing_sha256(self, key: bytes, message: bytes):
        assert hmac(key, message, 512, sha256).hex() == lib_hmac.new(key, message, hashlib.sha256).hexdigest()

    @pytest.mark.parametrize(
        "key, message, expected_hash",
        [
            (
                b"\x0b" * 20,
                b"Hi There",
                "87aa7cdea5ef619d4ff0b4241a1d6cb02379f4e2ce4ec2787ad0b30545e17cde"
                "daa833b7d6b8a702038b274eaea3f4e4be9d914eeb61f1702e696c203a126854",
            ),
            (
                b"Jefe",
                b"what do ya want for nothing?",
                "164b7a7bfcf819e2e395fbe73b56e0a387bd64222e831fd610270cd7ea250554"
                "9758bf75c05a994a6d034f65f8f0e6fdcaeab1a34d4a6b4b636e070a38bce737",
            ),
            (
                b"\xaa" * 20,
                b"\xdd" * 50,
                "fa73b0089d56a284efb0f0756c890be9b1b5dbdd8ee81a3655f83e33b2279d39"
                "bf3e848279a722c806b485a47e67c807b946a337bee8942674278859e13292fb",
            ),
            (
                b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19",
                b"\xcd" * 50,
                "b0ba465637458c6990e5a8c5f61d4af7e576d97ff94b872de76f8050361ee3db"
                "a91ca5c11aa25eb4d679275cc5788063a5f19741120c4f2de2adebeb10a298dd",
            ),
            (
                b"\xaa" * 131,
                b"Test Using Larger Than Block-Size Key - Hash Key First",
                "80b24263c7c1a3ebb71493c1dd7be8b49b46d1f41b4aeec1121b013783f8f352"
                "6b56d037e05f2598bd0fd2215d6a1e5295e64f73f63f0aec8b915a985d786598",
            ),
            (
                b"\xaa" * 131,
                b"This is a test using a larger than block-size key and a larger than block-size data. The key needs "
                b"to be hashed before being used by the HMAC algorithm.",
                "e37b6a775dc87dbaa4dfa9f96e5e3ffddebd71f8867289865df5a32d20cdc944"
                "b6022cac3c4982b10d5eeb55c3e4de15134676fb6de0446065c97440fa8c6a58",
            ),
        ],
    )
    def test_hashing_sha512(
        self, key: bytes, message: bytes, expected_hash: str
    ):
        assert hmac(key, message, 1024, sha512).hex() == expected_hash

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "key, message",
        [
            (randbytes(randint(0, 200)), randbytes(randint(0, 200))) for _ in range(30)
        ]
    )
    def test_random_hashing_sha512(self, key: bytes, message: bytes):
        assert hmac(key, message, 1024, sha512).hex() == lib_hmac.new(key, message, hashlib.sha512).hexdigest()