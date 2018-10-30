def hello_print(first_half):
    second_half = " World"

    return first_half+second_half

print(hello_print("Hello"))

a=0
b=0
c=0

def task1():
    a = int(input("what is the first number?"))
    b = int(input("what is the second number?"))

    return a * b

print(task1())


def task2():
    a=int(input("put in a number between 1 and ten to see if it matched the other number"))
    if a ==3:
        print("true")
    if a != 3:
        print("false")

print(task2())
