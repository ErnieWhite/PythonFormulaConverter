import pyperclip
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


def find_multiplier(s: str) -> float:
    """finds the multiplier for the formula in s. If this cannot be done then raises a value error"""
    if len(s) < 2:
        return 0
    code = s[0].upper()
    if code == '*':
        return float(s[1:])
    elif code == 'X':
        return float(s[1:])
    elif code == '-':
        return 1 + float(s) / 100
    elif code == '+':
        return 1 + float(s) / 100
    elif code == 'D':
        return 1 / float(s[1:])
    elif code == 'G':
        return 1 / (1 - float(s[2:]) / 100)
    else:
        raise ValueError('Invalid formula: ' + s)


def find_multiplier_formula(m: float) -> str:
    return f'*{m:.6}'


def find_markup_formula(m: float) -> str:
    return f'D{1 / m:.6}'


def find_discount_formula(m: float) -> str:
    return f'{(m-1)*100:+.6}'


def find_gross_profit_formula(m: float) -> str:
    return f'GP{(1 - 1 / m) * 100:.6}'


def create_image(filepath):
    image = Image.open(filepath)
    image = image.resize((16, 16))
    return ImageTk.PhotoImage(image)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # create the Tkinter Variables to access teh data
        self.formula_value = tk.StringVar()
        self.multiplier_value = tk.StringVar()
        self.discount_value = tk.StringVar()
        self.markup_value = tk.StringVar()
        self.gross_profit_value = tk.StringVar()

        # set the windows title bar icon
        window_icon = tk.PhotoImage(file="fc.png")
        self.iconphoto(True, window_icon)

        # create the Vars
        self.formula_value = tk.StringVar()

        # create the image to be used for the copy buttons
        self.copy_image = create_image('img.png')

        # create the image to be used for the erase button
        self.erase_image = create_image('eraser.png')

        self.frame = ttk.Frame(self, padding=(10, 10, 10, 10))

        self.formula_label = ttk.Label(self.frame, text="Formula")
        self.formula_label.grid(row=0, column=0, sticky=tk.W)

        self.formula_entry = ttk.Entry(self.frame, textvariable=self.formula_value)
        self.formula_entry.grid(row=0, column=1, sticky=(tk.E, tk.W))

        self.formula_clear_button = ttk.Button(self.frame, text="Clear", command=self.formula_entry_clear, image=self.erase_image)
        self.formula_clear_button.grid(row=0, column=2, sticky=tk.E)

        multiplier_label = ttk.Label(self.frame, text="Multiplier")
        multiplier_label.grid(row=1, column=0, sticky=tk.W)

        multiplier_entry = ttk.Entry(self.frame, state=tk.DISABLED, textvariable=self.multiplier_value)
        multiplier_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        multiplier_copy_button = ttk.Button(self.frame, text="Copy", command=self.copy_multiplier_formula, image=self.copy_image)
        multiplier_copy_button.grid(row=1, column=2, sticky=tk.E)

        discount_label = ttk.Label(self.frame, text="Discount")
        discount_label.grid(row=2, column=0, sticky=tk.W)

        discount_entry = ttk.Entry(self.frame, state=tk.DISABLED, textvariable=self.discount_value)
        discount_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        discount_copy_button = ttk.Button(self.frame, text="Copy", command=self.copy_discount_formula, image=self.copy_image)
        discount_copy_button.grid(row=2, column=2, sticky=tk.E)

        markup_label = ttk.Label(self.frame, text="Markup")
        markup_label.grid(row=3, column=0, sticky=tk.W)

        markup_entry = ttk.Entry(self.frame, state=tk.DISABLED, textvariable=self.markup_value)
        markup_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        markup_copy_button = ttk.Button(self.frame, text="Copy", command=self.copy_markup_formula, image=self.copy_image)
        markup_copy_button.grid(row=3, column=2, sticky=tk.E)

        gross_profit_label = ttk.Label(self.frame, text="Gross Profit", padding=(0, 0, 5, 0))
        gross_profit_label.grid(row=4, column=0, sticky=tk.W)

        gross_profit_entry = ttk.Entry(self.frame, state=tk.DISABLED, textvariable=self.gross_profit_value)
        gross_profit_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

        gross_profit_copy_button = ttk.Button(self.frame, text="Copy", command=self.copy_gross_profit_formula, image=self.copy_image)
        gross_profit_copy_button.grid(row=4, column=2, sticky=tk.E)

        self.frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.frame.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.formula_entry.bind("<KeyRelease>", self.do_something)

    def do_something(self, event):
        try:
            formula = self.formula_value.get().upper()
            multiplier = find_multiplier(formula)

            multiplier_formula = find_multiplier_formula(multiplier)
            self.multiplier_value.set(multiplier_formula)

            markup_formula = find_markup_formula(multiplier)
            self.markup_value.set(markup_formula)

            discount_formula = find_discount_formula(multiplier)
            self.discount_value.set(discount_formula)

            gross_profit_formula = find_gross_profit_formula(multiplier)
            self.gross_profit_value.set(gross_profit_formula)
        except ZeroDivisionError:
            self.clear_formulas()
        except TypeError:
            self.clear_formulas()
        except ValueError:
            self.clear_formulas()

    def copy_multiplier_formula(self):
        pyperclip.copy(self.multiplier_value.get())

    def copy_discount_formula(self):
        pyperclip.copy(self.discount_value.get())

    def copy_gross_profit_formula(self):
        pyperclip.copy(self.gross_profit_value.get())

    def copy_markup_formula(self):
        pyperclip.copy(self.markup_value.get())

    def formula_entry_clear(self):
        self.formula_value.set("")
        self.clear_formulas()

    def clear_formulas(self):
        self.multiplier_value.set('')
        self.discount_value.set('')
        self.markup_value.set('')
        self.gross_profit_value.set('')


if __name__ == "__main__":
    app = App()
    app.mainloop()
