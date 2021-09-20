import os
import subprocess


print(
    """ 
1 - View all files in current directory
2 - Read out files
3 - Make new files
4 - Delete files
5 - Rename a file
6 - Exit the session
"""
)


x = input("\n\n\nWhat do want to do? ")


def main():
    if x == "1":
        ran = subprocess.run("ls", capture_output=True)
        if ran.stderr:
            ran_on_windows = subprocess.run("dir", capture_output=True)
            print(ran_on_windows.stdout.decode())
        else:
            if ran.stdout:
                print((ran.stdout).decode())

    if x == "2":
        to_read = input("\nWhat file do you want to read out? ")
        with open(to_read, "r") as f:
            print(f.read())
            f.close()

    if x == "3":
        to_name = input("\nWhat do you want to name the file? ")
        subprocess.run(["touch", to_name])
        print("Made the file.")

    if x == "4":
        to_remove = input("\nWhich file do you want to delete? ")
        try:
            os.remove(to_remove)
        except FileNotFoundError:
            print("File does not exist.")

    if x == "5":
        current = input("\nWhich file do you want to rename? ")
        to_rename_to = input("\nWhat do you want to change the name to? ")
        try:
            os.rename(current, to_rename_to)
        except Exception:
            print("File not found.")

    if x == "6":
        exit(0)


main()
