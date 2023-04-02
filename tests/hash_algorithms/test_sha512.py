import hashlib
from random import randbytes, randint

import pytest

from hash_algorithms.sha import sha512


class TestSHA512:
    @pytest.mark.parametrize(
        "input_bytes, expected_hash",
        [
            (
                b"",
                "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce"
                "47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
            ),
            (
                b"abc",
                "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a"
                "2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f",
            ),
            (
                b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq",
                "204a8fc6dda82f0a0ced7beb8e08a41657c16ef468b228a8279be331a703c335"
                "96fd15c13b1b07f9aa1d3bea57789ca031ad85c7a71dd70354ec631238ca3445",
            ),
            (
                b"abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmno"
                b"pqrsmnopqrstnopqrstu",
                "8e959b75dae313da8cf4f72814fc143f8f7779c6eb9f7fa17299aeadb6889018"
                "501d289e4900f7e4331b99dec4b5433ac7d329eeb6dd26545e96e55b874be909",
            ),
        ],
    )
    def test_hashing(self, input_bytes: bytes, expected_hash: str):
        assert sha512(input_bytes).hex() == expected_hash

    @pytest.mark.parametrize(  # Тесты на случайных байтах
        "input_bytes", [(randbytes(randint(0, 100))) for j in range(30)]
    )
    def test_random_hashing(self, input_bytes: bytes):
        assert (
            sha512(input_bytes).hex() == hashlib.sha512(input_bytes).hexdigest()
        )
