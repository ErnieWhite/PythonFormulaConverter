from tkinter import ttk


class View(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # create the entry widgets
        self.basis_value_entry = ttk.Entry(self)
        self.formula_entry = ttk.Entry(self)
        self.unit_price_entry = ttk.Entry(self)
        self.number_decimals_combo = ttk.Combobox(self)
        self.calculated_basis_value_entry = ttk.Entry(self)

        self.multiplier_formula_entry = ttk.Entry(self)
        self.discount_formula_entry = ttk.Entry(self)
        self.markup_formula_entry = ttk.Entry(self)
        self.gross_profit_formula_entry = ttk.Entry(self)

        # row 0
        ttk.Label(self, text="Unit Price").grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='ew')
        self.multiplier_formula_entry.grid(row=0, column=2, sticky='ew')
        # row 1
        ttk.Label(self, text="Basis Value").grid(row=1, column=0, sticky='w')
        self.basis_value_entry.grid(row=1, column=1, sticky='ew')
        self.discount_formula_entry.grid(row=1, column=2, sticky='ew')
        # row 2
        ttk.Label(self, text="Decimals").grid(row=2, column=0, sticky='w')
        self.number_decimals_combo.grid(row=2, column=1, sticky='ew')
        self.markup_formula_entry.grid(row=2, column=2, sticky='ew')
        # row 3
        ttk.Label(self, text="Calculated Basis").grid(row=3, column=0, sticky='w')
        self.calculated_basis_value_entry.grid(row=3, column=1, sticky='ew')
        self.gross_profit_formula_entry.grid(row=3, column=2, sticky='ew')

        self.pack()
