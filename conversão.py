#preços da moeda
precos_em_moedas = [
    [1, 6, 8, 10],
    [3, 7, 10, 15]
]

taxas_de_conversao = {
    'JPY': 26.35,
    'GBP':0.14
}

def conversao_para_real(preco, moeda):
    return preco * taxas_de_conversao[moeda]

preco_em_real = [
    [conversao_para_real(preco, 'JPY') for preco in linha] if i == 0
    else [conversao_para_real(preco,'GBP') for preco in linha]
    for i, linha in enumerate(precos_em_moedas)
    ]

print("Preços convertidos em real: ")
for linha in preco_em_real:
    print(linha)