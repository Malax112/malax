import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # библиотека для копирования в буфер обмена

def generate_password():
    """Генерирует 8‑значный пароль из случайных символов."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(20))
    password_entry.delete(0, tk.END)  # очищаем поле
    password_entry.insert(0, password)  # вставляем новый пароль

def copy_password():
    """Копирует сгенерированный пароль в буфер обмена."""
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Успех", "Пароль скопирован в буфер обмена!")
    else:
        messagebox.showwarning("Внимание", "Сначала сгенерируйте пароль!")

# Создаём главное окно
root = tk.Tk()
root.title("Password generator")
root.geometry("300x120")
root.resizable(False, False)  # фиксированный размер окна

# Поле для отображения пароля
password_entry = tk.Entry(root, width=30, font=("Arial", 10), justify="center")
password_entry.pack(pady=10)

# Кнопка генерации пароля
generate_btn = tk.Button(root, text="Generate", command=generate_password, width=15, height=2)
generate_btn.pack(pady=5)

# Кнопка копирования пароля
copy_btn = tk.Button(root, text="Copy", command=copy_password, width=15, height=2)
copy_btn.pack(pady=5)

# Запускаем главный цикл приложения
root.mainloop()
