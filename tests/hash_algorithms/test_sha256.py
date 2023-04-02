import hashlib
from random import randbytes, randint

import pytest

from hash_algorithms.sha import sha256


class TestSHA256:
    @pytest.mark.parametrize(
        "input_bytes, expected_hash",
        [
            (
                b"",
                "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            ),
            (
                b"abc",
                "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            ),
            (
                b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq",
                "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1",
            ),
            (
                b"abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmno"
                b"pqrsmnopqrstnopqrstu",
                "cf5b16a778af8380036ce59e7b0492370b249b11e8f07a51afac45037afee9d1",
            ),
        ],
    )
    def test_hashing(self, input_bytes: bytes, expected_hash: str):
        assert sha256(input_bytes).hex() == expected_hash

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "input_bytes", [(randbytes(randint(0, 100))) for j in range(30)]
    )
    def test_random_hashing(self, input_bytes: bytes):
        assert (
            sha256(input_bytes).hex() == hashlib.sha256(input_bytes).hexdigest()
        )
