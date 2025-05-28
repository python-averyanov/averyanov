import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS ТОВАРЫ(
    item_id INTEGER,
    item_name TEXT,
    store_name TEXT,
    post_store TEXT,
    how_many_in_store INTEGER,
    единиицы_измерения INTEGER,
    оптовая_цена INTEGER

    )''')
    cur.execute('''INSERT INTO ТОВАРЫ VALUES(1,"апельсины","пятерочка","задолженности_поставщиков",1,2,36)''')
