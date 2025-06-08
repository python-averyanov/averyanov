import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS PRODUCTS(
    item_id INTEGER,
    item_name TEXT,
    store_name TEXT,
    post_store TEXT,
    how_many_in_store INTEGER,
    units INTEGER,
    wholesale INTEGER
    )''')
    # for i in range(10):
    #     cur.execute(f'''INSERT INTO PRODUCTS VALUES({i},"апельсины","пятерочка","задолженности_поставщиков",{2+i},2,{36+i})''')
    # cur.execute('''SELECT * FROM PRODUCTS WHERE item_id > 5''')
    # cur.execute('''DELETE FROM PRODUCTS WHERE item_id > -1''')
    # cur.execute('''UPDATE PRODUCTS SET store_name = 'МАГНИТ' WHERE item_id > 5 or wholesale > 39''')

