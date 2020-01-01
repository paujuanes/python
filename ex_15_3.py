'''
Exercise 15.3 (Assignment)
Musical Track Database

This application will read an iTunes export file in XML and produce a properly
normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)

*Solution by Pau Juanes, Dec 27th 2019*
'''

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect(r'databases/trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER, skipped INTEGER
)
''')

file_n = input('Enter XML file name: ')
if len(file_n) < 1: file_n = r'UMichigan_PyCourse/tracks/Library.xml'

xmlcont = ET.parse(file_n)
entries = xmlcont.findall('dict/dict/dict')  # A list of all 3rd level entries

print('Number of entries found: ', len(entries))

# A function that parses an entry looking for a specific key and returns its
# "value" -- that is, the text of the next child
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text  # Returns the text of the NEXT child
        if child.tag == 'key' and child.text == key :
            found = True
    return None

for entry in entries:
    if (lookup(entry, 'Track ID') is None): continue
    # Retrieving all the info from each XML entry
    title = lookup(entry, 'Name')
    album = lookup(entry, 'Album')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')
    skipped = lookup(entry, 'Skip Count')

    # Discarding the entry if any value is empty
    if title is None or album is None or artist is None or genre is None:
        continue

    print(title, album, artist, genre, length, count, rating, skipped)

    # Creating new db entries with the extracted data
    cur.execute('insert or ignore into Genre (name) values (?)', (genre,))
    cur.execute('select id from Genre where name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('insert or ignore into Artist (name) values (?)', (artist,))
    cur.execute('select id from Artist where name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''insert or ignore into Album (artist_id, title) values (?, ?)
        ''', (artist_id, album))
    cur.execute('select id from Album where title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''insert or replace into Track (title, album_id, genre_id,
        len, rating, count, skipped) values (?, ?, ?, ?, ?, ?, ?)''', (title,
        album_id, genre_id, length, rating, count, skipped))
    
    conn.commit()
    
cur.close()
