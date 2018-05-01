##练习二 集合
# definition collection

colt1 = []

colt1.append("ab")
colt1.append("hh")
colt1.append("ff")
colt1[0] = 'gg'
del colt1[1]

print(type(colt1), colt1, colt1[1])

colt2 = (100.1, 100.1, 10.12, 123.45)

print(type(colt2), colt2, colt2.count(100.1))

colt3 = set()

colt3.add(100.1)
colt3.add(300.1)
colt3.add(150.1)
colt3.update([3.1, 2.003])

print(type(colt3), colt3)

colt4 = {}

colt4["money1"] = 100.1
colt4["money2"] = 101.1
colt4["money3"] = 102.1
colt4["money4"] = 104.1
colt4["money2"] = 666
del colt4["money4"]

colt4.update({"m1": 00.1, "m2": 99.2})

print(type(colt4), colt4, colt4["money1"])

