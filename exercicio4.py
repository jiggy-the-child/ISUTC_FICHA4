count = 0
lista_peca = []

while count < 3:
    count +=1
    nome_peca = str(input('Nome da peça: '))
    
    if nome_peca.lower().__contains__('paraf') or nome_peca.lower().__contains__('porca') or nome_peca.lower().__contains__('arrue'):
        preco_peca = float(input('Preço da peça: '))

        if nome_peca.lower().__contains__('paraf'):
            preco_peca -= (preco_peca * 10) / 100
            print(f'O preço desta peça menos 10% de desconto dá: {preco_peca}!')
        elif nome_peca.lower().__contains__('porca'):
            preco_peca -= (preco_peca * 20) / 100
            print(f'O preço desta peça menos 20% de desconto dá: {preco_peca}!')
        else:
            preco_peca -= (preco_peca * 30) / 100
            print(f'O preço desta peça menos 30% de desconto dá: {preco_peca}!')
        
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