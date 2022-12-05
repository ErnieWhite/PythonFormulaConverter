import model
import view
import controller
from tkinter import Tk
from tkinter import ttk




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
