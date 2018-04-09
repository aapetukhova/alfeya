import re
import collections

def reading():
    with open ('F.xml', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def header(lines):
    n=0
    for line in lines:
        opening = re.search('<teiHeader>', line)
        closing = re.search('</teiHeader>', line)
        if opening:
            p = n
        if closing:
            m = n
        n+=1
    s = m - p +1
    s = str(s)
    return s     

def writing(filename, s, dictionary):
    with open (filename, 'w', encoding='utf-8') as f:
        f.write('Количество строк: ')
        f.write(s + '\n')
        f.write('Словарь:' + '\n')
        for key, value in dictionary.items():
            f.write(key +' ')
            f.write(str(value) + '\n')
        

        
    
def morph(lines):
    l = []
    for line in lines:
        res = re.search('<w.+?type="(.*?)">', line)
        if res:
            l.append(res.group(1))
    dictionary = collections.Counter(l)
    return dictionary
####    with open('output.xml', 'w', encoding='utf-8') as f:
##    for key, value in dictionary.items():
##            print(key, value)
        
    
    
    




def main():
    x = header(reading())
    d = morph(reading())
    writing('output.xml', x, d)


if __name__ == '__main__':
    main()



    
        
