import os 

def print_changes():
    contents = os.listdir(r"C:\Users\Okereke-Ejiogu\Documents")
    print("current directory contents")
    print(contents)

print(print_changes())
