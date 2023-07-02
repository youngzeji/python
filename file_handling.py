file = open("test.txt", mode = "r")

data = file.readlines()

print(data)

file.close()

with open("test2.txt", mode = "r") as doc:

    content = doc.read()

    print(content)