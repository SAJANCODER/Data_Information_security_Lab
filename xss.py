import html

# Ask user for input
user_input = input("Enter your name or some text: ")

# Escape HTML special characters to prevent XSS
safe_output = html.escape(user_input)

# Display safe output in console
print("\nSafe Output:")
print(safe_output)