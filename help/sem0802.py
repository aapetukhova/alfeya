##чтение посторчно взять 4 значение
##создание словаря
##

def reading(name):
    values = []
    with open(name, "r", encoding="utf-8") as f:
        for line in f:
            value = line.split("\t")[3]
            values = values.append(value)
        return values

def slovar(values):
    por = {}
    for value in values:
        if value in por:
            por[values] += 1
        else:
            por[values] = 1
    return values

values = reading("table.tab")
problem = slovar(values)
for key, value in problem.items():
    print(key, value)

