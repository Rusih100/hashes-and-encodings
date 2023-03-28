from encoding_algorithms.base32.tables import DECODING_TABLE, ENCODING_TABLE


def base32_encode(bytes_string: bytes) -> bytes:
    if not isinstance(bytes_string, bytes):
        raise TypeError(f"bytes string should be {bytes}, not be {type(bytes_string)}")

    encoded_string: bytes = b""
    length_bytes_string = len(bytes_string)
    count_signs = 0

    for block_index in range(0, length_bytes_string, 5):
        bytes_count = min(5, length_bytes_string - block_index)

        block = int.from_bytes(
            bytes_string[block_index: block_index + 5], byteorder="big"
        )

        bit_count = bytes_count * 8
        while bit_count > 0:
            if bit_count >= 5:
                int_key = (block >> (bit_count - 5)) & 0b00011111
            else:
                int_key = (block & (0b00011111 >> (5 - bit_count))) << (
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

            encoded_string += ENCODING_TABLE[int_key]
            bit_count -= 5

    encoded_string += b"=" * count_signs

    return encoded_string


def base32_decode(bytes_string: bytes) -> bytes:
    if not isinstance(bytes_string, bytes):
        raise TypeError(f"bytes string should be {bytes}, not be {type(bytes_string)}")

    decoded_string: bytes = b""
    count_signs = 0

    while bytes_string.rfind(b"=") != -1:
        bytes_string = bytes_string[:-1]
        count_signs += 1

    length_bytes_string = len(bytes_string)

    for block_index in range(0, length_bytes_string, 8):
        bytes_block: bytes = bytes_string[block_index: block_index + 8]
        length_bytes_block = len(bytes_block)

        block = 1
        bit_count = 0
        for i in range(length_bytes_block):
            byte_key: bytes = bytes_block[i : i + 1]
            block = (block << 5) | (DECODING_TABLE[byte_key])
            bit_count += 5

        if block_index + 8 > length_bytes_string:
            match count_signs:
                case 6:
                    block = block >> 2
                    bit_count -= 2
                case 4:
                    block = block >> 4
                    bit_count -= 4
                case 3:
                    block = block >> 1
                    bit_count -= 1
                case 1:
                    block = block >> 3
                    bit_count -= 3

        temp_byte_string: bytes = b""

        while bit_count > 0:
            byte = block & 0b11111111
            temp_byte_string = bytes([byte]) + temp_byte_string
            block = block >> 8
            bit_count -= 8

        decoded_string += temp_byte_string

    return decoded_string
