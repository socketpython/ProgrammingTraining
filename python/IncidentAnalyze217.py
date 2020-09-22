# IncidentAnalyze217.py
#
# Programmer   : Elad L
# Student no.  : 217
# Date         : 22/09/2020
#
# This program sorts logs of incidents according
# to the user's choice
# ---------------------------------------------------


# Imports
import shutil
import os


# Constants
folder_path = r"C:\Analyze"
options = ["Sort by unit number", "Sort by risk",
           "Sort by date", "Exit"]
units = [1133, 2222, 4546, 7878, 9999, 1919]
logs_path = r""


def menu():
    """Prints the menu for the user and returns the choice"""
    global options

    index = 1
    for option in options:
        print(f"{index}. {option}")
        index += 1

    choice = int(input("Enter the number of your choice: "))
    return choice


def get_log_files():
    """Gets all the file names of the logs"""
    global logs_path
    
    log_files = []
    # Goes through the folder files
    for _, _, filenames in os.walk(logs_path):
        log_files.extend(filenames)
        break
    return log_files


def sort_by_unit():
    """
    Puts only the logs belonging to the unit into the
    unit folder
    """
    global units, folder_path, logs_path
    
    unit_num = int(input("Enter the unit number: "))
    unit_dir = f"{folder_path}\{unit_num}"
    
    # check if dir exist
    if os.path.exists(unit_dir):
        print("The unit dir is already exist")
        return
    # create folder if not
    os.mkdir(unit_dir)
    
    log_files = get_log_files()

    for log_file in log_files:
        log_file_path = f"{logs_path}\{log_file}"
        # Reads the file into the 'data' variable
        with open(log_file_path, "r") as log:
            data = log.read()

        # Checks whether the unit name is in the log
        if f"Unit: {unit_num}" in data:
            new_path = f"{unit_dir}\{log_file}"
            shutil.copyfile(log_file_path, new_path)

def sort_by_risk():
    """
    Sort the logs according to their level of
    risk and put them in the appropriate folders
    """
    global folder_path, logs_path

    low_path = f"{folder_path}\Low"
    medium_path = f"{folder_path}\Medium"
    critical_path = f"{folder_path}\Critical"
    risk_lvls = ["Low", "Medium", "Critical"]
    
    low_exist = os.path.exists(low_path)
    medium_exist = os.path.exists(medium_path)
    critical_exist = os.path.exists(critical_path)
    # check if one of the dirs exist
    if low_exist or medium_exist or critical_exist:
        print("Atleast one of the folders is already exist")
        return

    # Creates a folder for each level of risk
    os.mkdir(low_path)
    os.mkdir(medium_path)
    os.mkdir(critical_path)
    log_files = get_log_files()

    for log_file in log_files:
        log_file_path = f"{logs_path}\{log_file}"
        # Reads the file into the 'data' variable
        with open(log_file_path, "r") as log:
            data = log.read()

        for risk in risk_lvls:
            # Checks whether the risk is in the log
            if f"Risk: {risk}" in data:
                new_path = f"{folder_path}\{risk}\{log_file}"
                shutil.copyfile(log_file_path, new_path)


def sort_by_date():
    """
    Puts in the folder only the logs that occurred
    in the year that the user selects
    """
    global folder_path, logs_path

    year = input("Enter the year of your choice: ")
    date_dir = f"{folder_path}\{year}"
    
    # check if dir exist
    if os.path.exists(date_dir):
        print(f"The '{year}' dir is already exist")
        return

    os.mkdir(date_dir)
    log_files = get_log_files()

    for log_file in log_files:
        log_file_path = f"{logs_path}\{log_file}"
        # Reads the file into the 'data' variable
        with open(log_file_path, "r") as log:
            data = log.read().splitlines()

        # Gets only the row of the date
        date_line = data[5]
        # Checks whether the year is in the log
        if year in date_line:
            new_path = f"{folder_path}\{year}\{log_file}"
            shutil.copyfile(log_file_path, new_path)


def main():
    global logs_path

    logs_path = input("Enter the path to the Logs folder: ")
    choice = 0

    while choice != 4:
        choice = menu()

        if choice == 1:
            sort_by_unit()

        elif choice == 2:
            sort_by_risk()

        elif choice == 3:
            sort_by_date()

        elif choice != 4:
            print("The number you wrote is incorrect (should be between 1-4)")


if __name__ == "__main__":
    main()
