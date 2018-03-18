import re
def main():
    with open('bulgakov.txt', encoding='utf-8') as f:
        text = f.read()
        words = text.split()
        for word in words:
            r = re.search('(^[цкнгшщзхфвпрлджчсмтб]([уеыаоэяиюё])([цкнгшщзхфвпрлджчсмтб]\\2)+$)', word)
            if r:
                g = r.group(1)
                print(g)

if __name__ == '__main__':
    main()

