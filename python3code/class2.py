
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





class dog(hospital):


    def __init__(self, name ,age, pname, page):
        hospital.__init__(self, pname, page)
        self.name = name
        self.age  = age


    def details(self):
        print("name : ", self.name , "age : ", self.age )
        hospital.displayname(self)







#objdog = dog(" bowbow" , 5)

#objdog.details()




obj = dog ("prat", 21 ,"chow", 2)
obj.details()
print()