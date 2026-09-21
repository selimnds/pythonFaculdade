# 2 dada a nota, determine se é válida ou inválida
import os
os.system("cls")

n = float(input("nota: "))

if n >= 0 and n <= 10:
    print("nota válida")
else:
    print ("nota inválida")