idade = 67
preco_passagem = 0
if idade < 18:
    print("Menor de idade")
    preco_passagem = 5.25
elif idade >= 18 and idade < 65:
    print("Adulto")
    preco_passagem = 7.50 
else:
    print("Idoso")
    preco_passagem = 00
    print("Passagem gratuita")

print("Preco da passagem:", "R$= " ,  preco_passagem)


   