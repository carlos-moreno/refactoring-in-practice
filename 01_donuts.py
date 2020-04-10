"""
01. donuts
Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""


def donuts(count):
    return f"Number of donuts: {Quantity(count)}"


class Quantity:
    def __init__(self, count, limit=10):
        self.count = count
        self.limit = limit

    @property
    def many(self):
        return self.count >= self.limit

    def __str__(self):
        return "many" if self.many else str(self.count)


def test_quantity():
    assert str(Quantity(4)) == "4"
    assert str(Quantity(9)) == "9"
    assert str(Quantity(10)) == "many"


def test_donuts():
    assert donuts(4) == "Number of donuts: 4"
    assert donuts(9) == "Number of donuts: 9"
    assert donuts(10) == "Number of donuts: many"
    assert donuts(99) == "Number of donuts: many"
