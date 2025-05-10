import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS ТОВАРЫ(
    код_товара INTEGER,
    наименование_товара TEXT,
    наименование_магазина TEXT,
    заявки_магазина TEXT,
    кол_во_товара_на_скалде INTEGER,
    единиицы_измерения INTEGER,
    оптовая_цена INTEGER

    )''')

    cur.execute('''INSERT INTO ТОВАРЫ VALUES(1,"апельсины","пятерочка","задолженности_поставщиков",1,2,36)''')
