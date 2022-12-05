import tkinter as tk
from tkinter import ttk


class UnitBasisFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create the widgets
        self.unit_price_label = ttk.Label(self, text='Unit Price')
        self.basis_value_label = ttk.Label(self, text='Basis Value')
        self.decimals_label = ttk.Label(self, text='Decimals')

        self.unit_price_entry = ttk.Entry(self)
        self.basis_value_entry = ttk.Entry(self)
        self.decimals_combo = ttk.Combobox(
            self,
            values=('Auto', '1', '2', '3', '4', '5', '6'),
        )
        self.decimals_combo.set('Auto')

        self.multiplier_formula_entry = ttk.Entry(self)
        self.discount_formula_entry = ttk.Entry(self)
        self.markup_formula_entry = ttk.Entry(self)
        self.gross_profit_formula_entry = ttk.Entry(self)

        self.unit_price_label.grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='ew')
        self.multiplier_formula_entry.grid(row=0, column=2, sticky='ew')

        self.basis_value_label.grid(row=1, column=0, sticky='w')
        self.basis_value_entry.grid(row=1, column=1, sticky='ew')
        self.discount_formula_entry.grid(row=1, column=2, sticky='ew')

        self.decimals_label.grid(row=2, column=0, sticky='w')
        self.decimals_combo.grid(row=2, column=1, sticky='ew')
        self.markup_formula_entry.grid(row=2, column=2, sticky='ew')

        self.gross_profit_formula_entry.grid(row=3, column=2, sticky='ew')

        self.pack()


if __name__ == '__main__':
    root = tk.Tk()

    frame = UnitBasisFrame(root)

    root.mainloop()
