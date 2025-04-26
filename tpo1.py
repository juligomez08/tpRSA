#FUNCIONES
def es_primo(n):                             
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mcd(e, phi):
    while phi % e != 0:  #mientras no sea divisible
        resto = phi % e  #calculamos el resto
        phi = e          #bajo un nivel
        e = resto        # lo que me resto antes ahora es el nuevo divbisor
    return e          # cuando lleogo a 0 ya devuelve el mcd


# 1. Algoritmo extendido de Euclides
def extendido_mcd(a,b):
    if b == 0:
        return a, 1, 0
    else:
        mcd, x1, y1 = extendido_mcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return mcd , x, y

# 2. Inverso modular
def inverso_modular (e , phi):
    mcd, x, y = extendido_mcd(e, phi)
    if mcd != 1:
        raise Exception ("No existe inverso modular")
    else:
        return x % phi


#EXPONENCIACION RAPIDA
def fast_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

#TEOREMA DE RESTOS CHINOS
def chinos(m_cifrado, p,q, d):
    md = m_cifrado**d
    mp = md % p
    mq = md % q
    q_inv = inverso_modular(q,p)
    p_inv = inverso_modular(p,q)
    mensaje = ((mp * q * q_inv) + (mq * p * p_inv)) % n
    return mensaje


#PROGRAMA PRINCIPAL
#MENSAJE A CIFRAR
mensaje= int(input("Ingrese el mensaje a encriptar:" ))
n=0
#PIDO VALORES FIJOS DE P Y Q Y ME FIJO QUE SEAN PRIMOS DISTINTOS (MAS ADELANTE LO HACEMOS DE OTRA FORMA)
while mensaje >= n-1:
    p=int(input("p= "))
    while es_primo(p)==False:
        print("ingrese un numero primo: ")
        p=int(input("p= "))
    q=int(input("q= "))
    while es_primo(q)==False or p==q:
        print("ingrese un numero primo diferente de p: ")
        q=int(input("q= "))
    n = p * q
    if mensaje >=n-1:
        print("elija números primos más grandes")

print("el valor de n es: ", n)

#CALCULO PHI
phi = (p-1) * (q-1)
print("el valor de phi es: ", phi)

# CALCULO POSIBLES VALORES DE E (que sean coprimos con phi)
e = 2
valores_de_e = []
while e < phi:
    if mcd(e, phi) == 1:
        valores_de_e.append(e)
    e += 1
print("posibles valores de e: ", valores_de_e)

while mcd(e, phi)!=1:
     print("elija un valor de la lista: ")
     e = int(input("e= "))

#CALCULAR D
d = inverso_modular(e,phi)

# Mostrar claves
print("Clave pública (n, e):", (n, e))
print("Clave privada d:", d)

x = fast_exp(mensaje, e, n)  # mensaje cifrado
print("Mensaje cifrado:", x)

# 6. Descifrado
m_descifrado1 = fast_exp(x, d, n)
m_descifrado = chinos(x,p,q,d)
print("Mensaje descifrado ER:", m_descifrado)
print("Mensaje descifrado TCR:", m_descifrado1)










