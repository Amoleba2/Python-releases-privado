nota1 = float(input("digite a primeira nota: "))

if (nota1 <= 0 or nota1 > 10 ):
    print("apenas numeros de 0-10")
    input("enter para sair")
    exit()




nota2 = float(input("digite a segunda nota: "))

if (nota2 <= 0 or nota2 >10 ):
    print("apenas numeros de 0-10")
    input("aperteenter para sair")
    exit()


nota3 = float(input("digite a terceira nota: "))

if (nota3 <= 0 or nota3 >10 ):
    print("apenas numeros de 0-10")
    input("enter para sair")
    exit()



media = ((nota1+nota2+nota3) /3)



    



if (media >= 6):
    print("passou de ano! ")
    input("enter para sair")
    exit()
else:
    print("nao passou de ano")
    input("enter para sair")
    exit()