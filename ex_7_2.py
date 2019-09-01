file = input('Enter the name of the file you want to scan:\n')

try:
    fhand = open(file)
except:
    if file == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('Sorry, but such file does not exist: {:s}'.format(file))
    quit()

count = 0
add = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    pos = line.find(' ')
    raw_coef = line[pos+1:] #  Isolating the raw coefficient
    #print(repr(raw_coef)) #  Just a control print to check how it goes
    coef = float(raw_coef.strip()) #  A strip before converting it into float, just in case...
    count += 1
    add += coef

avg = add/count
print('Average spam confidence: {:g}'.format(avg))