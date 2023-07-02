with open("newfile.txt", "r") as file:
    print(file.read(5))
    print(file.read())

with open("test.txt", "r") as file:
    print(file.readline(5))
    print(file.readline(30))


with open("test2.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))
    
    for line in lines:
        print(line)