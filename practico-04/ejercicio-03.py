import tkinter as tk
import tkinter.ttk as ttk


class Ciudades():
    def __init__(self):
        self.root = tk.Tk()
        self.configure_gui()
        self.create_widgets()
        self.root.mainloop()

    def configure_gui(self):
        self.root.title('Listado de ciudades')
        self.root.geometry('500x300')

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.tree = ttk.Treeview(self.frame, columns=('ciudad', 'cod_postal'))
        self.tree['show'] = 'headings'  # no mostrar columna vacía
        self.tree.heading('ciudad', text='Ciudad')
        self.tree.heading('cod_postal', text='Código postal')
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.tree.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.tree.insert('', 'end', values=('Rosario', '2000'))  # FIXME ciudad hardcodeada


if __name__ == '__main__':
    c = Ciudades()
