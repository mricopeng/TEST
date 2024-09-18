import random

def wonky_text(input_text):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(input_text))

def reverse_text(input_text):
    return input_text[::-1]

def randomize_case(input_text):
    return ''.join(random.choice([c.upper(), c.lower()]) for c in input_text)

def l33t_speak(input_text):
    l33t_dict = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return ''.join(l33t_dict.get(c.lower(), c) for c in input_text)

def apply_transformation(text, transformation):
    transformations = {
        '1': ('Wonky', wonky_text),
        '2': ('Reversed', reverse_text),
        '3': ('Random Case', randomize_case),
        '4': ('L33t Speak', l33t_speak)
    }
    name, func = transformations.get(transformation, ('Invalid', lambda x: x))
    return name, func(text)

# Main program loop
while True:
    print("\nText Transformer")
    print("1. Wonky Text")
    print("2. Reverse Text")
    print("3. Random Case")
    print("4. L33t Speak")
    print("5. Quit")

    choice = input("Choose a transformation (1-5): ")
    
    if choice == '5':
        print("Goodbye!")
        break
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        continue
    
    user_input = input("Enter your text: ")
    name, result = apply_transformation(user_input, choice)
    print(f"{name} output: {result}")
