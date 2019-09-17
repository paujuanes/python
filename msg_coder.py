dctmap = {
    'a':'u',
    'b':'i',
    'c':'v',
    'd':'j',
    'e':'w',
    'f':'k',
    'g':'x',
    'h':'l',
    'i':'y',
    'j':'m',
    'k':'z',
    'l':'a',
    'm':'n',
    'n':'b',
    'o':'p',
    'p':'c',
    'q':'o',
    'r':'d',
    's':'q',
    't':'e',
    'u':'r',
    'v':'f',
    'w':'s',
    'x':'g',
    'y':'t',
    'z':'h',
}

line = input('Write something down: (no punctuation)\n')

line = line.lower()
line = line.translate(line.maketrans(dctmap))
words = line.split()

new_line = list()

for word in words:
    if len(word) <= 2:
        if len(word) == 1:
            new_line.append(word)
            continue
        else:
            word = word[-1] + word[0]
    elif len(word) == 3:
        word = word[-1] + word[1] + word[0]
    elif len(word) == 4:
        word = word[-1] + word[-2] + word[1] + word[0]
    else:
        word = word[-1] + word[-2] + word[2:-2] + word[1] + word[0]
    new_line.append(word)

secret = ' '.join(new_line)

print(secret)