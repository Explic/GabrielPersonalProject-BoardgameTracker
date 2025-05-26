from user_manager import signup, login

def one():
    input_username = input("Enter new username: ").strip()
    input_password = input("Enter new password: ").strip()
    if signup(input_username, input_password) == (True, "Account created successfully."):
        print("Account created successfully.")
        print(f"Username: {input_username}\nPassword: {input_password}")
        menu()
    else:
        print("Username already exists. Please try again.")
        menu()
        
def two():
    input_username = input("Enter username: ").strip()
    input_password = input("Enter password: ").strip()
    result = login(input_username, input_password)
    if result == (True, "Login successful."):
        print("Login successful.")
        print(f"Logged in as: {input_username}")
        input("Press Enter to exit.")
        exit()
    elif result == (False, "Username not found."):
        print("Username not found. Please try again.")
        menu()
    elif result == (False, "Incorrect password."):
        print("Incorrect password. Please try again.")
        menu()
    
def menu():
    option = input("Select an option:\n1. Sign Up\n2. Log In\n3. Exit\n")
    if option == "1":
        one()
    elif option == "2":
        two()
    elif option == "3":
        print("Exiting the program.")
        exit()    

# Testing the user manager functions
menu()
