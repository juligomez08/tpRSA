

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
       

#CALCULO D CON LA INVERSA MULTIPLICADORA
k = 1
r = (1 +(k) * (phi))%(e)
while r!=0:
     k=k+1
     r=(1+(k)*(phi))%(e)
d=int((1+(k)*(phi))/(e))

print("el valor de d es: ", d)







