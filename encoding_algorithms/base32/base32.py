from encoding_algorithms.base32.tables import ENCODING_TABLE


def base32_encode(data_bytes: bytes) -> bytes:
    encoded_string: bytes = b""
    data_length = len(data_bytes)
    count_signs = 0

    for block_index in range(0, data_length, 5):
        bytes_count = min(5, data_length - block_index)
        print(bytes_count)

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


def base32_decode(base64_bytes: bytes) -> bytes:
    pass
