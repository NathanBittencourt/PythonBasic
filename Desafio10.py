#Converter real em dólar
n = float(input('Informe a quantidade de dinheiro que você tem na carteira: R$'))

dolar = n / 5.65

print('Com R${} você pode comprar {:>2.2f} dólares'.format(n, dolar))