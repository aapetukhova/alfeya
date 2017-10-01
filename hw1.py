a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if a==0:
    print('Нет решений')
elif (a*b==c and c==-b/a):
    print('Заданные числа обладают свойствами')
else:
    print('Заданные числа не обладают свойствами')
