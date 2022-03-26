larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = larg * alt

print('Sua parede tem a dimensão de {} x {} e sua área é de {:2.2f}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:2.1f} litros de tinta.'.format(tinta))