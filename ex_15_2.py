'''
Exercise 15.2 (Assignment)
Counting Organizations

This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
(i.e. domain name of the email address) using a database with the following schema to maintain the counts:

CREATE TABLE Counts (
    org TEXT,
    count INTEGER
)

*Solution by Pau Juanes, Dec 23rd 2019*
'''

import sqlite3

conn = sqlite3.connect(r'databases/orgmaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
    CREATE TABLE Counts (
        org TEXT,
        count INTEGER
    )
''')

file_r = open(r'UMichigan_PyCourse/mbox.txt', 'r')
for line in file_r:
    if not line.startswith('From: '): continue
    parts = line.split()
    email = parts[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org= ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ? ', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

[print(row[0], row[1]) for row in cur.execute(sqlstr)]

cur.close()
