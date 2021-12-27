import pyperclip
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


def find_multiplier(s: str) -> float:
    """finds the multiplier for the formula in s. If this cannot be done then raises a value error"""
    if len(s) < 2:
        return 0
    match s[0].upper():
        case '*':
            return float(s[1:])
        case 'X':
            return float(s[1:])
        case '-':
            return 1 + float(s) / 100
        case '+':
            return 1 + float(s) / 100
        case 'D':
            return 1 / float(s[1:])
        case 'G':
            return 1 / (1 - float(s[2:]) / 100)
        case _:
            raise ValueError('Invalid formula: ' + s)


def clear_formulas():
    multiplier_value.set('')
    discount_value.set('')
    markup_value.set('')
    gross_profit_value.set('')


def find_multiplier_formula(m: float) -> str:
    return f'*{m:.6}'


def find_markup_formula(m: float) -> str:
    return f'D{1 / m:.6}'


def find_discount_formula(m: float) -> str:
    return f'{(m-1)*100:+.6}'


def find_gross_profit_formula(m: float) -> str:
    return f'GP{(1 - 1 / m) * 100:.6}'


def do_something(event):
    try:
        formula = formula_value.get().upper()
        multiplier = find_multiplier(formula)

        multiplier_formula = find_multiplier_formula(multiplier)
        multiplier_value.set(multiplier_formula)

        markup_formula = find_markup_formula(multiplier)
        markup_value.set(markup_formula)

        discount_formula = find_discount_formula(multiplier)
        discount_value.set(discount_formula)

        gross_profit_formula = find_gross_profit_formula(multiplier)
        gross_profit_value.set(gross_profit_formula)
    except ZeroDivisionError:
        clear_formulas()
    except TypeError:
        clear_formulas()
    except ValueError:
        clear_formulas()


def copy_multiplier_formula():
    pyperclip.copy(multiplier_value.get())


def copy_discount_formula():
    pyperclip.copy(discount_value.get())


def copy_gross_profit_formula():
    pyperclip.copy(gross_profit_value.get())


def copy_markup_formula():
    pyperclip.copy(markup_value.get())


def formula_entry_clear():
    formula_value.set("")
    clear_formulas()


window = tk.Tk()
window.title('Formula Converter')
icon = tk.PhotoImage(file="fc.png")
copy_image = Image.open('img.png')
copy_image = copy_image.resize((16, 16), resample=2)
copy_icon = ImageTk.PhotoImage(copy_image)
erase_image = Image.open('eraser.png')
erase_image = erase_image.resize((16,16), resample=2)
erase_icon = ImageTk.PhotoImage(erase_image)
window.iconphoto(True, icon)

formula_value = tk.StringVar()
multiplier_value = tk.StringVar()
discount_value = tk.StringVar()
markup_value = tk.StringVar()
gross_profit_value = tk.StringVar()

frame = ttk.Frame(window, padding=(10, 10, 10, 10))

formula_label = ttk.Label(frame, text="Formula")
formula_label.grid(row=0, column=0, sticky=tk.W)

formula_entry = ttk.Entry(frame, textvariable=formula_value)
formula_entry.grid(row=0, column=1, sticky=(tk.E, tk.W))

formula_clear_button = ttk.Button(frame, text="Clear", command=formula_entry_clear, image=erase_icon)
formula_clear_button.grid(row=0, column=2, sticky=(tk.E))

multiplier_label = ttk.Label(frame, text="Multiplier")
multiplier_label.grid(row=1, column=0, sticky=tk.W)

multiplier_entry = ttk.Entry(frame, state=tk.DISABLED, textvariable=multiplier_value)
multiplier_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

multiplier_copy_button = ttk.Button(frame, text="Copy", command=copy_multiplier_formula, image=copy_icon)
multiplier_copy_button.grid(row=1, column=2, sticky=tk.E)

discount_label = ttk.Label(frame, text="Discount")
discount_label.grid(row=2, column=0, sticky=tk.W)

discount_entry = ttk.Entry(frame, state=tk.DISABLED, textvariable=discount_value)
discount_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

discount_copy_button = ttk.Button(frame, text="Copy", command=copy_discount_formula, image=copy_icon)
discount_copy_button.grid(row=2, column=2, sticky=tk.E)

markup_label = ttk.Label(frame, text="Markup")
markup_label.grid(row=3, column=0, sticky=tk.W)

markup_entry = ttk.Entry(frame, state=tk.DISABLED, textvariable=markup_value)
markup_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

markup_copy_button = ttk.Button(frame, text="Copy", command=copy_markup_formula, image=copy_icon)
markup_copy_button.grid(row=3, column=2, sticky=tk.E)

gross_profit_label = ttk.Label(frame, text="Gross Profit", padding=(0, 0, 5, 0))
gross_profit_label.grid(row=4, column=0, sticky=tk.W)

gross_profit_entry = ttk.Entry(frame, state=tk.DISABLED, textvariable=gross_profit_value)
gross_profit_entry.grid(row=4, column=1, sticky=(tk.W, tk.E))

gross_profit_copy_button = ttk.Button(frame, text="Copy", command=copy_gross_profit_formula, image=copy_icon)
gross_profit_copy_button.grid(row=4, column=2, sticky=tk.E)

frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
frame.columnconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

formula_entry.bind("<KeyRelease>", do_something)

window.mainloop()
