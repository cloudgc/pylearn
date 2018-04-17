# -*- coding: UTF-8 -*-
list = ['Google', 'Runoob', 1997, 2000]

print(id(list))
print(id(list[:]))

print(list[1:2])

del list[2]

print(list)

ll = [['a', 'b', 'c'], [1, 2, 3]]
print(ll[0][2])

base = ["@", "$", "%", "&"]
base.append("append")
print(base)
base.count("%")
print(base)
base.extend(("a", "b", "c"))
print(base)
print(base.index("a"))
base.insert(2, "I")
print(base)
print(base.pop(-2))

print(base.remove("a"))
base.reverse()
print(base)

base.sort()
print(base)

l = [i for i in range(0, 15)]
# l[start:end:span]
print(l[::2])

import copy

d = copy.copy(l)
print(d, id(l), id(d))

list_empty = [None]*10

