import tkinter as tk
from tkinter import ttk


class UnitFormulaFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        # create the widgets
        self.unit_price_label = ttk.Label(self, text='Unit Price')
        self.formula_label = ttk.Label(self, text='Formula')
        self.calculated_basis_label = ttk.Label(self, text='Basis Value')

        self.unit_price_entry = ttk.Entry(self)
        self.formula_entry = ttk.Entry(self)
        self.calculated_basis_entry = ttk.Entry(self)

        self.unit_price_label.grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='we')

        self.formula_label.grid(row=1, column=0, sticky='w')
        self.formula_entry.grid(row=1, column=1, sticky='we')

        self.calculated_basis_label.grid(row=2, column=0, sticky='w')
        self.calculated_basis_entry.grid(row=2, column=1, sticky='we')
