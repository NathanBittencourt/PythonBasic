metro = float(input('Informe uma distância em metros: '))

km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000 

print('Valor em kilômetros: {} \nValor em hectômetros: {} \nValor em decâmetros: {}\nValor em decímetros: {}\nValor em centímetros: {}\nValor em milímetros: {}'.format(km, hm, dam, dm, cm, mm))