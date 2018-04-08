import random
import collections
##def words_from_file(filename):
##    """Принимает имя файла, а точнее его системный путь, и возвращает
##    список слов в нем
##    """
##    with open(filename, encoding='utf-8') as f:  # открвываем файл
##        text = f.read()  # прочитываем весь файл в строковую переменную
##    text = text.replace('-', '')  # удаляем дифисы
##    text = text.replace(',', '').replace('.', '')  # удаляем запятые и точки
##    # Тут можно было почистить текст еще лучше
##    text = text.lower()  # заменяем все заглавные на строчные
##    words = text.split()  # получаем список слов
##    return words  # возвращаем список слов
##def word_freq(words):
##    freq = {}
##    for word in words:
##        if word in freq:
##            freq[words] += 1 / len(words)
##        else:
##            freq[words] = 1 / len(words)
##    return words

#Постройте частотный список (словарь {слово: частотность}) для текста из файла, вывести n самых часто употребляемых слов.

##def text(filename):
##    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
##    d = []
##    with open(filename, encoding='utf-8') as f:
##        for line in f:
##            words = line.strip().lower().split()
##            for word in words:
##                d.append(word.strip(symbols))
##    return d
##
##def word_freq(words, top):
##    words = collections.Counter(words)

##
##
##def main():
##    print(maxim(word_freq(text('titanic.txt'))))
##
##
##    
##symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
##d = []
##with open('titanic.txt', encoding='utf-8') as f:
##    for line in f:
##        words = line.strip().lower().split()
##        for word in words:
##            d.append(word.strip(symbols))
##words = collections.Counter(d)
##n = 3
##for i in range (0, n):
##
##    for key in sorted(words, key=words.get, reverse=True):
##        print(key, words[key])
              
def most_common_words(filename, top):
    with open(filename, encoding='utf-8') as f:
        text = f.read().lower()
        words = collections.Counter(text.split())
    return dict(words.most_common(top))

def main():
    n = int(input("Number: "))
    top = most_common_words('titanic.txt', n)
    for key, value in top.items():
        print(key, value)
        
if __name__ == '__main__':
    main()
    

