import tkinter as tk
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems!",
]

def tell_joke():
    joke = random.choice(jokes)
    joke_label.config(text=joke)

# Create the main window
root = tk.Tk()
root.title("Joke Teller")
root.geometry("400x200")

# Create and pack the button
joke_button = tk.Button(root, text="Tell me a joke", command=tell_joke)
joke_button.pack(pady=20)

# Create and pack the label to display jokes
joke_label = tk.Label(root, text="Click the button for a joke!", wraplength=350)
joke_label.pack(pady=10)

# Start the main event loop
root.mainloop()
