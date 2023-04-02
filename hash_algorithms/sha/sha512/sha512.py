from typing import List

from hash_algorithms.sha.message_preprocess import message_preprocess
from hash_algorithms.sha.operations import choose, majority
from hash_algorithms.sha.sha512.consts import INIT_HASH_CONSTS, K_CONSTS, MOD
from hash_algorithms.sha.sha512.operations import (
    big_sigma0,
    big_sigma1,
    sigma0,
    sigma1,
)


def sha512(bytes_string: bytes) -> bytes:
    blocks: List[bytes] = message_preprocess(bytes_string, block_size=1024)

    h0, h1, h2, h3, h4, h5, h6, h7 = INIT_HASH_CONSTS

    for block in blocks:
        message_schedule: List[int] = []

        for t in range(80):
            if t <= 15:
                message_schedule.append(
                    int.from_bytes(
                        block[t * 8 : (t + 1) * 8],
                        byteorder="big",
                    )
                )
            else:
                message_schedule.append(
                    (
                        sigma1(message_schedule[t - 2])
                        + message_schedule[t - 7]
                        + sigma0(message_schedule[t - 15])
                        + message_schedule[t - 16]
                    )
                    % MOD
                )

        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        for t in range(80):
            term1 = (
                h
                + big_sigma1(e)
                + choose(e, f, g)
                + K_CONSTS[t]
                + message_schedule[t]
            ) % MOD
            term2 = (big_sigma0(a) + majority(a, b, c)) % MOD

            h = g
            g = f
            f = e
            e = (d + term1) % MOD
            d = c
            c = b
            b = a
            a = (term1 + term2) % MOD

        h0 = (h0 + a) % MOD
        h1 = (h1 + b) % MOD
        h2 = (h2 + c) % MOD
        h3 = (h3 + d) % MOD
        h4 = (h4 + e) % MOD
        h5 = (h5 + f) % MOD
        h6 = (h6 + g) % MOD
        h7 = (h7 + h) % MOD

    result = b""
    for h in (h0, h1, h2, h3, h4, h5, h6, h7):
        result += h.to_bytes(8, "big")

    return result
