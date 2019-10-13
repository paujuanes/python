import re

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')
emails = dict()
counts = 0

for line in file_r:
  line = line.rstrip()
  if re.search('\S@\S', line):
    lst = re.findall('[A-Za-z0-9]\S*@\S*[A-Za-z0-9]', line)
    for email in lst:
      emails[email] = emails.get(email, 0) + 1
      counts += 1

inverted = list()
for k,v in emails.items():
  inverted.append((v,k))

inverted.sort(reverse=True)

for v,k in inverted:
  print(k,v)

print(f'{counts} total email addresses (non-unique)')