from core.utils.sizeof import sizeof_int
from encoding_algorithms.base32.tables import DECODING_TABLE, ENCODING_TABLE


def base32_encode(data_bytes: bytes) -> bytes:
    encoded_string: bytes = b""
    length_data = len(data_bytes)
    count_signs = 0

    for block_index in range(0, length_data, 5):
        bytes_count = min(5, length_data - block_index)

        block = int.from_bytes(
            data_bytes[block_index : block_index + 5], byteorder="big"
        )

        bit_count = bytes_count * 8
        while bit_count > 0:
            if bit_count >= 5:
                key = (block >> (bit_count - 5)) & 0b00011111
            else:
                key = (block & (0b00011111 >> (5 - bit_count))) << (
                    5 - bit_count
                )
                match bit_count:
                    case 3:
                        count_signs = 6
                    case 1:
                        count_signs = 4
                    case 4:
                        count_signs = 3
                    case 2:
                        count_signs = 1

            encoded_string += ENCODING_TABLE[key]
            bit_count -= 5

    encoded_string += b"=" * count_signs

    return encoded_string


def base32_decode(data_bytes: bytes) -> bytes:
    decoded_string: bytes = b""
    count_signs = 0

    while data_bytes.rfind(b"=") != -1:
        data_bytes = data_bytes[:-1]
        count_signs += 1

    length_data = len(data_bytes)

    for block_index in range(0, length_data, 8):
        bytes_block = data_bytes[block_index : block_index + 8]
        length_bytes_block = len(bytes_block)

        block = 0
        for i in range(length_bytes_block):
            key = bytes_block[i : i + 1]
            block = (block << 5) | (DECODING_TABLE[key])

        if block.bit_length() < 39:
            match count_signs:
                case 6:
                    block = block >> 2
                case 4:
                    block = block >> 4
                case 3:
                    block = block >> 1
                case 1:
                    block = block >> 3

        decoded_string += block.to_bytes(
            length=sizeof_int(block), byteorder="big"
        )

    return decoded_string
