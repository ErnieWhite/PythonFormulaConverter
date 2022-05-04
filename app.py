import model
import view
import controller
from tkinter import Tk


if __name__ == "__main__":
    app = Tk()
    model = model.Model()
    view = view.View(master=app)

    controller.Controller(master=app, model=model, view=view)

    app.mainloop()
