import tkinter as tk
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems!",
    # New jokes
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the JavaScript developer quit his job? Because he didn't get arrays.",
    "How do you comfort a JavaScript bug? You console it!",
    "Why do Java developers wear glasses? Because they don't C#!",
    "Why was six afraid of seven? Because seven eight nine!",
    "What's the best way to watch a fly fishing tournament? Live stream.",
    "Why did the scarecrow become a successful motivational speaker? He was outstanding in his field.",
    "What do you call a parade of rabbits hopping backwards? A receding hare-line.",
    "Why don't scientists trust atoms? Because they make up everything!",
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
