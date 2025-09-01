def validate_input():
    while True:
        user_input = input("enter your name:").strip()
        if not user_input:
            print("Invalid Input , Enter the name the value not be empty")
        elif not user_input.isalpha():
            print("Enter the name ony")
        else:
            return user_input


name = validate_input()
print(f"Hello {name}")
    
