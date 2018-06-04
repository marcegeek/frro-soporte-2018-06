import tkinter as tk
import tkinter.messagebox as mbox


class Calculator2:
    def __init__(self, master):
        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.master.title('Calculadora 2')
        self.master.geometry('180x150')

    def create_widgets(self):
        self.expression_var = tk.StringVar()
        self.txt_expression = tk.Entry(self.master, textvariable=self.expression_var)
        self.btn_0 = tk.Button(self.master, text='0', command=self.add_0)
        self.btn_1 = tk.Button(self.master, text='1', command=self.add_1)
        self.btn_2 = tk.Button(self.master, text='2', command=self.add_2)
        self.btn_3 = tk.Button(self.master, text='3', command=self.add_3)
        self.btn_4 = tk.Button(self.master, text='4', command=self.add_4)
        self.btn_5 = tk.Button(self.master, text='5', command=self.add_5)
        self.btn_6 = tk.Button(self.master, text='6', command=self.add_6)
        self.btn_7 = tk.Button(self.master, text='7', command=self.add_7)
        self.btn_8 = tk.Button(self.master, text='8', command=self.add_8)
        self.btn_9 = tk.Button(self.master, text='9', command=self.add_9)
        self.btn_plus = tk.Button(self.master, text='+', command=self.add_plus)
        self.btn_minus = tk.Button(self.master, text='-', command=self.add_minus)
        self.btn_times = tk.Button(self.master, text='x', command=self.add_times)
        self.btn_divide = tk.Button(self.master, text='/', command=self.add_divide)
        self.btn_equals = tk.Button(self.master, text='=', command=self.compute)

        self.txt_expression.grid(columnspan=4)
        self.btn_7.grid(row=1, column=0)
        self.btn_8.grid(row=1, column=1)
        self.btn_9.grid(row=1, column=2)
        self.btn_plus.grid(row=1, column=3)
        self.btn_4.grid(row=2, column=0)
        self.btn_5.grid(row=2, column=1)
        self.btn_6.grid(row=2, column=2)
        self.btn_minus.grid(row=2, column=3)
        self.btn_1.grid(row=3, column=0)
        self.btn_2.grid(row=3, column=1)
        self.btn_3.grid(row=3, column=2)
        self.btn_divide.grid(row=3, column=3)
        self.btn_0.grid(row=4, column=0)
        self.btn_equals.grid(row=4, column=1, columnspan=2, sticky=tk.W + tk.E)
        self.btn_times.grid(row=4, column=3)

    def add_0(self):
        self.expression_var.set(self.expression_var.get() + '0')

    def add_1(self):
        self.expression_var.set(self.expression_var.get() + '1')

    def add_2(self):
        self.expression_var.set(self.expression_var.get() + '2')

    def add_3(self):
        self.expression_var.set(self.expression_var.get() + '3')

    def add_4(self):
        self.expression_var.set(self.expression_var.get() + '4')

    def add_5(self):
        self.expression_var.set(self.expression_var.get() + '5')

    def add_6(self):
        self.expression_var.set(self.expression_var.get() + '6')

    def add_7(self):
        self.expression_var.set(self.expression_var.get() + '7')

    def add_8(self):
        self.expression_var.set(self.expression_var.get() + '8')

    def add_9(self):
        self.expression_var.set(self.expression_var.get() + '9')

    def add_plus(self):
        self.expression_var.set(self.expression_var.get() + '+')

    def add_minus(self):
        self.expression_var.set(self.expression_var.get() + '-')

    def add_times(self):
        self.expression_var.set(self.expression_var.get() + '*')

    def add_divide(self):
        self.expression_var.set(self.expression_var.get() + '/')

    def compute(self):
        expression = self.expression_var.get()
        try:
            res = eval(expression)
            self.expression_var.set(str(res))
        except Exception as err:
            mbox.showerror('Error', str(err))


def main():
    root = tk.Tk()
    p = Calculator2(root)
    root.mainloop()


if __name__ == '__main__':
    main()
