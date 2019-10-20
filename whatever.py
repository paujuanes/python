import string

#alphabet = list(string.ascii_lowercase)

sentence = 'The quick, brown, fox jumps over the lazy dog.'
sentence = sentence.translate(str.maketrans('', '', string.punctuation))
sentence = sentence.lower()