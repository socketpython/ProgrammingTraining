# card_checker.py
#
# Programmer   : Elad L
# Student no.  : 217
# Date         : 03/10/2020
#
# ---------------------------------------------------

# Constants
record_path = r"C:\Logs\report.txt"
password_path = r"C:\Logs\password.txt"


def menu():
    """
    The function print the menu, and gets the user's choice and returns it
    """
    
    while True:
        msg = """
    Welcome!
    Choose your option:
    1- Change login password
    2- Check if Hoger number is valid
    3- Show report"""
        print(msg)
        choice = input("Enter your choice (number): ")
        
        if 1 <= int(choice) <= 3:
            break
        
        print("The number you enrered is invalid")
    return choice


def change_password():
    """
    The function gets a valid password from the
    user and replace it with the last password
    """

    global password_path    
    new_password = input("Enter the new password: ")
    
    if len(new_password) >= 6 and new_password[-2:].isnumeric() and sum(c.isdigit() for c in new_password[:-2]) == 0:
        with open(password_path, "w") as pass_file:
            pass_file.write(new_password)
        return new_password
    
    print("The password you entered is invalid (the password's"
          "length needs to be atleast 6 and have atleast 2 digits)")


def check_card():
    """
    The function gets the user's personal number and checks if valid
    """
    
    number = input("Enter your Hoger number: ")
    date = input("Enter the date when you Hoger was made (xx.xx.xxxx): ")
    gender = input("Enter you gender (Male/Female): ").lower()
    day, month, year = date.split(".")

    # Checks whether the length of the number is
    # greater than 7 or less than 7 but was issued after 2011
    first_rule = len(number) > 7 or (len(number) < 7 and int(year) >= 2011)
    second_rule = number[-3] != month[-1]
    third_rule = (int(number[0]) + int(number[1])) >= int(day)
    times = int(number[-1]) * int(number[-2])
    fourth_rule = (times % 2 == 0 and gender == "female") or (times % 2 != 0 and gender == "male")
    
    if first_rule or second_rule or third_rule or fourth_rule:
        print("your Hoger number is invalid")
        return number, "not valid"
    
    print("your Hoger number is valid")
    return number, "valid"


def main():
    global record_path, password_path
    user_name = input("Enter your username -> ").lower()
    password_input = input("Enter your password -> ")
    
    with open(password_path, "r") as pass_file:
            password = pass_file.read().splitlines()[0]
    
    if (user_name == "root" or user_name == "admin") and password_input == password:
        choice = menu()
        if choice == "1":
            new_password = change_password()
            if not new_password:
                with open(record_path, "a") as reports:
                    reports.write(f"User {user_name.capitalize()} chose option"
                                  " {choice} - Changed password to {new_password}\n")
                              
        elif choice == "2":
            number, is_valid = check_card()
            with open(record_path, "a") as reports:
                reports.write(f"User {user_name.capitalize()} chose option"
                              " {choice} - Personal number {number} is {is_valid}\n")
        else:
            print("\nReport\n------")
            with open(record_path, "r") as reports:
                print(reports.read())
            with open(record_path, "a") as reports:
                reports.write(f"User {user_name.capitalize()} chose option"
                              " {choice} - Whatced the report\n")
    else:
        print("The password/username you entered is invalid")


if __name__ == "__main__":
    main()
