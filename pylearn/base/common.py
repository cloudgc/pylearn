# -*- coding: UTF-8 -*-

import sys

print(sys.maxsize)
print(sys.getsizeof(1.0))

nums = 9223372036854775807 * 2
print(nums)

a = 5.026

print(float('%.2f' % a))

from decimal import Decimal

print(Decimal(a).quantize(Decimal('0.00')))

print(1 + 2j)

# input("\n\n按下 enter 键后退出。")
x = 'runoob';
sys.stdout.write(x + '\n')

for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

item_one = "123"
item_two = "4235"
item_three = "jkhjk"

total = item_one + \
        item_two + \
        item_three

print(total)

####### int

plus = 1 + 1
mul = 3 - 1
div = 3 / 2
div = 3 // 2
le = 3 % 2
sqr = 3 ** 2
# isinstance(sqr))

######## str

str = "ABCDed"
print(str[0:-1])
print(str[2:4])
print(str * 2)

# str[1] = 'c'  error

##############list

list = ['abcd', 786, 2.23, 'runoob', 70.2]

print(list[:-1])
print(list * 2)
list[0] = 'FFF'
print(list[0:3])

#############tuple

tuple = ('tttt', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple[:-1])
print(tuple * 2)
print(tuple[1:3])
print(tuple[2:])
print(tuple + tinytuple)

# tuple[2] = 666
# print(tuple)

tuEmpty = ()
tupleOne = (123,)
print(tuEmpty, tupleOne)

###################set
setA = {"$", "%", '%^'}
setB = {"A", "B"}
print(setA | setB)
# print(setA[0])
# print(setA + setA)

########### dictionary
dict = {}
dict['name'] = 'tom'
dict[2] = 'gjhghj'
print(dict)
print(dict[2])
print(dict.keys(), dict.values())
dict = {x: x * 2 for x in (1, 2, 3, 4)}
print(dict)

###########convert
print(int('3'))
print(frozenset('sfasfasdasd'))

sum = 1

for i in range(101):
    sum = sum + i

print(sum)
