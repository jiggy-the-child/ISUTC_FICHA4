import random

def calcula_salario():
    salario_fixo = 5200 * 2
    salario_total = 0
    valor_vendas = 0
    
    for _ in range(random.randint(0, 10)):
        carro_vendido = random.choice(['True', 'False'])
        if carro_vendido == 'True':
            valor_vendas += 4000
            salario_fixo += 4000
        salario_total = salario_fixo
        
        if valor_vendas != 0:
            percent_sales = (valor_vendas * 5) / 100
            salario_total += percent_sales
        else:
            salario_total += salario_fixo
    return f'O salário total deste funcionário será: {salario_total}MT'.format(salario_total=salario_total)
print(calcula_salario())