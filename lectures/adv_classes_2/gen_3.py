
def subgenerator():
    yield 'Subgen1'
    yield 'Subgen2'
    yield 'Subgen3'


def generator():
    yield "Gen 1"
    yield "Gen 2"
    yield from subgenerator()
    yield "Gen 3"
    yield "Gen "


for i in generator():
    print(i, end = ' ')