import os 
os.system("cls")

valor = input("Valor: ")
crrt = True

match valor:
    case '1' | '3':
        print("Digitou impar")
        valor = int(valor)
    case '2' | '4':
        print("Digitou par")
        valor = int(valor)
    case _:
        print("Digite um valor valido")
        crrt = False

if crrt:
    dobro = valor * 2 
    print(dobro)