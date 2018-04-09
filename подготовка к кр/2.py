##import re
##
##def page(filename):
##    with open( filename, encoding='utf-8') as f:
##        text = f.read()
##    r = re.findall('((>[А-Я][а-яё]+ [А-Я][а-яё]+ [А-Я][а-яё]+?вили</a>)|(>[А-Я][а-яё]+ [А-Я][а-яё]+ [А-Я][а-яё]+?дзе</a>))', text)
##    return r
##
##def gal(r):
##    new = []
##    for name in r:
##        imya = name.split( )
##        if len(imya[0]) > 7:
##            new.append(name)
##    return new
##
##def changed(filename, text, new, exp, g):
##    for name in new:
##        galiktion = re.sub( exp, g, name)
##        text = text.replace(name, exp)
##    with open(filename, 'w', encoding='utf-8') as f:
##        f.write(text)
##
##def main():
##    s = page('short.html')
##    gala = gal(s)
##    changed('galaktion.html', s, gala, '>[А-Яа-яё]+ ', 'Галактион')
##
##if __name__ == '__main__':
##    main()
##


import re

def öffnen_file():
    with open('georgians.html', 'r', encoding='utf-8') as file:
        html = file.read()
    return html

def familie(html):
    dze = re.findall('>[А-Яа-яЁё ]+?дзе</a>', html)
    print(dze)
    shv = re.findall('>[А-Яа-яЁё ]+?швили</a>', html)
    if len(dze) > len(shv):
        k = round(len(dze)/len(shv), 2)
        print('Людей с фамилией на -дзе в ', k, ' раз больше, чем на -швили')
    elif len(dze) < len(shv):
        k = round(len(shv)/len(dze), 2)
        print('Людей с фамилией на -дзе в ', k, ' раз меньше, чем на -швили')
    else:
        print("Людей на -дзе столько же, сколько на -швили")
    return dze, shv

def beria(html):
    ija = re.findall('>[А-Я][а-яё]+ [А-Я][а-яё]+ [А-Я][а-яё]+?ия</a>', html)
    print('Людей с фамилией на -ия: ', len(ija))
    return ija

def find_galaktions(html, dze, shv):
    dze.extend(shv)
    gal = []
    for name in dze:
        name_l = name.split( )
        if len(name_l[0]) > 7:
            gal.append(name)
    return gal

def change(html, gal):
    for name in gal:
        galak = re.sub('>[А-Я][а-яё]+ ', '>Галактион ', name)
        html = html.replace(name, galak)
    with open('galaktion.html', 'w', encoding='utf-8') as file:
        file.write(html)
    

def main():
    html = öffnen_file()
    dze, shv = familie(html)
    ija = beria(html)
    names = find_galaktions(html, dze, shv)
    change(html, names)
    
if __name__ == '__main__':
    main()
