def divide_by(a, b):
    return a / b


try:
    print(divide_by(40, 0))
except:
    print("Something went wrong")


try:
    print(divide_by(70 / 0))
except Exception as e:
    print("something went wrong!", e)
    print(e.__class__)


try:
    print(divide_by(200/ 0))
except ZeroDivisionError as e:
    print("something went wrong!", e)
        
