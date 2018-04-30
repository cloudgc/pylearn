s = 'hello.primt\n'
print(str(s))
print(repr(s))

d = ("123", "12412")
print(str(d))
print(repr(d))

print('{0:2d} {2:3d} {1:4d}'.format(6, 56, 123))
print('{name:10}| {0:.2f}'.format(1.2356, name='asfasf'))

dt = {"name": "tom", "age": 18}
print('name-{0[name]:10}|'.format(dt))

# ccc = 123
ccc = 3.1424
print("|" + str(ccc).center(10) + "|")
print("|" + str(ccc).ljust(10) + "|")
print("|" + str(ccc).rjust(10) + "|")
# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr())
car = 'A'
print('{!a}'.format(car))

with open("./filecontent.txt", 'a+') as f:
    print("_asf", f.readlines())
    # print(f.tell())

# f.write("www.runorg.com\n")
# print(f.read(1))
f.close()

import pickle

import os

exportf = open("./export.file", 'wb')
# if not os.path.exists("./export.file"):
#     open("./export.file", 'wb').close()

daa = ("agent", "hmeasd", "fff", "this ist test")
pickle.dump(daa, exportf)

#
# dll = pickle.load("./export.file")
# print(dll)
exportf.close()

exportf = open("./export.file", 'rb')

print(pickle.load(exportf))
exportf.close()
