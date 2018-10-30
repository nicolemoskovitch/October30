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
        return "true"
    if a != 3:
        return "false"

print(task2())

def task3():
    a=int(input("how much was the bill"))
    b = int(input("what percent do you want to tip"))
    b = b / 100
    return a * b

print("you should tip $" + str(task3()))

def task4():
    a=input("choose a letter to see if it is in the string")
    hello="hello"
    if a in hello:
        return "true"
    if a not in hello:
        return "false"

print(task4())