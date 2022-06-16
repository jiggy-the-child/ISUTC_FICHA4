import random



# lista_peca = []
# total_discount, count_parafuso, count_porca, count_arruelas = 0, 0, 0, 0

# for _ in range(3):
#     nome_peca = str(input('Nome da peça: '))
#     if nome_peca.lower().__contains__('paraf') or nome_peca.lower().__contains__('porca') or nome_peca.lower().__contains__('arrue'):
#         preco_peca = 0
#         preco_peca = float(input('Preço da peça: '))
        
#         if nome_peca.lower().__contains__('paraf'):
#             prod_discount = (preco_peca * 20) / 100
#             total_discount += prod_discount
#         elif nome_peca.lower().__contains__('porca'):
#             prod_discount = (preco_peca * 10) / 100
#             total_discount += prod_discount
#         else:
#             prod_discount = (preco_peca * 30) / 100
#             total_discount += prod_discount
#         preco_peca -= prod_discount
#         vals = {
#             'nome_peca': nome_peca.title(),
#             'preco_peca': preco_peca,
#         }
#         lista_peca.append(vals)

# for _ in range(random.randint(0, 13)):
#     nome = lista_peca[random.randint(0, 2)].get('nome_peca')
#     if nome == 'Parafuso' or nome == 'Parafusos':
#         count_parafuso += 1
#     elif nome == 'Porca' or nome == 'Porcas':
#         count_porca += 1
#     elif nome == 'Arruelas' or nome == 'Arruela':
#         count_arruelas += 1

# client_name = str(input('Introduza o nome do cliente: '))
# linha = ''
# if count_parafuso > 0:
#     linha += f"\n{lista_peca[0].get('nome_peca')}         |       {count_parafuso}       |       {count_parafuso * lista_peca[0].get('preco_peca')}"
# if count_porca > 0:
#     linha += f"\n{lista_peca[1].get('nome_peca')}         |       {count_porca}          |       {count_porca * lista_peca[1].get('preco_peca')}"
# if count_arruelas > 0:
#     linha += f"\n{lista_peca[2].get('nome_peca')}         |       {count_arruelas}       |       {count_arruelas * lista_peca[2].get('preco_peca')}" 
# recibo = f"ISUTC FICHA 4\n______________________________________\nNome do Cliente: {client_name};\n______________________________________\n\nDescrição do Produto        |       Quantidade        |             Total das Linhas        \n{linha}\n\n\n______________________________________\nTotal de venda: {(count_parafuso * lista_peca[0].get('preco_peca')) + (count_porca * lista_peca[1].get('preco_peca')) + (count_arruelas * lista_peca[2].get('preco_peca'))}MT;\n______________________________________\nTotal Disconto: {total_discount}MT."
# print(recibo)