# antes de mais nada, só queria dizer que esse exercício está de parabéns.
# neste exercício algumas coisas são redundantes como: o número de vezes que o "round" aparece no código.

#TODO: melhorar a sintaxe;
import random

pieces = [
    {
        'name': 'Parafusos',
        'unit_price': round(random.uniform(1.0, 200.0), 2),
        'discount': 20,
    },
    {
        'name': 'Porcas',
        'unit_price': round(random.uniform(1.0, 200.0), 2),
        'discount': 10,
    },
    {
        'name': 'Arruelas',
        'unit_price': round(random.uniform(1.0, 200.0), 2),
        'discount': 30,
    }
]

def compra(pieces):
    count_para = 0
    count_porca = 0
    count_arru = 0
    for prod in pieces:
        if prod.get('name').lower() == 'parafusos':
            desconto = round((prod.get('unit_price') * prod.get('discount') / 100), 2)
            prod['discount'] = desconto
        elif prod.get('name').lower() == 'porcas':
            desconto = round((prod.get('unit_price') * prod.get('discount') / 100), 2)
            prod['discount'] = desconto
        else:
            desconto = round((prod.get('unit_price') * prod.get('discount') / 100), 2)
            prod['discount'] = desconto
    
    for _ in range(random.randint(1, 10)):
        prod = pieces[random.randint(0, 2)]
        if prod.get('name').lower() == 'parafusos':
            count_para += 1
        elif prod.get('name').lower() == 'porcas':
            count_porca +=1
        else:
            count_arru +=1
    
    receipt = 'Descrição        |        Quantidade        |        Preço Unit.        |        Desconto        |        Total        |'
    receipt += '\n_________________________________________________________________________________________________________________________'
    if count_para > 0:
        receipt += f"\n{pieces[0].get('name')}        |            {count_para}             |           {pieces[0].get('unit_price')}           |        {round(pieces[0].get('discount') * count_para, 2)}             |          {round((pieces[0].get('unit_price') * count_para) - (pieces[0].get('discount') * count_para), 2)}"
    if count_porca > 0:
        receipt += f"\n{pieces[1].get('name')}           |            {count_porca}             |           {pieces[1].get('unit_price')}           |        {round(pieces[1].get('discount') * count_porca, 2)}              |          {round((pieces[1].get('unit_price') * count_porca) - (pieces[1].get('discount') * count_porca), 2)}"
    if count_arru > 0:
        receipt += f"\n{pieces[2].get('name')}         |            {count_arru}             |           {pieces[2].get('unit_price')}           |        {round(pieces[2].get('discount') * count_arru, 2)}              |          {round((pieces[2].get('unit_price') * count_arru) - (pieces[2].get('discount') * count_arru), 2)}"
    receipt += f"\nTotal do Desconto: {round((pieces[0].get('discount') * count_para) + (pieces[1].get('discount') * count_porca) + (pieces[2].get('discount') * count_arru), 2)}"    
    receipt += f"\nTotal da Compra: {round((pieces[0].get('unit_price') * count_para) - (pieces[0].get('discount') * count_para) + (pieces[1].get('unit_price') * count_porca) - (pieces[1].get('discount') * count_porca) + (pieces[2].get('unit_price') * count_arru) - (pieces[2].get('discount') * count_arru), 2)}"
    return receipt           
print(compra(pieces=pieces))