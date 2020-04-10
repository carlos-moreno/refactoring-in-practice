"""
01. donuts
Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""


def donuts(count, limit=10):
    if count >= limit:
        qty = "many"
    else:
        qty = str(count)

    return f"Number of donuts: {qty}"


def test_donuts():
    assert donuts(4) == "Number of donuts: 4"
    assert donuts(9) == "Number of donuts: 9"
    assert donuts(10) == "Number of donuts: many"
    assert donuts(99) == "Number of donuts: many"
