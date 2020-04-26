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
from collections import defaultdict


def open_(filename):
    if filename == "-":
        return sys.stdin

    return open(filename)


def read(file):
    with file as f:
        return f.read()


def split(content):
    content = content.lower()
    return content.split()


def count(words):
    d = defaultdict(int)
    for w in words:
        d[w] += 1
    return d.items()


def lines(word_count):
    return "\n".join(f"{w} {c}" for w, c in word_count)


def top(word_count, limit=20):
    return sorted(word_count, key=lambda t: t[-1], reverse=True)[:limit]


def word_counter(filename, order):
    return lines(order(count(split(read(open_(filename))))))


def main():
    if len(sys.argv) != 3:
        print("Utilização: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    try:
        order = {"--count": sorted, "--topcount": top}[option]
    except KeyError:
        print("unknown option: " + option)
        sys.exit(1)

    print(word_counter(filename, order))


if __name__ == "__main__":
    main()
