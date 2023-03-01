
print('Bem Vindo a Loja do Carlos Eduardo Silva De Oliveira')#identificador
valorP = int(input('Entre com o valor do produto! '))# aqui capturo o valorP = valor do produto
valorQ = int(input('Entre com o valor da quantidade! '))# aqui capturo o valorQ = valor da quantidade de produtos
if(valorQ >= 10) and (valorQ <= 99): # se valor da quantidade for maior igual a 10 e menor igual a 99, 5% de desconto
    valorSemDesconto = valorP * valorQ # valor sem desconto é o valor do produto multiplicado pelo valor da quantidade
    desconto = valorSemDesconto * 0.05 # na variavel desconto eu salvo o valor sem desconto multiplicado por 0.05
    print(f'o valor do seu produto sem desconto é de: {valorSemDesconto}.00 R$')
    print(f'o desconto ganho foi de {desconto}0 R$')
    print(f'o valor com desconto é de: {valorSemDesconto - desconto}0 R$ (5% de Desconto)')
elif(valorQ >= 100) and (valorQ <= 999):
    valorSemDesconto = valorP * valorQ
    desconto = valorSemDesconto * 0.10
    print(f'o valor do seu produto sem desconto é de: {valorSemDesconto}.00 R$')
    print(f'o desconto ganho foi de {desconto}0R$')
    print(f'o valor com desconto é de: {valorSemDesconto - desconto}0 R$ (10% de Desconto)')
elif(valorQ >= 1000):
    valorSemDesconto = valorP * valorQ
    desconto = valorSemDesconto * 0.15
    print(f'o valor do seu produto sem desconto é de: {valorSemDesconto}.00 R$')
    print(f'o desconto ganho foi de {desconto}0 R$')
    print(f'o valor com desconto é de: {valorSemDesconto - desconto}0 R$ (15% de Desconto)')
# se o cliente nao levar uma quantidade que dê um possivel desconto, apenas encerro o programa com o valorQ * valorP
else:
    print(f'total a pagar {valorQ * valorP}.00 R$')
