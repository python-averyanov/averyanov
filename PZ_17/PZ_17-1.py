import tkinter as tk
from tkinter import messagebox

def register():
    if not terms_var.get():
        messagebox.showwarning("Ошибка", "Вы должны согласиться с условиями")
        return
    messagebox.showinfo("Регистрация", "Вы успешно зарегистрированы!")

root = tk.Tk()
root.title("Register")
root.configure(bg="black")
root.geometry("400x500")

tk.Label(root, text="Elegant Login and Register forms", font=("Segoe Script", 16, "bold"), bg="#2c2f36", fg="white").pack(pady=10)

form_frame = tk.Frame(root, bg="#1f2125")
form_frame.pack(padx=20, pady=10, fill="both", expand=True)


tk.Label(form_frame, text="👤 Register", font=("Arial", 14, "bold"), bg="#1f2125", fg="white").pack(pady=15)


entries = {}
fields = ["First Name", "Last Name", "Email Address", "User Name", "Password", "Confirm Password"]
for field in fields:
    show = "*" if "Password" in field else ""
    entry = tk.Entry(form_frame, font=("Arial", 12), show=show, bg="#2c2f36", fg="white", insertbackground='white')
    entry.insert(0, field)
    entry.bind("<FocusIn>", lambda e, default=field: e.widget.delete(0, tk.END) if e.widget.get() == default else None)
    entry.pack(pady=5, ipady=5, ipadx=5, fill="x", padx=30)
    entries[field] = entry

terms_var = tk.BooleanVar()
tk.Checkbutton(form_frame, text="I agree to the Terms and Conditions", variable=terms_var,
               bg="#1f2125", fg="white", selectcolor="#1f2125").pack(pady=10)

tk.Button(form_frame, text="Sign Me Up >", command=register, bg="#66cc33", fg="white",
          font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=10)

root.mainloop()
