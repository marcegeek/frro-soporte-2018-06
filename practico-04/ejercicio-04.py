import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox


class EditaCiudad:
    def __init__(self, parent, ciudad=None):
        self.parent = parent
        self.top = tk.Toplevel(self.parent)
        self.top.transient(self.parent)

        if ciudad:
            self.top.title('Editando ciudad')
        else:
            self.top.title('Nueva ciudad')
        self.top.resizable(1, 0)

        self.resultado = None

        self.frame = ttk.Frame(self.top)
        self.top.columnconfigure(0, weight=1)
        self.frame.grid(sticky=tk.W + tk.E)
        self.lbl_ciudad = ttk.Label(self.frame, text='Ciudad')
        self.ciudad_var = tk.StringVar()
        self.txt_ciudad = ttk.Entry(self.frame, textvariable=self.ciudad_var)
        self.lbl_cod_postal = ttk.Label(self.frame, text='Código postal')
        self.cod_postal_var = tk.StringVar()
        self.txt_cod_postal = ttk.Entry(self.frame, textvariable=self.cod_postal_var)
        self.frame.columnconfigure(1, weight=1)
        self.lbl_ciudad.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.txt_ciudad.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        self.lbl_cod_postal.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.txt_cod_postal.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E)

        self.btn_frame = ttk.Frame(self.top)
        self.btn_frame.grid(sticky=tk.E)
        self.btn_aceptar = ttk.Button(self.btn_frame, text='Aceptar', command=self.ok)
        self.btn_cancelar = ttk.Button(self.btn_frame, text='Cancelar', command=self.cancel)
        self.btn_aceptar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btn_cancelar.pack(side=tk.LEFT, padx=5, pady=5)

        self.top.grab_set()
        self.top.protocol("WM_DELETE_WINDOW", self.cancel)
        self.txt_ciudad.focus_set()
        self.top.wait_window(self.top)

    def ok(self):
        self.resultado = self.ciudad_var.get(), self.cod_postal_var.get()
        if self.resultado and self.resultado[0] and self.resultado[1]:
            self.cancel()
        else:
            mbox.showinfo('Campos incompletos', 'Complete todos los campos', parent=self.top)

    def cancel(self):
        self.parent.focus_set()
        self.top.destroy()


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
        self.frame_acciones = ttk.Frame(self.root)
        self.frame_acciones.grid(row=0, column=1)
        self.btn_nueva_ciudad = ttk.Button(self.frame_acciones, text='Nueva ciudad', command=self.nueva_ciudad)
        self.btn_modificar = ttk.Button(self.frame_acciones, text='Modificar')
        self.btn_eliminar = ttk.Button(self.frame_acciones, text='Eliminar')
        self.btn_nueva_ciudad.grid(row=0, column=0, padx=(5, 5), pady=(5, 0), sticky=tk.W + tk.E)
        self.btn_modificar.grid(row=1, column=0, padx=(5, 5), pady=(5, 0), sticky=tk.W + tk.E)
        self.btn_eliminar.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky=tk.W + tk.E)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        self.lista_ciudades.sort()
        for c in self.lista_ciudades:
            self.tree.insert('', 'end', values=c)

    def nueva_ciudad(self):
        ed = EditaCiudad(self.root)
        c = ed.resultado
        if c and c[0] and c[1]:
            try:
                self.agregar_ciudad(c)
            except Exception as err:
                mbox.showerror('Error', str(err))

    def agregar_ciudad(self, ciudad):
        for c in self.lista_ciudades:
            if c[0] == ciudad[0] or c[1] == ciudad[1]:
                raise Exception('Ciudad o código postal repetido')
        self.lista_ciudades.append(ciudad)
        self.populate_treeview()


if __name__ == '__main__':
    c = Ciudades()
