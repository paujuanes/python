text = "X-DSPAM-Confidence:    0.8475";

point = text.find(':')
string = text[point+1:]
num = float(string.strip())
print(num)