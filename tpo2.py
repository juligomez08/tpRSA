#SBOXES
S_BOXES = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
#FUNCIONES

#pasar hexa a binario
def transfABin(hexa):
    bina = bin(int(hexa, 16))[2:]
    # Calculamos cuántos ceros faltan para que sea múltiplo de 8
    faltan = (8 - len(bina) % 8) % 8
    bina = "0" * faltan + bina
    return bina

def transDecABin(numero):
    if numero < 0 or numero >= 2**64:
        raise ValueError("El número debe estar entre 0 y 2^63 - 1")
    binario = bin(numero)[2:]  # Convierte a binario y elimina el prefijo '0b'
    return binario.zfill(64) 

def transfAHexa(binario):
    # Asegurarse de que la longitud del binario sea múltiplo de 4
    faltan = (4 - len(binario) % 4) % 4
    binario = "0" * faltan + binario
    # Convertir binario a entero, luego a hexadecimal
    hexa = hex(int(binario, 2))[2:].upper()
    return hexa

def separarbloques(mhexa):
    bloquesm ={}
    i = 0
    while len(mhexa) !=0: 
        bloquesm[i] = mhexa[:16] #son los primeros 16
        mhexa = mhexa[16:] # le sacamos los primeros 16
        i = i+1
    print("antes de padding")
    bloquesm = padding(bloquesm, i-1)
    print(bloquesm)
    return bloquesm

def padding(diccionario, i):
     #aca tiene que ver si termina en 16 y sino rellena igual
    if len(diccionario[i])==16:
        diccionario[i]= "0808080808080808"
    else: 
        restante = int((16 - len(diccionario[i]))/2)
        agregado = "0"+str(restante)
        while restante !=0: 
            diccionario[i] = diccionario[i] + agregado 
            restante -=1
    return diccionario
        
def xor(a,b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result = result + "0"
        else:
            result = result + "1"
    return result

def expan(bina):
    E = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9,10,11,12,13,
        12,13,14,15,16,17,
        16,17,18,19,20,21,
        20,21,22,23,24,25,
        24,25,26,27,28,29,
        28,29,30,31,32,1
    ]
    return ''.join(bina[i - 1] for i in E)

def aplicar_sboxes(bloque_48bits):
    resultado = ""

    # Dividimos el bloque en 8 bloques de 6 bits
    for i in range(8):
        bloque6 = bloque_48bits[i * 6: (i + 1) * 6]
        
        fila = int(bloque6[0] + bloque6[5], 2)     # 1° y 6° bit
        columna = int(bloque6[1:5], 2)             # bits del medio

        valor_sbox = S_BOXES[i][fila][columna]     # valor decimal
        bits_sbox = f"{valor_sbox:04b}"            # a 4 bits binarios
        resultado += bits_sbox

    return resultado  # devuelve 32 bits

def feistel(leftant, rightant, k):
    P = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25
    ]
    right_exp = expan(rightant)
    B = xor(right_exp, k)
    B = aplicar_sboxes(B)
    B = permutar(B, P)
    return xor(leftant, B)  # Retorna el nuevo bloque derecho


def permutar(cadena, tabla):
    return ''.join(cadena[i - 1] for i in tabla)

def rotar_izq(bits, n):
    return bits[n:] + bits[:n]

def generar_subclaves(K):
    # Paso 1: convertir a binario
    K_bin = transfABin(K)  # tu función para pasar a binario
    # Paso 2: PC-1
    PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4] # como la tabla de arriba
    K_permutado = ''.join(K_bin[i - 1] for i in PC_1)

    C = K_permutado[:28]
    D = K_permutado[28:]

    SHIFT_ROUNDS = [1, 1, 2, 2, 2, 2, 2, 2,
                    1, 2, 2, 2, 2, 2, 2, 1]

    PC_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32]  # como la tabla de arriba

    subclaves = []

    for shift in SHIFT_ROUNDS:
        C = rotar_izq(C, shift)
        D = rotar_izq(D, shift)
        CD = C + D
        subclave = ''.join(CD[i - 1] for i in PC_2)
        subclaves.append(subclave)

    return subclaves

def des(x, K, cifrar):
    IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]
    IP_inv = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25]
    subclaves = generar_subclaves(K)
    #print("subclaves", subclaves)
    x = permutar (x,IP)
    left = x[:32]
    right = x[32:]
    if cifrar == True:
        for i in range(16):
            auxleft = left # pongo esto ya que desp modificamos left y no queremos perder el anterior
            left = right
            right = feistel(auxleft, left, subclaves[i])
    else: 
        for i in reversed(range(16)):
            auxleft = left # pongo esto ya que desp modificamos left y no queremos perder el anterior
            left = right
            right = feistel(auxleft, left, subclaves[i])
    x = permutar(right + left, IP_inv)
    return x

def cifrar(bloquesm, IV, K):
    bloquesx = {}
    IV = transfABin(IV)
    for i in bloquesm:
        bloquem = transfABin(bloquesm[i])
        if i == 0: 
            x = xor(bloquem, IV)#bloque de 64 bits 
        else:
           # bloques x en i-1
           x = xor(bloquem, bloquesx[i-1])
        bloquesx[i] = des(x,K, True)
    return bloquesx

def validarPadding(ultBloque):
    try:
        ultimovalorCad = ultBloque[-2:]
        ultimovalorInt = int(ultimovalorCad)
        nuevacadena = ""
        for i in range(ultimovalorInt):
            nuevacadena = nuevacadena + ultimovalorCad #0505050505
        if ultBloque[-(ultimovalorInt*2):] == nuevacadena: #verifica con los ultimos 10 (en el caso de 05)
            return ultBloque[:16-(ultimovalorInt*2)] # retorna los primeros 6
        else:
            return False
    except: #hacemos este try except por si los atacantes usan un padding que no sea numerico
        return False

def descifrar(mensajecifrado, IV,K):
    diccMensaje = {}
    IV = transfABin(IV)
    for i in mensajecifrado:
        m = des(mensajecifrado[i], K, False)
        if i== 0:
            m = xor(m,IV)
        else:
            m = xor(m,mensajecifrado[i-1]) #el atacante cambia el mensaje anterior con uno modificado 
            #validacion padding 
        diccMensaje[i] = transfAHexa(m)
    paddingvalidado = validarPadding(diccMensaje[i]) #capaz este padding lo podemos hacer antes y de guardarlo y que verifique antes para hacer lo del atacante
    if  paddingvalidado != False:
        diccMensaje[i] = paddingvalidado
        return diccMensaje
    else: 
        return False
        
def descifrarAtacante(moriginal, IV, K): #agrego IV y K porque el atancante lo manda al servidor y este ya lo deberia saber 
    minventado = ""
    for i in range(1,257):
        minventado = transDecABin(i)
        mprueba = des(moriginal, K, False)
        print("mprueba", mprueba)
        mprueba = xor(mprueba,minventado)
        print("xor",mprueba)
        mprueba = validarPadding(mprueba)
        if mprueba == False:
            print("padding Invalido")
        else:
            print(minventado)
            print("todo ok")





m = "3f5200ae7d152ae44a5f4a6b25a4d7f4c2b5d8e75d6d9c2b5a3b6f96ef5c2b2bfa2eb6c3daf0303030303"
bloques = separarbloques(m)
IV = "52a5b96f8d221b56"
K = "45DF9D2B3A635414"

mensajecifrado = cifrar(bloques, IV, K)
print("bloques" , bloques)
print("cifrado" , mensajecifrado)

mensajetrucho = {0:"1010110101010111011111010000111000011111100101010010100100111101", 1: "1010110101010111011111010000111000011111100101010010100100111101"}
mensajetruchodescifrado = descifrar(mensajetrucho, IV, K)
#mensajeOriginal = descifrar(mensajecifrado, IV, K) #si queremos probar el mensajeoriginal cambiar los parametros del if de abajo y viceversa
if mensajetruchodescifrado != False:
    for i in range(len(mensajetruchodescifrado)):
       print("bloque" , i , mensajetruchodescifrado[i])
else:
    print("Error Padding invalido")    
    

print("--------------------------------")

#print("mensaje cifrado", mensajecifrado)
#cifrapruebaatacante = "0000000000000000000000000000000000000000000000000000000000000001" 
#mensajeatacante = descifrarAtacante(mensajecifrado[5], IV, K)

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

# Paso 2: Cifrar
mensajecifrado = cifrar(bloques, IV, K)

# Paso 3: Elegir los bloques
c1 = mensajecifrado[0]
c2 = mensajecifrado[1]

# Paso 4: Ejecutar el ataque
m2_hex = ataque_padding_oracle(c1, c2, K)

print("\nBloque recuperado (m2) por ataque:", m2_hex)
print("Bloque original (m2 real):", bloques[1].upper())