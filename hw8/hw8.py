#makes the dictionary of problems and hints
def dict_maker(filename):
    d = {}
    with open (filename, encoding='utf-8') as f:
        hint = ''
        for line in f:
            guess, hint = line.split(',')
            hint_list = d.setdefault(guess, [])
            hint_list.append(hint.strip('\r\n'))
            hint = ''
    return d

#chooses a random secret word
import random
def rand_guess(d):
    keys = list(d.keys())
    key = random.choice(keys)
    return key

#chooseы a random hint for a secret word
def rand_hint(key, d):
    value = random.choice(d[key])
    return value

#makes every letter of a word a dot
def dot_word(word):
    dots = ''
    dot = '.'
    for letter in word:
        dots += dot
    return dots

#the main function
def main():
    d = dict_maker('wordlist.csv')
    key = rand_guess(d)
    hint = rand_hint(key, d)
    print(hint, dot_word(hint))
    attempt = input('Your attempt: ')
    if attempt == key:
        print('You win!')
    else:
        print('You lose')

if __name__ == '__main__':
    main()














##def rand_hint(keys):
##    values = list(d.values())
##    value = values
##    return random.choice(value)                




##dot_word('dof')

##print(dot_word(rand_guess(d)[1]))

##, ' ', ) 

##def main():
##    print('Insert your word')
##    word = input("My word: ")
##    if word == 'ya':
##        print('ok')
##    else:
##        print('schlecht')
##