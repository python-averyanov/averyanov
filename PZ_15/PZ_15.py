# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
# товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
# товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.

import sqlite3


def connect_db():
    conn = sqlite3.connect("saper.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            store_name TEXT NOT NULL,
            store_requests INTEGER,
            stock_quantity INTEGER,
            unit TEXT,
            wholesale_price REAL
        )
    ''')
    conn.commit()
    return conn


def insert(conn):
    data = [
        (1, 'Milk', 'Magnit', 100, 50, 'liters', 35.0),
        (2, 'Bread', 'Pyaterochka', 150, 80, 'pcs', 20.5),
        (3, 'Sugar', 'Lenta', 75, 100, 'kg', 45.0),
        (4, 'Flour', 'Okey', 60, 40, 'kg', 33.0),
        (5, 'Oil', 'Diksi', 90, 30, 'liters', 78.0),
        (6, 'Eggs', 'Victoria', 120, 90, 'dozen', 50.0),
        (7, 'Rice', 'Auchan', 70, 60, 'kg', 48.0),
        (8, 'Buckwheat', 'Carousel', 55, 45, 'kg', 60.0),
        (9, 'Salt', 'Magnit', 40, 100, 'kg', 18.0),
        (10, 'Tea', 'Pyaterochka', 30, 25, 'pack', 85.0)
    ]
    try:
        cur = conn.cursor()
        cur.executemany('''
            INSERT OR IGNORE INTO Products
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")


def search_products(conn):
    cur = conn.cursor()
    print("1. По имени товара\n2. По магазину\n3. По количеству на складе < заданного")
    choice = input("Выберите тип поиска: ")

    if choice == "1":
        name = input("Введите название товара: ")
        cur.execute("SELECT * FROM Products WHERE product_name = ?", (name,))
    elif choice == "2":
        store = input("Введите название магазина: ")
        cur.execute("SELECT * FROM Products WHERE store_name = ?", (store,))
    elif choice == "3":
        qty = int(input("Введите пороговое количество: "))
        cur.execute("SELECT * FROM Products WHERE stock_quantity < ?", (qty,))
    else:
        print("Неверный выбор.")
        return

    for r in cur.fetchall():
        print(r)


def delete_product(conn):
    cur = conn.cursor()
    print("1. По ID\n2. По имени товара\n3. По магазину")
    choice = input("Выберите тип удаления: ")

    try:
        if choice == "1":
            pid = int(input("Введите ID товара: "))
            cur.execute("DELETE FROM Products WHERE product_id = ?", (pid,))
        elif choice == "2":
            name = input("Введите название товара: ")
            cur.execute("DELETE FROM Products WHERE product_name = ?", (name,))
        elif choice == "3":
            store = input("Введите магазин: ")
            cur.execute("DELETE FROM Products WHERE store_name = ?", (store,))
        else:
            print("Неверный выбор.")
            return

        conn.commit()
        print("Удаление выполнено.")
    except sqlite3.Error as e:
        print(f"Ошибка удаления: {e}")


def update_product(conn):
    cur = conn.cursor()
    print("1. Изменить цену по ID\n2. Изменить количество по имени\n3. Изменить заявки по магазину")
    choice = input("Выберите тип редактирования: ")

    try:
        if choice == "1":
            pid = int(input("Введите ID товара: "))
            new_price = float(input("Новая цена: "))
            cur.execute("UPDATE Products SET wholesale_price = ? WHERE product_id = ?", (new_price, pid))
        elif choice == "2":
            name = input("Введите название товара: ")
            new_qty = int(input("Новое количество: "))
            cur.execute("UPDATE Products SET stock_quantity = ? WHERE product_name = ?", (new_qty, name))
        elif choice == "3":
            store = input("Введите магазин: ")
            new_requests = int(input("Новое количество заявок: "))
            cur.execute("UPDATE Products SET store_requests = ? WHERE store_name = ?", (new_requests, store))
        else:
            print("Неверный выбор.")
            return

        conn.commit()
        print("Редактирование выполнено.")
    except sqlite3.Error as e:
        print(f"Ошибка редактирования: {e}")


def show_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products")
    for row in cur.fetchall():
        print(row)


def main():
    conn = connect_db()
    insert(conn)

    while True:
        print("\n1. Показать все\n2. Поиск\n3. Удаление\n4. Редактирование\n5. Выход")
        action = input("Выберите действие: ")

        if action == "1":
            show_all(conn)
        elif action == "2":
            search_products(conn)
        elif action == "3":
            delete_product(conn)
        elif action == "4":
            update_product(conn)
        elif action == "5":
            print("Завершение программы.")
            break
        else:
            print("Неверный выбор.")

    conn.close()


if __name__ == "__main__":
    main()
