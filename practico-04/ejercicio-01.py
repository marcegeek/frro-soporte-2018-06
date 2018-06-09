# Hacer un formulario tkinter que es una calculadora:
# Tiene 2 entry para ingresar los valores V1 y V2
# y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
# que al cliquearlos muestra el resultado de aplicar el operador respectivo en los V1 y V2.

import tkinter as tk
import tkinter.messagebox as mbox


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.configure_gui()
        self.create_widgets()
        self.root.mainloop()

    def configure_gui(self):
        self.root.title('Calculadora')
        self.root.geometry('500x100')
        self.root.resizable(1, 1)

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame.grid(column=0, row=0, padx=(5, 5), pady=(5, 5),
                        sticky=tk.S + tk.E + tk.N + tk.W)
        self.lbl_v1 = tk.Label(self.frame, text='Primer operando')
        self.lbl_v2 = tk.Label(self.frame, text='Segundo operando')
        self.dvar_v1 = tk.DoubleVar()
        self.dvar_v2 = tk.DoubleVar()
        self.txt_v1 = tk.Entry(self.frame, textvariable=self.dvar_v1)
        self.txt_v2 = tk.Entry(self.frame, textvariable=self.dvar_v2)
        self.btn_suma = tk.Button(self.frame, text='+', command=self.sumar)
        self.btn_resta = tk.Button(self.frame, text='-', command=self.restar)
        self.btn_multiplicacion = tk.Button(self.frame, text='x', command=self.multiplicar)
        self.btn_division = tk.Button(self.frame, text='/', command=self.dividir)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.lbl_v1.grid(row=0, column=0, sticky=tk.S)
        self.txt_v1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N)
        self.lbl_v2.grid(row=0, column=1, sticky=tk.S)
        self.txt_v2.grid(row=1, column=1, padx=(0, 5), pady=5, sticky=tk.W + tk.E + tk.N)
        self.btn_suma.grid(row=1, column=2, sticky=tk.N)
        self.btn_resta.grid(row=1, column=3, sticky=tk.N)
        self.btn_multiplicacion.grid(row=1, column=4, sticky=tk.N)
        self.btn_division.grid(row=1, column=5, sticky=tk.N)

    def calcular(self, f):
        try:
            v1 = self.dvar_v1.get()
            v2 = self.dvar_v2.get()
            res = f(v1, v2)
            mbox.showinfo('Resultado', 'El resultado vale ' + str(res))
        except Exception as err:
            mbox.showerror('Error', str(err))

    def sumar(self):
        self.calcular(lambda v1, v2: v1 + v2)

    def restar(self):
        self.calcular(lambda v1, v2: v1 - v2)

    def multiplicar(self):
        self.calcular(lambda v1, v2: v1 * v2)

    def dividir(self):
        self.calcular(lambda v1, v2: v1 / v2)


def main():
    calc = Calculator()


if __name__ == '__main__':
    main()
