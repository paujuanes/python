url = input('Enter URL to parse:\n')
string = input('Enter the characters to find:\n')

"""times = 0
for i in url:
    if i == string:
        times +=1
        found = True"""

if string in url:
    pos = url.find(string)
    subs = url[pos-10:pos+13]
    print('The characters are part of the url, in position %d. Here it is: %s' %(pos,subs))
else:
    print('The charaters are NOT part of the url.')