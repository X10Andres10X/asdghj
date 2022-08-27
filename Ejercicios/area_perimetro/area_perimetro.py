# Programa No. 1: área y perímetro del círculo


print("---------------------------------")
print("---------- Área Perimetro -------")
print("---------------------------------")

# Input 

r = int(input("Digite el valor del radio: "))

# Procesing
import math
a = math.pi*r*r
p = 2*math.pi*r

# Output
print("---------- Resultados ----------")
print("Área: " + str(a))
print("Perímetro: " + str(p))