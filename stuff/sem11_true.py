import random

def words_from_file(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
    text = text.replace("-", "")
    text = text.replace(".", "").replace(",", "")
    text = text.lower()
    words = text.split()
    return words

def ana(word):
    #Функция random.sample(sequence, count) возвращает список из count уникальных элементов последовательности (например списка или строки) взятых в случайном порядке. Заметим, что каждый элемент не может бытьбольше одного раза, а также напомним то, что элементами строки являютсяоднобуквенные строки.
    a = random.sample(word, len(word))
    new_word = "".join(a)
    return new_word

def create_csv_table(table_filename, words, n_ana):
    with open(table_filename, "w", encoding="utf-8") as f:
        for x in words:
            f.write(x)
            for i in range(n_ana):
                f.write(",")
                f.write(ana(x))
            f.write("\n")

words = words_from_file("semin11")
create_csv_table("table.csv", words, 3)
