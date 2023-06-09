from typing import Dict

from core.utils import reverse_dict

ENCODING_TABLE: Dict[int, bytes] = {
    0b00000: b"A",
    0b00001: b"B",
    0b00010: b"C",
    0b00011: b"D",
    0b00100: b"E",
    0b00101: b"F",
    0b00110: b"G",
    0b00111: b"H",
    0b01000: b"I",
    0b01001: b"J",
    0b01010: b"K",
    0b01011: b"L",
    0b01100: b"M",
    0b01101: b"N",
    0b01110: b"O",
    0b01111: b"P",
    0b10000: b"Q",
    0b10001: b"R",
    0b10010: b"S",
    0b10011: b"T",
    0b10100: b"U",
    0b10101: b"V",
    0b10110: b"W",
    0b10111: b"X",
    0b11000: b"Y",
    0b11001: b"Z",
    0b11010: b"2",
    0b11011: b"3",
    0b11100: b"4",
    0b11101: b"5",
    0b11110: b"6",
    0b11111: b"7",
}

DECODING_TABLE: Dict[bytes, int] = reverse_dict(ENCODING_TABLE)
