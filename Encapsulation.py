#Protected Vs Private
#Protected can still modify the methods and properties but acts as a warning
#private takes more coding but ensures that private can not be changed unless it is on purpose



class Cat:
        def __init__(self):
            self.__privatelives = 9
        def getlives(self):
            print(self.__privatelives)
        def setlives(self, private):
            self.__privatelives = private
            #the folowing make use of protected and private
        def color(self):
             self._protectedvar = "Yellow"

obj = Cat()
obj.getlives()
obj.setlives(10)
obj.getlives ()
obj._protectedvar = "Black"
print(obj._protectedvar)