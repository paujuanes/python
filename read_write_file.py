fhand = open(r'UMichigan_PyCourse\mbox.txt')
fedit = open('output.txt', 'w')
okline = 0  # Counting processed lines
koline = 0  # Counting ignored lines
'''
for line in fhand :
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1 :
        koline += 1
        continue
    # Split the line to isolate the left part of the @ (the username)
    part = line.partition('@')
    # Find the whitespace before the username
    pos = part[0].rfind(' ')
    # Now we got the username!
    username = part[0][pos+1:]
    # Let's check if there's any tab character and delete it
    if username.find('\t') != -1 :
        tab = username.find('\t')
        username = username[tab+1:]
    print(repr(username))
    # Write the username to the output file
    fedit.write('{:s} \n'.format(username))
    okline +=1

print('Emails found: {:d}. Ignored lines: {:d}'.format(okline, koline))
fedit.write('Emails found: {:d}. Ignored lines: {:d}'.format(okline, koline))
fedit.close()
fhand.close()
'''
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        koline += 1
        continue
    words = line.split()
    email = words[1]
    email_split = email.split('@')
    username = email_split[0]
    okline +=1
    print(username)