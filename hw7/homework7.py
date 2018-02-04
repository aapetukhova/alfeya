import random

def words_from_file(filename):
    with open(filename, encoding='utf-8') as f: 
        text = f.read()  
    text = text.replace('-', '')  
    text = text.replace(',', '').replace('.', '')  
    text = text.lower() 
    words = text.split()  
    return words 

def counter(words):
    ed = 0
    y = 0
    for word in words:
        if word[-2:] == 'ed':
            ed += 1
            if word[-3] == 'i':
                y += 1
    return ed, y

words = words_from_file('text.txt')
ed_form, y_verbs = counter(words)
print('Number of -ed forms: ',ed_form,'\n','Number of -y verbs: ',y_verbs)

