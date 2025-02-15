from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):  # Corrected __init__ method
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        # Entry widget to display the equation
        self.entry = Entry(master, width=20, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation)
        self.entry.place(x=0, y=0)

        # Buttons
        buttons = [
            ('(', 0, 50), (')', 90, 50), ('%', 180, 50), ('/', 270, 50),
            ('7', 0, 125), ('8', 90, 125), ('9', 180, 125), ('*', 270, 125),
            ('4', 0, 200), ('5', 90, 200), ('6', 180, 200), ('-', 270, 200),
            ('1', 0, 275), ('2', 90, 275), ('3', 180, 275), ('+', 270, 275),
            ('C', 0, 350), ('0', 90, 350), ('.', 180, 350), ('=', 270, 350)
        ]

        for text, x, y in buttons:
            bg_color = 'lightblue' if text == '=' else 'white'
            command = self.solve if text == '=' else (self.clear if text == 'C' else lambda t=text: self.show(t))
            Button(master, width=11, height=4, text=text, relief='flat', bg=bg_color, command=command).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''


root = Tk()
calculator = Calculator(root)
root.mainloop()
