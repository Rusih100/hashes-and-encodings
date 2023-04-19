from struct import pack, unpack

from hash_algorithms.stribog.consts import (
    A_CONSTS,
    BLOCKSIZE,
    C_CONSTS,
    PI_CONSTS,
    TAU_CONSTS,
)


def byte_xor(a: bytes, b: bytes) -> bytes:
    min_len = min(len(a), len(b))
    a, b, xor = bytearray(a), bytearray(b), bytearray(min_len)
    for i in range(min_len):
        xor[i] = a[i] ^ b[i]
    return bytes(xor)


def g(n: int, hash_: bytes, message: bytes) -> bytes:
    res = E(LPS(byte_xor(hash_[:8], pack("<Q", n)) + hash_[8:]), message)
    return byte_xor(byte_xor(res, hash_), message)


def E(k: bytes, message: bytes) -> bytes:
    for i in range(12):
        message = LPS(byte_xor(k, message))
        k = LPS(byte_xor(k, C_CONSTS[i]))
    return byte_xor(k, message)


def LPS(data: bytes) -> bytes:
    """
    Основная операция функции сжатия обозначается как LPS и состоит из
    трёх преобразований: подстановки на байтах, транспонирования матрицы
    байт и умножения 64-битных векторов на матрицу 64 × 64 в GF(2)
    """
    return L(PS(bytearray(data)))


def PS(data: bytes) -> bytes:
    """
    P — переупорядочивание байт.  Байты аргумента меняются местами по
    определённому в стандарте порядку

    S — нелинейная биекция. 512 бит аргумента рассматриваются как
    массив из шестидесяти четырёх байт, каждый из которых заменяется
    по заданной стандартом таблице подстановки
    """
    res = bytearray(BLOCKSIZE)
    for i in range(BLOCKSIZE):
        res[TAU_CONSTS[i]] = PI_CONSTS[data[i]]
    return res


def L(data: bytes) -> bytes:
    """
    L — линейное преобразование.  Аргумент рассматривается как 8
    64-битных векторов, каждый из которых заменяется результатом
    умножения на определённую стандартом матрицу 64 × 64 над GF(2)
    """
    res = []
    for i in range(8):
        val = unpack("<Q", data[i * 8 : i * 8 + 8])[0]
        res64 = 0
        for j in range(BLOCKSIZE):
            if val & 0x8000000000000000:
                res64 ^= A_CONSTS[j]
            val <<= 1
        res.append(pack("<Q", res64))
    return b"".join(res)
