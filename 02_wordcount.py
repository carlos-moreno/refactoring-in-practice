"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().
"""

import sys


# def print_words(filename):
#     result = {}
#     with open(filename, "r") as f:
#         words = f.readline().lower().split()
#         for word in words:
#             result[word] = result.get(word, 0) + 1
#     result = sorted(result.items(), key=lambda k: (k[0]))
#     for k, v in result:
#         print(f'{k} {v}')
#
#
# def print_top(filename):
#     result = {}
#     with open(filename, "r") as f:
#         words = f.readline().lower().split()
#         for word in words:
#             result[word] = result.get(word, 0) + 1
#     result = sorted(result.items(), key=lambda k: (k[1]), reverse=True)
#     for k, v in result[:20]:
#         print(f'{k} {v}')

def print_words(filename):
    d = {}
    f = open(filename)
    for line in f:
        words = line.split()
        for w in words:
            w = w.lower()
            d[w] = d.get(w, 0) + 1
    f.close()
    d = sorted(d.items(), key=lambda k: (k[0]))
    for k, v in d:
        print(f'{k} {v}')


def print_top(filename):
    result = {}
    with open(filename, "r") as f:
        words = f.readline().lower().split()
        for word in words:
            result[word] = result.get(word, 0) + 1
    result = sorted(result.items(), key=lambda k: (k[1]), reverse=True)
    for k, v in result[:20]:
        print(f'{k} {v}')


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print("Utilização: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == "__main__":
    main()
