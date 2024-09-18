def wonky_text(input_text):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(input_text))

# Get input from the user
user_input = input("Enter your text: ")

# Convert the input to wonky format
wonky_output = wonky_text(user_input)

# Print the result
print("Wonky output:", wonky_output)
