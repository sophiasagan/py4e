import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Track (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT UNIQUE,
    album_id    INTEGER,
    artist_id   INTEGER,
    genre_id    INTEGER
);
CREATE TABLE Artist (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name        TEXT UNIQUE
);
CREATE TABLE Album (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT UNIQUE,
    artist_id   INTEGER
);
CREATE TABLE Genre (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name        TEXT UNIQUE
);
''')



fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, genre)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    a_cursor.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre,) )
    a_cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre_text,) )
    genre_id = a_cursor.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, artist_id, album_id, genre_id)
        VALUES ( ?, ?, ?, ?)''',
        (name, artist_id, album_id, genre_id) )

    conn.commit()
