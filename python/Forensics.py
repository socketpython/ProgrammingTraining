# forensics.py
#
# Programmer   : Elad L
# Student no.  : 217
# Date         : 03/10/2020
#
# ---------------------------------------------------

# Imports
import os
import time
import argparse
import sys


def main():
    args = None
    if not len(sys.argv) == 4:
        parser = argparse.ArguementParser()
        parser.add_arguement("-i", "--investigator" type=str, help="Enter your name")
        parser.add_arguement("-f", "--investigation_name", type=str, help="Enter the name of the investigation")
        parser.add_arguement("-n", "--notes", type=str, help="Enter notes")
        args = parser.parse_args()
        investigator_name = args.investigator
        investigation_name = args.investigation_name
        notes = args.notes
    

    elif len(sys.argv) == 4:
        investigator_name = sys.argv[0]
        investigation_name = sys.argv[1]
        notes = sys.argv[2]

    else:
        investigator_name = input("Enter your name: ")
        investigation_name = input("Enter the name of the investigation: ")
        notes = input("Enter notes: ")

    path = r"c:\Forensics"
    start_time = time.ctime()

    invest_folder = f"{path}\{investigation_name}"
    os.mkdir(invest_folder)
    while True:
        if os.path.isdir(invest_folder):
            break

    folders = ["Pdf", "Pictures", "Videos", "Documents", "Links", "IPs", "Infected", "Cleaned", "E-Mails", "Logs"]
    for folder in folders:
        os.mkdir(f"{invest_folder}\{folder}")

    want_del = input("Do you want to delet folders(y/n): ")
    if want_del == "y":
        f = input("Enter the name of the folders and between them space: ").split(" ")
        for i in f:
            os.rmdir(f"{invest_folder}\{i}")

    det_file_name = f"{invest_folder}\Details.txt"
    os.system(f"(echo Start time: {start_time} & echo Investigator name: {investigator_name} & echo Notes: {notes}) > {det_file_name}")


if __name__ == "__main__":
    main()
