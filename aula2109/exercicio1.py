import os
os.system("cls")

n = int(input("numero: "))

# forma "tradicional"
if n < 0:
    print("negativo")
else:
    if n > 0:
        print("positivo")
    else:
        print("nulo")

# forma python (elif)
if n < 0:
    print("negativo")
elif n > 0:
    print("positivo")
else:
    print("nulo")