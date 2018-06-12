from operator import attrgetter

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox

from practico_06.capa_negocio import Socio, NegocioSocio, DniRepetido, LongitudInvalida, MaximoAlcanzado


class PresentacionSocios:
    def __init__(self):
        self.ns = NegocioSocio()
        self.root = tk.Tk()
        self.configure_gui()
        self.create_widgets()
        self.populate_treeview()
        self.root.mainloop()

    def configure_gui(self):
        self.root.title('ABM de Socios')
        self.root.geometry('1000x600')

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding=10)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.frame.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.tree = ttk.Treeview(self.frame, columns=('id', 'nombre', 'apellido', 'dni'))
        self.tree['show'] = 'headings'  # no mostrar columna vacía
        self.tree.heading('id', text='Id')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('apellido', text='Apellido')
        self.tree.heading('dni', text='DNI')
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.tree.grid(sticky=tk.W + tk.E + tk.N + tk.S)
        self.frame_acciones = ttk.Frame(self.root, padding=(10, 0, 0, 10))
        self.frame_acciones.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.btn_alta = ttk.Button(self.frame_acciones, text='Alta', command=None)
        self.btn_modificar = ttk.Button(self.frame_acciones, text='Modificar', command=None)
        self.btn_baja = ttk.Button(self.frame_acciones, text='Baja', command=self.baja_socio)
        self.btn_alta.pack(side=tk.LEFT, padx=(0, 5))
        self.btn_baja.pack(side=tk.LEFT, padx=(0, 5))
        self.btn_modificar.pack(side=tk.LEFT)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        lista_socios = self.ns.todos()
        lista_socios.sort(key=attrgetter('nombre', 'apellido'))  # ordena por nombre y apellido
        for s in lista_socios:
            self.tree.insert('', 'end', values=(s.id, s.nombre, s.apellido, s.dni))

    def baja_socio(self):
        item_id = self.tree.focus()
        if item_id:
            baja = mbox.askyesno('Confirme baja de socio', '¿Realmente desea dar de baja?', default='no',
                                 parent=self.root)
            if baja:
                id_socio = self.tree.item(item_id, 'values')[0]
                self.ns.baja(id_socio)
                self.populate_treeview()


if __name__ == '__main__':
    p = PresentacionSocios()
