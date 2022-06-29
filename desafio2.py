#   DESAFIO 2

# Função para gerar a sequencia Fibonacci e retornar o ultimo valor quando for maior ou igual ao valor digitado pelo usuario
def verificar_fibonacci(valor):
    lista = [0, 1]

    while True:

        lista.append(lista[-2] + lista[-1])
        if lista[-1] >= valor:
            return lista[-1]


# entrando com o valor e chamando a função
valor = int(input('Inserir numero para verificar: '))
resultado = verificar_fibonacci(valor)

# verificando se o valor pertence ou não
if resultado == valor:
    print(f'O valor {valor} pertence a sequencia Fibonacci.')
else:
    print(f'O valor {valor} nao pertence a sequencia Fibonacci.')
