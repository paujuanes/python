text = "X-DSPAM-Confidence:    0.8475"

pos = text.rfind(' ')
num = text[pos+1:]
print(float(num))