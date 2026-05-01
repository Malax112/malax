import tkinter as tk
import random

class CodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rust password generator")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        
        self.generated_codes = set()

        
        self.current_code = None

        self.init_ui()

    def init_ui(self):
        self.code_label = tk.Label(
            self.root,
            text="Press Generate to create a new password",
            font=("Arial", 12),
            wraplength=280
        )
        self.code_label.pack(pady=20)

        generate_button = tk.Button(
            self.root,
            text="Generate",
            command=self.generate_code,
            font=("Arial", 10),
            width=15
        )
        generate_button.pack(pady=5)

        copy_button = tk.Button(
            self.root,
            text="Copy",
            command=self.copy_to_clipboard,
            font=("Arial", 10),
            width=15
        )
        copy_button.pack(pady=5)

    def generate_code(self):
        """Генерирует уникальный четырёхзначный код"""
        while True:
            code = random.randint(1000, 9999)

            if code not in self.generated_codes:
                self.generated_codes.add(code)
                self.current_code = code
                self.code_label.config(text=f"Password: {code}")
                break

    def copy_to_clipboard(self):
        """Копирует текущий код в буфер обмена"""
        if self.current_code is not None:
            self.root.clipboard_clear()
            self.root.clipboard_append(str(self.current_code))
            self.code_label.config(fg="green")
            self.root.after(1000, lambda: self.code_label.config(fg="black"))

def main():
    root = tk.Tk()
    app = CodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
