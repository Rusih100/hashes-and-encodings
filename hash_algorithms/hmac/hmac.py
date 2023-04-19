from typing import Callable


def hmac(
    secret_key_bytes: bytes,
    message_bytes: bytes,
    block_size: int,
    hash_function: Callable[[bytes], bytes],
) -> bytes:
    block_size_for_bytes = block_size // 8

    if len(secret_key_bytes) > block_size_for_bytes:
        secret_key_bytes = hash_function(secret_key_bytes)

    while len(secret_key_bytes) < block_size_for_bytes:
        secret_key_bytes += b"\x00"

    secret_key = int.from_bytes(secret_key_bytes, byteorder="big")

    outer_padding_bytes = b"\x5c" * block_size_for_bytes
    inner_padding_bytes = b"\x36" * block_size_for_bytes

    outer_padding = int.from_bytes(outer_padding_bytes, byteorder="big")
    inner_padding = int.from_bytes(inner_padding_bytes, byteorder="big")

    first_xor = secret_key ^ outer_padding
    second_xor = secret_key ^ inner_padding

    first_xor_bytes = first_xor.to_bytes(block_size_for_bytes, byteorder="big")
    second_xor_bytes = second_xor.to_bytes(
        block_size_for_bytes, byteorder="big"
    )

    return hash_function(
        first_xor_bytes + hash_function(second_xor_bytes + message_bytes)
    )
