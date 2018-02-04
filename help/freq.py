import random

def words_from_file(filename):
    """Принимает имя файла, а точнее его системный путь, и возвращает
    список слов в нем
    """
    with open(filename, encoding='utf-8') as f:  # открвываем файл
        text = f.read()  # прочитываем весь файл в строковую переменную
    text = text.replace('-', '')  # удаляем дифисы
    text = text.replace(',', '').replace('.', '')  # удаляем запятые и точки
    # Тут можно было почистить текст еще лучше
    text = text.lower()  # заменяем все заглавные на строчные
    words = text.split()  # получаем список слов
    return words  # возвращаем список слов
def word_freq(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[words] += 1 / len(words)
        else:
            freq[words] = 1 / len(words)
    return words

slova = words_from_file(dictionary.txt)
slovar = word_freq(slova)
for i in range (0, len())
    
    
            
