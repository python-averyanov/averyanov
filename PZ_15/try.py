import sqlite3
conn = sqlite3.connect("teaher.db")
cur = conn.cursor()
cur.execute('''
        CREATE TABLE IF NOT EXISTS teachers(
            table_id INTEGER PRIMARY KEY,
            last_name TEXT NOT NULL,
            stage INTRGER,
            heavy INTEGER 
        )
''')
conn.commit()

cur.execute('''
    INSERT INTO teachers (table_id, last_name, stage, heavy) VALUES (1, 'Аверьянов Г.С.', 1, 15)
''')

cur.execute('''
    INSERT INTO teachers (table_id, last_name, stage, heavy) VALUES (2, 'петров У. Г', 0, 19)
''')

cur.execute('''
    INSERT INTO teachers (table_id, last_name, stage, heavy) VALUES (3, 'Иванов В. Б.', 1, 100)
''')
conn.commit()



cur.execute('''UPDATE teachers set heavy = 12 where stage > 0''')



# cur.execute('''drop table teachers''')
conn.commit()
