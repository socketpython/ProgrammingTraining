import datetime


birth_dates = {}
done = False


def read_file(file_path):
    """
    This function read the data from the .txt file into the global var birth_dates
    """
    global birth_dates
    with open(file_path, "r") as file:
        data = file.read().splitlines()
    for line in data:
        name, date = line.split(":")
        birth_dates[name] = date


def write_file(file_path):
    """
    This function write the data from the birth_dates var into the file
    """
    global birth_dates
    data = ""
    for name, date in birth_dates.items():
        data += f"{name}:{date}\n"
    data = data[:-1]
    with open(file_path, "w") as file:
        file.write(data)


def add_student():
    """
    Adds student to the dictionary
    """
    name = input("Enter the student's name: ")
    date = input("Enter his birth date (dd\mm\yyyy): ")
    global birth_dates
    birth_dates[name] = date


def same_month():
    """
    Show students who were borned in the same month
    """
    valid = False
    while not valid:
        month = int(input("Enter the month (in numbers): "))
        valid = check_month(month)
        if valid == False:
            print("The value you entered is invalid!")
    print("Students who were borned in the same month:")
    global birth_dates
    for name, date in birth_dates.items():
        d, m, y = date.split("\\")
        if month == int(m):
            age = datetime.datetime.today().year - int(y)
            print(f"- Name: {name}, Birth Date: {date}, Age: {age}")


def check_month(month):
    return 1 <= month <= 12


def same_year():
    """
    Show students who were borned in the same year
    """
    valid = False
    while not valid:
        year = int(input("Enter the year: "))
        valid = check_year(year)
        if valid == False:
            print("The value you entered is invalid!")
    print("Students who were borned in the same year:")
    global birth_dates
    for name, date in birth_dates.items():
        print(name, date)
        d, m, y = date.split("\\")
        print(year == int(y), y)
        if year == int(y):
            age = datetime.datetime.today().year - int(y)
            print(f"- Name: {name}, Birth Date: {date}, Age: {age}")


def check_year(year):
    return type(year) == int and len(year) == 4


def exit_program(file_path):
    """
    This function breaks the loop and calls to 'write_file()' to save the data
    """
    global done
    done = True
    write_file(file_path)


def check_for_birthday():
    global birth_dates
    full_date = datetime.datetime.today()
    today = datetime.date(full_date.year, full_date.month, full_date.day)
    for name, date in birth_dates.items():
        d, m, y = date.split("\\")
        birth = datetime.date(today.year, int(m), int(d))
        if (birth - today).days <= 14:
            print(f"Happy birthday {name}!")


def main():
    file_path = r"c:\birthdays.txt"
    read_file(file_path)
    global done

    check_for_birthday()
    
    while not done:
        print("""
Enter the number according to your choice:
1 - Add new student
2 - Show students who were borned in the same month
3 - Show students who were borned in the same year
4 - Exit
""")
        choice = int(input("-->"))
        if choice == 1:
            add_student()
        elif choice == 2:
            same_month()
        elif choice == 3:
            same_year()
        elif choice == 4:
            exit_program(file_path)


if __name__ == "__main__":
    main()
