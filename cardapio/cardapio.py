print('''
        Cod      Produto        Valor
         1        MAÇÃ        R$ 6.00
         2       BANANA       R$ 5.00
         3      UVA VERDE     R$ 7.00
         4      UVA ROXA      R$ 7.00
         5        PERA        R$ 4.00
         6       MORANGO      R$ 10.00
         7        MANGA       R$ 3.00
         8        CAJA        R$ 5.00
         ''')
soma = 0
quant = int(input("Digite a quantidade de produtos: "))
while quant > 0:
    cod = int(input("Digite o codigo do produto: "))
    if cod==1:
        quant_prod = int(input("Digite a quantidade de maçãs: "))
        soma += quant_prod*6
    elif cod==2:
        quant_prod = int(input("Digite a quantidade de bananas: "))
        soma += quant_prod*5
    elif cod==3:
        quant_prod = int(input("Digite a quantidade de uvas verdes: "))
        soma += quant_prod*7
    elif cod==4:
        quant_prod = int(input("Digite a quantidade de uvas roxas: "))
        soma += quant_prod*7
    elif cod==5:
        quant_prod = int(input("Digite a quantidade de peras: "))
        soma += quant_prod*4
    elif cod==6:
        quant_prod = int(input("Digite a quantidade de morangos: "))
        soma += quant_prod*10
    elif cod==7:
        quant_prod = int(input("Digite a quantidade de mangas: "))
        soma += quant_prod*3
    elif cod==8:
        quant_prod = int(input("Digite a quantidade de cajás: "))
        soma += quant_prod*5

    quant-= 1
print(f"Esse é o total da sua compra R${soma}! Obrigado e volta sempre. ")