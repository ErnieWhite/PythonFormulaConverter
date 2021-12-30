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


class FormulaEntry(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.textvariable = tk.StringVar()
        self.image = create_image('eraser.png')
        self.label = ttk.Label(self, text="Formula", width=11)
        self.label.grid(row=0, column=0, sticky=tk.W)

        self.entry = ttk.Entry(self, textvariable=self.textvariable)
        self.entry.grid(row=0, column=1, sticky=(tk.E, tk.W))

        self.clear_button = ttk.Button(self, text="Clear", command=lambda: app.formula_entry_clear(), image=self.image)
        self.clear_button.grid(row=0, column=2, sticky=tk.E)

        self.columnconfigure(1, weight=1)
        self.grid(row=0, column=0, sticky=(tk.W, tk.E))

    def get(self):
        self.textvariable.get()

    def set(self, v):
        self.textvariable.set(v)


class FormulaDisplay(ttk.Frame):
    def __init__(self, container, text: str, row=0, column=0):
        super().__init__(container)
        # create the image to be used for the copy buttons
        self.image = create_image('img.png')
        self.textvariable = tk.StringVar()
        self.label = ttk.Label(self, text=text, width=11)
        self.label.grid(row=0, column=0, sticky=tk.W)

        self.entry = ttk.Entry(self, state=tk.DISABLED, textvariable=self.textvariable)
        self.entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.copy_button = ttk.Button(self, text="Copy", command=lambda: pyperclip.copy(self.textvariable.get()), image=self.image)
        self.copy_button.grid(row=0, column=2, sticky=tk.E)
        self.columnconfigure(1, weight=1)
        self.grid(row=row, column=column, sticky=(tk.W, tk.E))

    def get(self):
        self.textvariable.get()

    def set(self, v):
        self.textvariable.set(v)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        window_icon = tk.PhotoImage(file="fc.png")
        self.iconphoto(True, window_icon)
        self.title("Formula Converter")

        self.frame = ttk.Frame(self, padding=(10, 10, 10, 10))

        self.formula_entry = FormulaEntry(self.frame)
        self.multiplier_display = FormulaDisplay(self.frame, text="Multiplier", row=1, column=0)
        self.discount_display = FormulaDisplay(self.frame, text="Discount", row=2, column=0)
        self.markup_display = FormulaDisplay(self.frame, text="Markup", row=3, column=0)
        self.gross_profit_display = FormulaDisplay(self.frame, text="Gross Profit", row=4, column=0)

        self.frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.frame.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.formula_entry.entry.bind("<KeyRelease>", self.do_something)

    def do_something(self, event):
        try:
            formula = self.formula_entry.entry.get().upper()
            multiplier = find_multiplier(formula)

            multiplier_formula = find_multiplier_formula(multiplier)
            self.multiplier_display.set(multiplier_formula)

            markup_formula = find_markup_formula(multiplier)
            self.markup_display.set(markup_formula)

            discount_formula = find_discount_formula(multiplier)
            self.discount_display.set(discount_formula)

            gross_profit_formula = find_gross_profit_formula(multiplier)
            self.gross_profit_display.set(gross_profit_formula)
        except ZeroDivisionError:
            self.clear_displays()
        except TypeError:
            self.clear_displays()
        except ValueError:
            self.clear_displays()

    def formula_entry_clear(self):
        self.formula_entry.set("")
        self.clear_displays()

    def clear_displays(self):
        self.multiplier_display.set('')
        self.discount_display.set('')
        self.markup_display.set('')
        self.gross_profit_display.set('')


if __name__ == "__main__":
    app = App()
    app.mainloop()
