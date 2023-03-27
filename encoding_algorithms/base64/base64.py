from encoding_algorithms.base64.tables import DECODING_TABLE, ENCODING_TABLE


def base64_encode(data_bytes: bytes) -> bytes:
    encoded_string: bytes = b""
    length_data = len(data_bytes)
    count_signs = 0

    for block_index in range(0, length_data, 3):
        bytes_count = min(3, length_data - block_index)

        block = int.from_bytes(
            data_bytes[block_index: block_index + 3], byteorder="big"
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


def base64_decode(data_bytes: bytes) -> bytes:
    decoded_string: bytes = b""
    count_signs = 0

    while data_bytes.rfind(b"=") != -1:
        data_bytes = data_bytes[:-1]
        count_signs += 1

    length_data = len(data_bytes)

    for block_index in range(0, length_data, 8):
        bytes_block: bytes = data_bytes[block_index: block_index + 8]
        length_bytes_block = len(bytes_block)

        block = 1
        bit_count = 0
        for i in range(length_bytes_block):
            byte_key: bytes = bytes_block[i: i + 1]
            block = (block << 6) | (DECODING_TABLE[byte_key])
            bit_count += 6

        if block_index + 8 > length_data:
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
