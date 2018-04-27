# -*- coding: UTF-8 -*-

dic1 = {"a": "b", "c": "d"}

dic1[2] = "cc"
dic1['a'] = 'aa'

print(dic1)

print(dic1['a'])

##delete the dict key
del dic1['c']
print(dic1)

print(dic1.copy())
dic1[1] = "12312"
print(dic1)
print(dic1.fromkeys(range(1, 10, 3)))

dica = {"a": "old", "b": "old1"}
dicb = {"a": "new", "b": "new1"}

dica.update(dicb)
print(dica)
