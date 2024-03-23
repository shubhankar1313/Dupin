import pyfiglet
import sys
from main2 import select_folder, sorter

# MAIN

def main():

    global invalid

    # Logo

    print(figlet_text("Dupin", "gothic"))
    
    # Options

    print(
        "       1 Select Folder\n            2 Help\n            3 Exit"
    )

    # Invalid Check

    print(invalid_msg(invalid))

    # Option Selection

    choose_option_main(input("        Select Option: "))

def choose_option_main(choice):
    r"For option selection of main()."

    global invalid

    if choice == "1":
        get_folder()
    elif choice == "2":
        pass
    elif choice == "3":
        sys.exit("\n   Thank You For Using FileSort :)")
    else:
        invalid = 1
        main()

# 1 SORTING PROCESS

def get_folder():

    global invalid

    print("\nEnter Path of Folder to Sort: ", end = "")
    folder = select_folder()
    if folder != -1:
        start_sorting(folder)
    else:
        invalid = 2
        main()

def start_sorting(folder):

    global invalid

    task = sorter(folder)
    if task == 1:
        invalid = 3
        main()
    else:
        invalid = 4
        main()

# FUNCTIONALITY

def figlet_text(prompt, style):
    r"Converts text in prompt to stylized text."

    return pyfiglet.figlet_format(prompt, font=style)

def invalid_msg(code=0):
    r"""Returns to Main() with corresponding error message according to the code.
    It also resets global variable invalid back to 0."""

    global invalid

    if code == 0:
        return ""
    elif code == 1:
        msg = "\n Invalid Input, Please Select Again!\n"
    elif code == 2:
        msg = "\n      Path Does Not Exist!\n"
    elif code == 3:
        msg = "\n        Folder Sorted!\n"
    elif code == 4:
        msg = "\n    Folder Already Sorted!\n"
    invalid = 0
    return msg

if __name__ == "__main__":

    global invalid

    invalid = 0  # Variable for checking invalid input in main

    main()