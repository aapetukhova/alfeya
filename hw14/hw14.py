##Создать словарь, в котором ключами являются предложения,
##а в качестве значения выступает словарь с ключами-словами
##и значениями-длинами слов
##(например, {"Мама вымыла раму": {"Мама": 4, "вымыла": 6, "раму": 4}, ...}). 

def text(filename):
    d = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            stns = line.split('.')
            for stn in stns:
                d.append(stn.strip('\n').strip('—«»123456789,/\@#$%^&*():"{}[];_-=+<>№'))
    return d

def one(x):    
    a = {word.strip('—«»123456789,/\@#$%^&*():"{}[];_-=+<>№'): len(word) for word in x.split()}
    return a

def two(d):
    b = {item: one(item) for item in d}
    return b

def main():
    print(two(text('text.txt')))

    
if __name__ == '__main__':
    main()


    
    



    
    
