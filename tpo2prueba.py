def padding_oracle(bloque_anterior_bin: str, bloque_objetivo_bin: str, clave_hex: str) -> bool:
    """
    Oráculo que descifra el bloque objetivo usando el anterior y dice si el resultado tiene padding PKCS#7 válido.
    """
    # Descifrar c2 (bloque objetivo)
    descifrado = des(bloque_objetivo_bin, clave_hex, False)

    # Simular CBC: XOR con r (bloque anterior falso)
    mensaje_bin = xor(descifrado, bloque_anterior_bin)

    # Verificar padding PKCS#7 en binario
    ultimo_byte = mensaje_bin[-8:]
    padding_val = int(ultimo_byte, 2)

    if padding_val < 1 or padding_val > 8:
        return False

    padding_esperado = f"{padding_val:08b}" * padding_val
    return mensaje_bin[-padding_val * 8:] == padding_esperado

def ataque_padding_oracle_camila(c1_hex: str, c2_hex: str, clave_hex: str) -> str:
    """
    Ataque padding oracle sobre dos bloques de 8 bytes (16 hex cada uno).
    Devuelve el mensaje descifrado del segundo bloque (m2) en hexadecimal.
    """
    m2 = [None] * 8
    r_bin = list("0" * 64)  # r como lista binaria mutable de 64 bits

    # Recorremos desde el último byte al primero (posición 7 a 0)
    for pos in reversed(range(8)):
        padding_val = 8 - pos

        # Ajustamos los bytes ya descubiertos (de pos+1 en adelante)
        for j in range(pos + 1, 8):
            m2_byte = int(m2[j], 16)
            c1_byte = int(c1_hex[j * 2:(j + 1) * 2], 16)
            nuevo_byte = padding_val ^ m2_byte ^ c1_byte
            r_bin[j * 8:(j + 1) * 8] = list(f"{nuevo_byte:08b}")

        # Buscamos el byte correcto para esta posición
        for guess in range(256):
            r_bin[pos * 8:(pos + 1) * 8] = list(f"{guess:08b}")

            # Unimos el binario y nos aseguramos de que tenga exactamente 64 bits
            r_bin_str = "".join(r_bin)
            r_bin_str = r_bin_str.ljust(64, "0")[:64]  # Si quedó corto, completamos con ceros

            # Convertimos a HEX y nos aseguramos de tener exactamente 16 caracteres hexadecimales
            r_hex = "".join([f"{int(r_bin_str[i:i+8], 2):02X}" for i in range(0, 64, 8)])
            r_hex = r_hex.zfill(16)  # relleno con ceros a la izquierda si fuera necesario

            # Oráculo
            if padding_oracle(r_hex, c2_hex, clave_hex):
                d_byte = guess ^ padding_val
                c1_byte = int(c1_hex[pos * 2:(pos + 1) * 2], 16)
                m2_byte = d_byte ^ c1_byte
                m2[pos] = f"{m2_byte:02X}"
                break
        else:
            raise Exception(f"No se encontró padding válido para el byte {pos}")

    return "".join(m2)

def ataque_padding_oracle(c1: str, c2: str, clave: str) -> str:
    bloque_tamaño = 64  # bits
    m2 = [None] * 8
    r = list("0" * bloque_tamaño)

    for pos in reversed(range(8)):
        padding_val = 8 - pos

        # Ajustamos los bytes ya descubiertos
        for j in range(pos + 1, 8):
            m2_byte = int(m2[j], 16)
            c1_byte = int(c1[j * 8:(j + 1) * 8], 2)
            nuevo = padding_val ^ m2_byte ^ c1_byte
            r[j * 8:(j + 1) * 8] = list(f"{nuevo:08b}")

        # Buscamos el valor correcto del byte actual
        for guess in range(256):
            r[pos * 8:(pos + 1) * 8] = list(f"{guess:08b}")

            if padding_oracle("".join(r), c2, clave):
                d_byte = guess ^ padding_val
                c1_byte = int(c1[pos * 8:(pos + 1) * 8], 2)
                m2_byte = d_byte ^ c1_byte
                m2[pos] = f"{m2_byte:02X}"  # Guardamos en HEX
                break
        else:
            raise Exception(f"No se encontró padding válido en byte {pos}")

    return "".join(m2)

# Parámetros de prueba
m = "3f5200ae7d152ae4a2eb6c3daf0303030303"
IV = "52a5b96f8d221b56"
K = "45DF9D2B3A635414"

# Paso 1: Separar bloques y aplicar padding
bloques = separarbloques(m)
print("paso 1", bloques)

# Paso 2: Cifrar
mensajecifrado = cifrar(bloques, IV, K)
print("paso 2", mensajecifrado)
# Paso 3: Elegir los bloques
c1 = mensajecifrado[0]
c2 = mensajecifrado[1]

# Paso 4: Ejecutar el ataque
m2_hex = ataque_padding_oracle(c1, c2, K)
print("paso 4", m2_hex)
print("\nBloque recuperado (m2) por ataque:", m2_hex)
print("Bloque original (m2 real):", bloques[1].upper())