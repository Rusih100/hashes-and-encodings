from struct import pack

from hash_algorithms.stribog.consts import BLOCKSIZE
from hash_algorithms.stribog.operations import g
from hash_algorithms.stribog.utils import add512bit


def stribog256(bytes_string: bytes) -> bytes:
    hash_: bytes = BLOCKSIZE * b"\x01"
    sigma: bytes = BLOCKSIZE * b"\x00"
    n = 0
    data = bytes_string

    for i in range(0, len(data) // BLOCKSIZE * BLOCKSIZE, BLOCKSIZE):
        block = data[i : i + BLOCKSIZE]
        hash_ = g(n, hash_, block)
        sigma = add512bit(sigma, block)
        n += 512

    padding_block_size = len(data) * 8 - n
    data += b"\x01"
    padding_length = BLOCKSIZE - len(data) % BLOCKSIZE
    if padding_length != BLOCKSIZE:
        data += b"\x00" * padding_length

    hash_ = g(n, hash_, data[-BLOCKSIZE:])
    n += padding_block_size
    sigma = add512bit(sigma, data[-BLOCKSIZE:])
    hash_ = g(0, hash_, pack("<Q", n) + 56 * b"\x00")
    hash_ = g(0, hash_, sigma)

    return hash_[32:]
