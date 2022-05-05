import tkinter as tk
import re


class Controller:
    def __init__(self, master, model, view):
        self.model = model
        self.view = view
        self.master = master

        self.init_unit_base_frame()
        self.init_unit_formula_frame()

    def init_unit_base_frame(self):
        float_vcmd = (self.master.register(self.validate_number), '%P')
        ivcmd = (self.master.register(self.on_invalid),)
        self.view.unit_basis_frame.unit_price_entry.configure(validate='key', validatecommand=float_vcmd, invalidcommand=ivcmd)
        self.view.unit_basis_frame.basis_value_entry.configure(validate='key', validatecommand=float_vcmd, invalidcommand=ivcmd)

    def init_unit_formula_frame(self):
        formula_vcmd = (self.master.register(self.validate_formula), '%P')
        float_vcmd = (self.master.register(self.validate_number), '%P')
        ivcmd = (self.master.register(self.on_invalid),)
        self.view.unit_formula_frame.unit_price_entry.configure(validate='key', validatecommand=float_vcmd, invalidcommand=ivcmd)
        self.view.unit_formula_frame.formula_entry.configure(validate='key', validatecommand=formula_vcmd, invalidcommand=ivcmd)

    @staticmethod
    def validate_number(value):
        if re.fullmatch(r"^\$?\d*\.?\d*$", value) is None:
            return False
        else:
            return True

    @staticmethod
    def validate_formula(value):
        if re.fullmatch(r'^(\*|X|-|\+|D|GP)\d*\.?\d*$', value, flags=re.IGNORECASE) is not None or value == '':
            return True
        else:
            return False

    def on_invalid(self):
        print('invalid')
        self.master.bell()
        self.master.bell()
