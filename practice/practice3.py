
# 练习三条件判断

##guess dog age


trulyage = 10

while True:
    inputage = int(input("the dog age:"))

    if (inputage < 0):
        print("oops,error!")
        continue
    elif (inputage > 10):
        print("age should be smaller..")
        continue
    elif (inputage < 10):
        print("age should be bigger..")
        continue
    elif (inputage == 10):
        print("guess right!!! congratulations.")
        break
