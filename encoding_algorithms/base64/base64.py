from encoding_algorithms.base64.tables import DECODING_TABLE, ENCODING_TABLE


def base64_encode(bytes_string: bytes) -> bytes:
    if not isinstance(bytes_string, bytes):
        raise TypeError(
            f"bytes string should be {bytes}, not be {type(bytes_string)}"
        )

    encoded_string: bytes = b""
    length_bytes_string = len(bytes_string)
    count_signs = 0

    for block_index in range(0, length_bytes_string, 3):
        bytes_count = min(3, length_bytes_string - block_index)

        block = int.from_bytes(
            bytes_string[block_index : block_index + 3], byteorder="big"
        )

        bit_count = bytes_count * 8
        while bit_count > 0:
            if bit_count >= 6:
                int_key = (block >> (bit_count - 6)) & 0b00111111
            else:
                int_key = (block & (0b00111111 >> (6 - bit_count))) << (
                    6 - bit_count
                )
                match bit_count:
                    case 4:
                        count_signs = 1
                    case 2:
                        count_signs = 2

            encoded_string += ENCODING_TABLE[int_key]
            bit_count -= 6

    encoded_string += b"=" * count_signs

    return encoded_string


def base64_decode(bytes_string: bytes) -> bytes:
    if not isinstance(bytes_string, bytes):
        raise TypeError(
            f"bytes string should be {bytes}, not be {type(bytes_string)}"
        )

    decoded_string: bytes = b""
    count_signs = 0

    while bytes_string.rfind(b"=") != -1:
        bytes_string = bytes_string[:-1]
        count_signs += 1

    length_bytes_string = len(bytes_string)

    for block_index in range(0, length_bytes_string, 8):
        bytes_block: bytes = bytes_string[block_index : block_index + 8]
        length_bytes_block = len(bytes_block)

        block = 1
        bit_count = 0
        for i in range(length_bytes_block):
            byte_key: bytes = bytes_block[i : i + 1]
            block = (block << 6) | (DECODING_TABLE[byte_key])
            bit_count += 6

        if block_index + 8 > length_bytes_string:
            match count_signs:
                case 1:
                    block = block >> 2
                    bit_count -= 2
                case 2:
                    block = block >> 4
                    bit_count -= 4

        temp_byte_string: bytes = b""

        while bit_count > 0:
            byte = block & 0b11111111
            temp_byte_string = bytes([byte]) + temp_byte_string
            block = block >> 8
            bit_count -= 8

        decoded_string += temp_byte_string

    return decoded_string
