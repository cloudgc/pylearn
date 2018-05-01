#练习6 变量作用域
###LEGB

def max(a, b):
    if a > b:
        return a
    if b > a:
        return b
    if a == b:
        return a


print(max(1, 2))

print(max(2, 2))

x = 1


def test():
    x = -1

    def judge():
        # nonlocal x
        global x
        if x > 0:
            print("x is positive number")
        if x < 0:
            print("x is negative number")

    judge()


test()
