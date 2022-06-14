import random

def calcula_salario():
    salario_fixo = 5500
    salario_total = 0
    valor_vendas = 0
    
    for _ in range(random.randint(0, 10)):
        carro_vendido = random.choice(['True', 'False'])
        print(f'Carro vendido: {carro_vendido}')
        if carro_vendido == 'True' or carro_vendido == True:
            valor_vendas += 4000
            salario_fixo += 4000
            print(f'Valor das Vendas: {valor_vendas};\n\
                    Salário total: {salario_total}'
                )
        salario_total = salario_fixo
        
        if valor_vendas != 0:
            percent_sales = (valor_vendas * 5) / 100
            print('AUMENTO_PERCENTUAL: {}'.format(percent_sales))
            salario_total += percent_sales
        else:
            salario_total += salario_fixo
        
    return f'O salário total deste funcionário será: {salario_total}MT'.format(salario_total=salario_total)
print(calcula_salario())