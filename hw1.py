a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if a==0:
    print('Нет решений')
elif (a*b==c and c==-b/a):
    print('Условие выполняется')
else:
    print('Условие не выполняется')
