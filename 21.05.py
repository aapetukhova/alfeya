def text(filename):
    symbols = '123456789.,/!?|\@#$%^&*():"{}[];_-=+<>№'
    d = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                d.append(word.strip(symbols))
    return d

def out(d):
    r = {key: value for key, value in enumerate(d)}
##    print(r)
    t = '{}. {:>16}'
    for key, value in r.items():
        print(t.format(key, value))

out(text('text.txt'))

    

##import re
##s = ['SIVJN', 'dfv', 'цвымлэ', 'АЫ']
##s1 = [ i.lower() for i in s if re.search('^[a-zA-Z]+$', i) ]
##print(s1)
##
##
##t = '{}{}'
##a = 98
##b = 23
###print(t.format(a, b))
##9823
##t1 = '{},{}'
##print(t1.format(a, b))
###98,23
##t2 = '{{}}'
##print(t2.format(a, b))
###{}
##b= 'sdv'
##print(t1.format(a, b))
###98,sdv
##
##
##>>> s = [1, 23, 456]
##>>> print(s)
##[1, 23, 456]
##>>> t = 'Age: '{:>10}
##SyntaxError: invalid syntax
##>>> t = ''Age: '{:>10}'
##SyntaxError: invalid syntax
##>>> t = 'Age: {:>10}'
##>>> for i in s:
##	print(i)
##
##	
##1
##23
##456
##>>> t = 'Age: {:<10}'
##>>> t = 'Age: {:>10}'
##>>> for i in s:
##	print(t.format(i))
##
##	
##Age:          1
##Age:         23
##Age:        456
##>>> 


