import model
import view
import controller
from tkinter import Tk
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


class View(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create the container to hold the frames
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(pady=10, expand=True)

        self.unit_basis_frame = UnitBasisFrame(self)
        self.unit_formula_frame = UnitFormulaFrame(self)

        self.unit_basis_frame.pack(fill='both', expand=True)
        self.unit_formula_frame.pack(fill='both', expand=True)

        self.tabs.add(self.unit_basis_frame, text='Unit Price/Basis Value')
        self.tabs.add(self.unit_formula_frame, text='Unit Price/Formula')

        self.pack()


if __name__ == "__main__":
    app = Tk()
    app.title('Special Calculator')
    app.resizable(False, False)
    model = model.Model()
    view = view.View(master=app)

    controller.Controller(master=app, model=model, view=view)

    app.mainloop()
