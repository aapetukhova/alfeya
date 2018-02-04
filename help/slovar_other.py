mendeleev_table = {"oxygen": "O", "helium": "He", "gold": "Au", "natrium": "Na"}
##print(mendeleev_table["gold"])
mendeleev_table["silver"] = "Ag"
##print(mendeleev_table["silver"])
gases = {"hydrogen": "H", "azot": "N"}
mendeleev_table.update(gases)
##print(mendeleev_table["azot"])
##for name in mendeleev_table:
##    print(name)
##    print(mendeleev_table[name])
##keys = list(mendeleev_table.keys())
##print(keys)
##for symbol in mendeleev_table.values():
##    print(symbol)  # напечатает значение, в нашем случае символ элемента
##
##values = list(mendeleev_table.values())  # список символов элементов
##
##print(values)
##
##for key, value in mendeleev_table.items():
##    print(key, value)  # напечатает пару ключ—значение
### Еще один пример, для нашего словаря с химическими элементами:
##for name, symbol in mendeleev_table.items():
##    print(symbol, "—", name)
# Перебор по отсортированным ключам
##for key in sorted(mendeleev_table):
##    print(key, mendeleev_table[key])  # печатает пару ключ-значение, ключи упорядочены
for value in sorted(mendeleev_table.values()):
    print(value)
for key in sorted(mendeleev_table, key=mendeleev_table.get, reverse=True):
    print(key, mendeleev_table[value])
