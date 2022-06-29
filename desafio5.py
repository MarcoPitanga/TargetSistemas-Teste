#   DESAFIO 5

# entrada de dados
palavra = input("Digite a palavra para inverter: ")

palavra_invertida = ''

# passando o inverso da palavra para outra variavel
i = len(palavra)
while True:
    palavra_invertida += palavra[i-1]
    i -= 1
    if i <= 0:
        break

# mostrando resultado
print(f'Palavra invertida: {palavra_invertida}')
