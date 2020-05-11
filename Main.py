#Juan Antonio Herrera Conde para TyMA. DNA Sequence.
#Ejecutamos los métodos creados.

from Metodos import *
import random

secuenciaAleatoria = ''.join([random.choice(Nucleotidos) for nucleotidos in range(100)])

secuencia = validarSecuencia(secuenciaAleatoria)

print("Secuencia = ", secuencia)

print ("La frecuencia de los nucleótidos es: ", contarFrecuenciaNuc(secuencia))

print("Complementaria: ", Complementaria(secuencia))

print(f"Secuencia ADN + Complementaria + Reversa Complementaria:\n5' {secuencia} 3'")
print(f"   {''.join(['|' for c in range (len(secuencia))])}")
print(f"3' {Complementaria(secuencia)} 5'")
print(f"5' {reversaComplementaria(secuencia)} 3'\n")

print("La secuencia de RNA resultante es: ", transcripcion(reversaComplementaria(secuencia)))

ARNmensajero = transcripcion(reversaComplementaria(secuencia))

secuenciaAminoacidos = traduccion(ARNmensajero, 0)

print(codones(ARNmensajero))

print("Secuencia de aminoácidos: ", secuenciaAminoacidos)

print ("Marcos de lectura: ")
for marcos in marcosLectura(ARNmensajero):
    print(marcos)
