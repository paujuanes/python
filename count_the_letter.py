word = input('Enter a word:\n')
letter = input('Enter the letter to count:\n')

# convert to lowercase
l_word = word.lower()
l_letter = letter.lower()

# defining function
def count(_word, _letter):
    times = 0
    for i in _word:
        if i == _letter:
            times += 1
    return times

ntimes = count(l_word, l_letter)

print('The letter %s was found %d times in the word %s.' %(letter, ntimes, word))