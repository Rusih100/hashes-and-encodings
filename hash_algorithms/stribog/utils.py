from codecs import getdecoder, getencoder

_hexdecoder = getdecoder("hex")
_hexencoder = getencoder("hex")


def hexdec(data):
    """Decode hexadecimal"""
    return _hexdecoder(data)[0]


def hexenc(data):
    """Encode hexadecimal"""
    return _hexencoder(data)[0].decode("ascii")


def add512bit(a, b):
    """Add two 512 integers"""
    a = bytearray(a)
    b = bytearray(b)
    cb = 0
    res = bytearray(64)
    for i in range(64):
        cb = a[i] + b[i] + (cb >> 8)
        res[i] = cb & 0xFF
    return res
