class Emptyee():
    def __init__(self, name):
        self.name = name

    def isManager(self):
        if self.name == "Tom":
            return True
        else:
            return False

    def __str__(self):
        return "i am is nb:{}".format(self.name)


emp = Emptyee("Tom")
empc = Emptyee("Jerry")

print(id(emp), id(empc))
print(emp)

print("Tom: {0}".format(emp.isManager()), empc.isManager())



class part(Emptyee):
    pass

    def isManager(self):
        return "every one is good "


pc = part("123")
print(pc.isManager())
