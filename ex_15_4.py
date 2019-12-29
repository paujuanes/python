'''
Exercise 15.4 (Assignment)
Many students in many courses

This application will read roster data in JSON format, parse the file, and then
produce an SQLite database that contains a User, Course, and Member table and
populate the tables from the data file.

You can base your solution on this code: www.py4e.com/code3/roster/roster.py
- this code is incomplete as you need to modify the program to store the role
column in the Member table to complete the assignment.

*Solution by Pau Juanes, Dec 29th 2019*
'''

import sqlite3
import json

conn = sqlite3.connect(r'databases/roster.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

file_r = input('Enter JSON file name: ')
if len(file_r) < 1: file_r = r'roster_data.json'

content = open(file_r, 'r').read()
json_data = json.loads(content)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name, title, role)

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)''', (user_id, course_id, role))
    
    conn.commit()

cur.execute('''
    SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1
''')
print(cur.fetchone())

conn.close()