import random

count = 0
lista_peca = []
total_discount = 0
quantidade = 0

while count < 3:
    count +=1
    nome_peca = str(input('Nome da peça: '))
    if nome_peca.lower().__contains__('paraf') or nome_peca.lower().__contains__('porca') or nome_peca.lower().__contains__('arrue'):
        preco_peca = float(input('Preço da peça: '))

        if nome_peca.lower().__contains__('paraf'):
            prod_discount = (preco_peca * 10) / 100
            preco_peca -= prod_discount
            print(f'O preço desta peça menos 10% de desconto dá: {preco_peca}!')
            total_discount += prod_discount
        elif nome_peca.lower().__contains__('porca'):
            prod_discount = (preco_peca * 20) / 100
            preco_peca -= prod_discount
            print(f'O preço desta peça menos 20% de desconto dá: {preco_peca}!')
            total_discount += prod_discount
        else:
            prod_discount = (preco_peca * 30) / 100
            preco_peca -= prod_discount
            print(f'O preço desta peça menos 30% de desconto dá: {preco_peca}!')
            total_discount += prod_discount
        lista_peca.append({
            'nome_peca': nome_peca.title(),
            'preco_peca': preco_peca,
        })
    else:
        while not nome_peca.lower().__contains__('para') or nome_peca.lower().__contains__('porca') or nome_peca.lower().__contains__('arru'):
            nome_peca = str(input(f'O produto {nome_peca}, não existe na nossa lista de peças!\nPor favor introduza um nome válido para peça, como (parafuso, porcas ou arruelas): '))
            preco_peca = float(input('Preço da peça: '))
            lista_peca.append({
                'nome_peca': nome_peca.title(),
                'preco_peca': preco_peca,
            })

count_parafuso = 0
count_porca = 0
count_arruelas = 0
client_name = str(input('Introduza o nome do cliente: '))
for _ in range(random.randint(0, 13)):
    # when I get here I really get tired!
    nome = lista_peca[random.randint(0, 2)].get('nome_peca')
    print(f'{nome}')
    if nome == 'Parafuso' or nome == 'Parafusos':
        count_parafuso += 1
    elif nome == 'Porca' or nome == 'Porcas':
        count_porca += 1
    elif nome == 'Arruelas' or nome == 'Arruela':
        count_arruelas += 1

    print(f'{nome}')