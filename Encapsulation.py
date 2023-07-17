#Protected Vs Private
#Protected can still modify the methods and properties but acts as a warning
#private takes more coding but ensures that private can not be changed unless it is on purpose



class Animal:
    def Dog(self):
        self.protectedcolor = "Yellow" #originally set 

    def Cat(self):
        self.privatelives = 9
        def getlives(self):
            print(self._privatelives)
        def setlives(self, private):
            self.privatelives = private
            #the folowing make use of protected and private
obj = Animal()
obj.protectedcolor = "Black" #you still have ability to change, just warns them
print(obj.protectedcolor)
cobj = Cat()
cobj.getlives()
cobj.setlives(10)
cobj.getlives
