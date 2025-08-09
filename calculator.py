import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("sqrt", 5, 1), ("^", 5, 2), ("log", 5, 3)
        ]

        for (text, row, col) in buttons:
            if text == "=":
                tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=self.calculate).grid(row=row, column=col)
            elif text == "C":
                tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=self.clear).grid(row=row, column=col)
            elif text == "sqrt":
                tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=self.sqrt).grid(row=row, column=col)
            elif text == "^":
                tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda: self.append("**")).grid(row=row, column=col)
            elif text == "log":
                tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=self.log).grid(row=row, column=col)
            else:
                tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: self.append(t)).grid(row=row, column=col)

    def append(self, value):
        self.expression += value
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

    def sqrt(self):
        try:
            result = math.sqrt(float(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

    def log(self):
        try:
            result = math.log10(float(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = AdvancedCalculator(root)
    root.mainloop()