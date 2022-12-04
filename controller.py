import tkinter as tk
import re


class Controller:
    def __init__(self, master, model, view):
        self.model = model
        self.view = view
        self.master = master

        self.init_unit_base_frame()
        self.init_unit_formula_frame()
        self.add_unit_base_event_handlers()
        self.add_unit_formula_event_handlers()

    def init_unit_base_frame(self):
        float_vcmd = (self.master.register(self.validate_number), '%P')
        ivcmd = (self.master.register(self.on_invalid),)
        self.view.unit_basis_frame.unit_price_entry.configure(
            validate='key',
            validatecommand=float_vcmd,
            invalidcommand=ivcmd,
            textvariable=self.model.ub_unit_price_var,
        )
        self.view.unit_basis_frame.basis_value_entry.configure(
            validate='key',
            validatecommand=float_vcmd,
            invalidcommand=ivcmd,
            textvariable=self.model.ub_basis_value_var,
        )

    def init_unit_formula_frame(self):
        formula_vcmd = (self.master.register(self.validate_formula), '%P')
        float_vcmd = (self.master.register(self.validate_number), '%P')
        ivcmd = (self.master.register(self.on_invalid),)
        self.view.unit_formula_frame.unit_price_entry.configure(
            validate='key',
            validatecommand=float_vcmd,
            invalidcommand=ivcmd,
            textvariable=self.model.uf_formula_var,
        )
        self.view.unit_formula_frame.formula_entry.configure(
            validate='key',
            validatecommand=formula_vcmd,
            invalidcommand=ivcmd,
            textvariable=self.model.uf_unit_price_var,
        )
        self.view.unit_basis_frame.multiplier_formula_entry.configure(
            textvariable=self.model.multilier_formula_var,
        )
        self.view.unit_basis_frame.discount_formula_entry.configure(
            textvariable=self.model.discount_formula_var,
        )
        self.view.unit_basis_frame.markup_formula_entry.configure(
            textvariable=self.model.markup_formula_var,
        )
        self.view.unit_basis_frame.gross_profit_formula_entry.configure(
            textvariable=self.model.gross_profit_formula_var,
        )

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

    def add_unit_base_event_handlers(self):
        self.view.unit_basis_frame.unit_price_entry.bind('<KeyRelease>', self.calculate_formulas)
        self.view.unit_basis_frame.basis_value_entry.bind('KeyRelease>', self.calcualte_formulas)

    def add_unit_formula_event_handlers(self):
        pass

    def calculate_formulas(self):
        if self.model.ub_unit_price_var is not None and self.model.ub_basis_value_var is not None:
            multiplier = self.model.ub_unit_price_var / self.model.ub_basis_value_var
