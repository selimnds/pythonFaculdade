# exc semana
import os
os.system("cls")

# print(f"""
# 1, 2, 3, 4, ou 5
# """)
# exc = int(input("escolha: "))

# # match exc:
#     case 1:
#         dia = input("Digite numero de 1 a 6: ")

#         match dia:
#             case 1:
#                 print('domingo')
#             case 2:
#                 print('segunda-feira')
#             case 3:
#                 print('terça-feira')
#             case 4:
#                 print('quarta-feira')
#             case 5:
#                 print('quinta-feira')
#             case 6:
#                 print('sábado')
#             case _:
#                 print('digite um número válido')
#     case 2:
#         mes = input("Digite numero de 1 a 12: ")

#         match mes:
#             case 1:
#                 print("janeiro")
#             case 2:
#                 print("fevereiro")
#             case 3:
#                 print("março")
#             case 4:
#                 print("abril")
#             case 5:
#                 print("maio")
#             case 6:
#                 print("junho")
#             case 7:
#                 print("julho")
#             case 8:
#                 print("agosto")
#             case 9:
#                 print("setembro")
#             case 10:
#                 print("outubro")
#             case 11:
#                 print("novembro")
#             case 12:
#                 print("dezembro")
#     case 3:
#         letra = input("Digite uma letra: ")
#         letra = letra.lower()
#         crrt = True

#         if letra >= 'a' and letra <= 'z':
#             match letra:
#                 case 'a' | 'e' |  'i' |  'o' |  'u':
#                     print("vogal")
#                 case _:
#                     print("consoante")
#         else:
#             print("não é letra")
#     case 4:
#         n1 = int(input("Digite um nunero: "))
#         n2 = int(input("Digite outro numero: "))
#         op = input("digite um operador aritmético: ")
#         valido = True

#         match op:
#             case '+' | '-' | '*' | '/':
#                 valido=True

#         if valido == True and n1 != 0 and n2 != 0:
#             if op == '+':
#                 print(n1+n2)
#             if op == '-':
#                 print(n1-n2)
#             if op == '*':
#                 print(n1*n2)
#             if op == '/':
#                 print(n1/n2)
#         else:
#             print("Inválido")
#     case 5:
#         placa = int(input("Digite a placa: "))
        
#         final = placa % 10
        
#         match final:
#             case 1 |  2:
#                 print("segunda")
#             case 3 | 4:
#                 print("terça")
#             case 5 | 6:
#                 print("quarta")
#             case 7 | 8:
#                 print("quinta")
#             case 9 | 0:
#                 print("sexta")

r = input("digite qualquer 1 caractere: ")
match r:
    case i if r >= 'a' and r <= 'z':
        if r == 'a' or r == 'e' or r == 'i' or r == 'o' or r == 'u':
            print("vogal minuscula")
        else: 
            print("consoante minuscula")
    case i if r >= 'A' and r <= 'Z':
        if r == 'A' or r == 'E' or r == 'I' or r == 'O' or r == 'U':
            print("consoante MAIUSCULA")
        else:
            print("consoante MAIUSUCLA")
    case i if r != 'a' and r != 'z' and r != 'A' and r != 'Z':
        r = int(r)
        if r >= 0 and r <= 9:
            print("um digito")
        else:
            print("numero invalido")
    case _:
        print("caractere especial")
    
