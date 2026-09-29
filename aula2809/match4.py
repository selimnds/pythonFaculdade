import os 
os.system("cls")

print("""
1 - Cadastrar
2 - Consultar 
3 - Editar
4 - Excluir 
0 - sair
""")

opc = input("Escolha: ")

match opc:
    case '0':
        os.kill
    case '1':
        print("comandos cadastro")
    case '2':
        print("comandos consulta")
    case '2':
        print("comandos editar")
    case '3':
        print("comandos excluir")
    case _:
        print("opc invalida")