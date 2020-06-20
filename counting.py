import sqlite3

db_connection = sqlite3.connect('emaildb.sqlite')
a_cursor = db_connection.cursor()

a_cursor.execute('DROP TABLE IF EXISTS Counts')
a_cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

for a_new_line in requested_file :
    if not a_new_line.startswith('From: ') : continue
    else :
        a_word_list = a_new_line.split()
        a_word = a_word_list[1].split('@')
        an_org = a_word[1]

        a_cursor.execute('''
            SELECT count FROM Counts WHERE org = ?''', (an_org,))

        a_possible_item = a_cursor.fetchone()

        if a_possible_item is None :
            a_cursor.execute('''
                INSERT INTO Counts (org, count) VALUES (?, 1)''', (an_org,))
        else :
            a_cursor.execute('''
                UPDATE Counts SET count = count+1 WHERE org = ?''', (an_org,))

        db_connection.commit()

the_results = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for a_row in a_cursor.execute(the_results):
    print(str(a_row[0]), a_row[1])

a_cursor.close()
