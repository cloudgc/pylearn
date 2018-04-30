# -*- coding: UTF-8 -*-

def method1():
    print("method1")


method1()


def method2(name, age=10):
    print(name, age)


method2("name")
method2("name", 23)

method2(age=100, name="Tom")
method2(name="jerry")


def method3(name, *desc):
    print(name, type(desc), type(desc[1]))


method3("name", "23 year", "world", "good gay")

####LGEB

a = 10


def method4(b):
    global a
    a += b
    print(a)


method4(2)


def method5(b):
    x = 1
    print(x)

    def inner():
        nonlocal x
        # global x
        # x = -1
        x += b
        print(x)

    inner()


method5(3)


def retMethod6(a, b):
    return a + b


print(retMethod6(101, 33))

x = int(3.3)
g = 0


def outer():
    o = 1

    def inner():
        i = 2
        print(x)

    inner()


outer()

import builtins

print(dir(builtins))

C = lambda a, b: a + b

print(C(1, 1))





matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(matrix)

print([[row[i] for row in matrix] for i in range(4)])