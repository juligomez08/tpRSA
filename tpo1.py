

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


#def inversa_modular(e, phi):         ESTO ME LO HIZO CHAT DEBERIA SER LA COSA DE EUCLIDES EN VERSION BIEN HECHO EL MIO ESTA HARDCODEADO
    # Guardamos valores originales
    original_phi = phi
    x0, x1 = 0, 1

    while e > 1:
        # Calculamos cociente
        q = e // phi
        # Actualizamos e y phi
        e, phi = phi, e % phi
        # Actualizamos x
        x0, x1 = x1 - q * x0, x0

    # Aseguramos que el resultado sea positivo
    if x1 < 0:
        x1 += original_phi

    return x1



#PIDO VALORES FIJOS DE P Y Q Y ME FIJO QUE SEAN PRIMOS DISTINTOS (MAS ADELANTE LO HACEMOS DE OTRA FORMA)
p=int(input("p= "))
while es_primo(p)==False:
	print("ingrese un numero primo: ")
	p=int(input("p= "))
q=int(input("q= "))
while es_primo(q)==False or p==q:
	print("ingrese un numero primo diferente de p: ")
	q=int(input("q= "))

#CALCULO N
n = p * q
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
       

# CÁLCULO DE LA INVERSA MODULAR D, TAL QUE: (d * e) ≡ 1 mod phi
k = 1
while (1 + k * phi) % e != 0:  # Buscamos el menor k tal que (1 + k * phi) sea divisible por e
    k += 1
# Una vez que encontramos ese k, calculamos d
d = (1 + k * phi) // e  

print("El valor de d es:", d)

#d = inversa_modular(e, phi)    LLAMA AL CODIGO DE CHAT
#print("El valor de d es:", d)











