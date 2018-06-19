##Давайте так. Начните с того пробника, который у вас есть (можете начать присылать его решения). И дополнительное задание — то, которое я сейчас придумал:
##
##Есть корпус параллельных библий. Каждый стих в них размечен. Вам дается библия на английском и на языке чаморро (Austronesian). 
##1. Посчитать среднюю длину слова в чаморро.
##2. Вывести на экран список 10 самых частотных слов в чаморро и в английском: в формате 
##СЛОВО.ЧАМОРРО:СЛОВО.АНГЛИЙСКИЙ
##3. Для первых 100 стихов посчитать, как средняя длина предложения (в словах) в чаморро соотносится со средней длиной предложения в английском. Распечатать в файл в формате: НОМЕР.СТИХА~~~СООТНОШЕНИЕ
##4. (дополнительное задание) найти в интернете грамматику языка чаморро и отглоссировать первые 5 предложений.

#. Посчитать среднюю длину слова в чаморро.

import re
import collections

def text(filename):
    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
    with open (filename, encoding='utf-8') as f:
        d = []
        lines = f.readlines()
        for i in range (0, len(lines)):
            r = re.search('<seg.+>', lines[i])
            if r:
                words = lines[i+1].strip().lower().split()
                for word in words:
                    d.append(word.strip(symbols))
    return d

def avg_l(words):
    avg = sum(len(word) for word in words)/len(words)
    return avg

##2. Вывести на экран список 10 самых частотных слов в чаморро и в английском: в формате 
##СЛОВО.ЧАМОРРО:СЛОВО.АНГЛИЙСКИЙ

def freq(words):
    counter = collections.Counter(words)
    first = sorted(counter, key=counter.get, reverse=True)[:10]
    return first

def out(a, b):
    for i in range(10):
        print('{}:{}'.format(a[i], b[i]))

##3. Для первых 100 стихов посчитать, как средняя длина предложения (в словах)
##в чаморро соотносится со средней длиной предложения в английском. Распечатать
##в файл в формате: НОМЕР.СТИХА~~~СООТНОШЕНИЕ

def poems(filename):
    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
    with open (filename, encoding='utf-8') as f:
        a = []
        lines = f.readlines()
        for i in range (0, len(lines[:100])):
            r = re.search('<seg.+>', lines[i])
            if r:
                words = lines[i+1].strip().lower().split()
                for word in words:
                    a.append(len(word.strip(symbols)))
    

    
    




def main():
##    print(avg_l(text('test.xml')))
##    print(text('test.xml'))
##    print(text('test.xml'))
##    print(text('test.xml'))
    out(freq(text('Chamorro-PART.xml')), freq(text('English.xml')))
    
if __name__ == '__main__':

    main()



        
                

        
        
    
