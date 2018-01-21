 #coding=utf-8
import random

def noun(gen_or_num):
    if gen_or_num == 'pl':
        with open("plural.txt", encoding="utf-8") as p:
            text1 = p.read()
            plural = text1.split()
        return random.choice(plural)
    elif gen_or_num == 'm':
        with open("masculin.txt", encoding="utf-8") as m:
            text2 = m.read()
            masculin = text2.split()
        return random.choice(masculin)
    elif gen_or_num == 'f':
        with open("feminin.txt", encoding="utf-8") as f:
            text3 = f.read()
            feminin = text3.split()
        return random.choice(feminin)
    else:
        with open("neutral.txt", encoding="utf-8") as n:
            text4 = n.read()
            neutral = text4.split()     
        return random.choice(neutral)
def verb():
    with open("verbs.txt", encoding="utf-8") as v:
        text5 = v.read()  
        verbs = text5.split()
    return random.choice(verbs)
def adj():
    with open("adjs.txt", encoding="utf-8") as a:
        text6 = a.read()  
        adjs = text6.split()
    return random.choice(adjs)
def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)
def verse1():
#функция собирает строчку из определенного артикля, сущ. мн.ч., глагола 3 л. мн.ч. и прилагательного
#например, "die Bilder sind schön"
    return 'die' + ' ' + noun('pl') + ' ' + 'sind' + ' ' + adj() + punctuation()
def verse2():
#функция собирает строчку из определенного артикля, сущ. м.р., cоюза, опр. артикля, сущ. ж.р.
#например, "der Drucker und die Brille"
    return 'der' + ' ' + noun('m') + ' ' + 'und' + ' ' + 'die' + ' ' + noun('f') + punctuation()
def verse3():
#функция собирает строчку из неопределенного артикля, сущ. ср.р. и глагола
#например, "ein Fädchen atmet"
    return 'ein' + ' ' + noun('n') + ' ' + verb() + punctuation()
def make_verse():
        return verse1() + '\n' + verse2() + '\n' +  verse3()


print(make_verse())
