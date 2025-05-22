from typing import Dict
import binascii

# XOR simple entre dos bytearrays
def xor_bytes(b1: bytes, b2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(b1, b2))

# Función de "cifrado" y "descifrado" con XOR
def xor_encrypt_decrypt(block: bytes, key: bytes) -> bytes:
    return xor_bytes(block, key)

# Simula un oracle que dice si el padding es válido o no
def validar_padding(bloque: bytes) -> bool:
    if not bloque:
        return False
    pad = bloque[-1]
    if pad == 0 or pad > len(bloque):
        return False
    return bloque[-pad:] == bytes([pad] * pad)

# Oracle: simula el servidor que valida si el padding es correcto
def oracle(c1: bytes, c2: bytes, key: bytes) -> bool:
    decrypted = xor_encrypt_decrypt(c2, key)
    m2 = xor_bytes(decrypted, c1)
    return validar_padding(m2)

# Ataque Padding Oracle: recupera el bloque m2 a partir de c1 y c2
def padding_oracle_attack(c1_hex: str, c2_hex: str, key_hex: str) -> str:
    c1 = bytearray(binascii.unhexlify(c1_hex))
    c2 = bytearray(binascii.unhexlify(c2_hex))
    key = binascii.unhexlify(key_hex)
    block_size = 8
    recovered = bytearray(block_size)

    for i in range(1, block_size + 1):
        prefix = bytearray(block_size - i)
        padding_byte = i
        suffix = bytearray(
            (recovered[block_size - j] ^ padding_byte) for j in range(1, i)
        )

        for guess in range(256):
            attack_block = prefix + bytes([guess]) + suffix
            if oracle(attack_block, c2, key):
                recovered[block_size - i] = guess ^ padding_byte ^ c1[block_size - i]
                break

    return binascii.hexlify(recovered).decode()

# Simulación de uso
key_hex = "0102030405060708"  # clave de 8 bytes
mensaje_original = b"ATAQUE\x02\x02"  # 6 bytes + padding PKCS#7 para 8 bytes
key = binascii.unhexlify(key_hex)

# Cifrado CBC: c0 = IV, c1 = E(m1 ^ IV)
IV = b"\x00\x00\x00\x00\x00\x00\x00\x00"
m1 = xor_bytes(mensaje_original, IV)
c1 = xor_encrypt_decrypt(m1, key)

# Simular estructura de mensaje cifrado en dict
mensajecifrado: Dict[int, str] = {0: binascii.hexlify(c1).decode()}

# Ataque usando el oracle
mensaje_descifrado = padding_oracle_attack(
    binascii.hexlify(IV).decode(), mensajecifrado[0], key_hex
)
mensaje_descifrado_bytes = binascii.unhexlify(mensaje_descifrado)

mensaje_descifrado_bytes.decode(errors="replace")  # Mostrar el resultado final
