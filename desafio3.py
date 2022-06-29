#   DESAFIO 3

import json

# pegando os dados do JSON
with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)


# ordenando os dados pelo valor em ordem crescente
for i in range(len(dados)):
    min = i

    for j in range(i+1, len(dados)):
        if dados[j]['valor'] < dados[min]['valor']:
            min = j

    dados[i], dados[min] = dados[min], dados[i]


# pegando o menor valor diferente de 0
for x in dados:
    if x['valor'] != 0:
        menor_valor = x['valor']
        break


# calculando a media mensal de faturamento
valor_total = 0
quantidade_dias = 0

for x in dados:
    valor_total += x['valor']
    if x['valor'] != 0:
        quantidade_dias += 1

media_faturamento = valor_total / quantidade_dias


# calculando quantidade de dias com faturamento superior a media
dias_faturamento_superior = 0
for x in dados:
    if x['valor'] > media_faturamento:
        dias_faturamento_superior += 1


# resultados
print(f"O menor valor de faturamento foi: {dados[0]['valor']}")
print(f"O menor valor de faturamento diferente de 0 foi: {menor_valor}\n")
print(f"O maior valor de faturamento foi: {dados[-1]['valor']}\n")
print(
    f"Numero de dias que o valor de faturamento foi superior a media mensal: {dias_faturamento_superior} dias")
