print("Hello world")

varB = "This string is too long " \
       "to be placd inside on" \
       " a single line"

print(varB)

varC = "Understandable"

print(len(varC))

bill_total = 225

discount1 = 10
discount2 = 25

if bill_total > 100 and bill_total < 200:
    print("Bill is greater 100!")
    bill_total = bill_total - discount1

elif bill_total > 200:
    print("Bill is greater than 200!")
    bill_total = bill_total - discount2
else:
    print("bill is less than 100!")

print("Total bill:", bill_total)


http_status = 200

if http_status == 200 or http_status == 201:
    print("success")
elif http_status == 400:
    print("Bad Request")
elif http_status == 404:
    print("Not found")
elif http_status == 500 or http_status == 501:
    print("server Error")
else:
    print("unknown")



str = "Looping"

for item in str:
    print(item)



for i in range(10):
    print("looping", i)



favorites = ["creme brulee", "Apple Pie", "Churros", "Tiramisu", "chocolate cake"]

for item in favorites:
    print("i like the desert", item)