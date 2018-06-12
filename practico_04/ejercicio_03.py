import tkinter as tk
import tkinter.ttk as ttk


class Ciudades():
    def __init__(self):
        self.lista_ciudades = [('Rosario', '2000'), ('Buenos Aires', '1073'), ('Santa Fe', '3000'),
                               ('Córdoba', '1000'), ('Salta', '5000')]
        self.root = tk.Tk()
        self.configure_gui()
        self.create_widgets()
        self.populate_treeview()
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

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        self.lista_ciudades.sort()
        for c in self.lista_ciudades:
            self.tree.insert('', 'end', values=c)


if __name__ == '__main__':
    c = Ciudades()
