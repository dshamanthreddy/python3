class hospital:
    pcount = 0

    def __init__(self, pname, page):
        self.pname = pname
        self.page = page
        hospital.pcount += 1

    def printcount(self):
        print("no of patients %d" % hospital.pcount)

    def displayname(self):
        print("Name : ",self.pname, ",age : ", self.page  )




obj1 = hospital("prathyusha",29)

obj1.printcount()
obj1.displayname()

