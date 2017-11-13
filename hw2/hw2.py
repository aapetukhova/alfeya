print("Введите слово:")
word = input()
n = len(word)
k=n-1
for i in range( 0, n-1 ):
    if i % 2== 0 and ( word[i] == 'п' or word[i] == 'е' or word[i] == 'о' ):
        print( word[i] )
    else:
        k -= 1
if k == 0:
    print('Букв, удовлетворяющих условию, нет')
    

