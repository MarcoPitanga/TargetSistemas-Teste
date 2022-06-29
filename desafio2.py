#   DESAFIO 2:
#   Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#   (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
#   ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


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
