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
            '0', '.', '=', '+', '√',
            'log', 'exp'  # Add new buttons for log and exp
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

        # Adjust the grid layout to accommodate new buttons
        tk.Button(master, text='Clear', command=self.clear, width=8).grid(row=row, column=0, padx=2, pady=2)
        tk.Button(master, text='log', command=lambda: self.click('log'), width=8).grid(row=row, column=1, padx=2, pady=2)
        tk.Button(master, text='exp', command=lambda: self.click('exp'), width=8).grid(row=row, column=2, padx=2, pady=2)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key in ['cos', 'sin', 'tan', '√', 'log', 'exp']:  # Add 'log' and 'exp' here
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
            elif func == 'log':
                result = math.log10(value)  # Using log base 10
            elif func == 'exp':
                result = math.exp(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
