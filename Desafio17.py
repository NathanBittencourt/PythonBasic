from math import hypot
Oposto = float(input('Comprimento do cateto oposto: '))
Adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (Oposto ** 2 + Adjacente ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
print()
print('Utilizando a biblioteca math, função hypot (hipotenusa):')
print()
hipotenusa = hypot(Oposto, Adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))