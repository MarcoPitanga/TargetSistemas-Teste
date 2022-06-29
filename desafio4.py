#   DESAFIO 4

# entrada de dados
dados = [
    {
        'estado': 'SP',
        'valor': 67836.43
    },
    {
        'estado': 'RJ',
        'valor': 36678.66
    },
    {
        'estado': 'MG',
        'valor': 29229.88
    },
    {
        'estado': 'ES',
        'valor': 27165.48
    },
    {
        'estado': 'Outros',
        'valor': 19849.53
    }
]

# calculando o total
total = 0
for x in dados:
    total += x['valor']


# transformando em porcentagem e mostrando resultado
print("Percentual de representação:\n")
for x in dados:
    print(f"{x['estado']}: {(x['valor']/total)*100:.2f} %")
