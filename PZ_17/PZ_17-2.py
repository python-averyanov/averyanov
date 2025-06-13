import tkinter as tk

def calculate():
    try:
        x = float(entry_x.get())
        a = float(entry_a.get())
        y = float(entry_y.get())
        cost_per_kg = a / x
        total_cost = cost_per_kg * y
        result_var.set(f"1 кг = {cost_per_kg:.2f} руб.\n{y} кг = {total_cost:.2f} руб.")
    except ValueError:
        result_var.set("Пожалуйста, введите числовые значения.")

root = tk.Tk()
root.title("Стоимость конфет")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

tk.Label(root, text="X кг:", bg="#f0f0f0").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Label(root, text="Цена A (руб):", bg="#f0f0f0").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Y кг:", bg="#f0f0f0").pack()
entry_y = tk.Entry(root)
entry_y.pack()

tk.Button(root, text="Рассчитать", command=calculate).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, bg="#f0f0f0", fg="blue").pack()

root.mainloop()
