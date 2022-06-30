# import random

anos = int(input('Introduza os anos que você tem: '))
ano = 30 * 12
if anos > 0 and anos < 126:
    anos *= ano
else:
    raise Exception('A idade tem de ser maior que \'0\' e menor que \'126\'.')

meses = int(input('Introduza os meses: '))
mes = 30
if meses > 0 and meses < 12:
    anos += (meses * mes)
else:
    raise Exception('Os meses devem estar entre \'1\' e \'12\'.')
print(f'Este utilizador já viveu {anos} dias.')