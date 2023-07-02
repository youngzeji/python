try:
    with open("newfile.txt", "w") as file:
        file.write("This is a new file created ")
        file.writelines(["\nThis is the second line of the file", "\nThere are permissions to add more lines"])
except FileNotFoundError as e:
    print("ERROR", e)