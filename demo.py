import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Create buttons
        buttons = [
            '7', '8', '9', '/', 'cos',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', '√'
        ]

        # Add buttons to the grid
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=8).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Add clear button
        tk.Button(master, text='Clear', command=self.clear, width=18).grid(row=row, column=0, columnspan=2, padx=2, pady=2)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key in ['cos', 'sin', 'tan', '√']:
            self.calculate_function(key)
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

    def calculate_function(self, func):
        try:
            value = float(self.display.get())
            if func == 'cos':
                result = math.cos(math.radians(value))
            elif func == 'sin':
                result = math.sin(math.radians(value))
            elif func == 'tan':
                result = math.tan(math.radians(value))
            elif func == '√':
                result = math.sqrt(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
