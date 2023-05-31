# getter and setter functions 


class PointPublic:
        def __init__(self, x,y) -> None:
                self.x = x
                self.y = y
    

class PointPrivateGetterSetter:
    def __init__(self,x=0,y=0):
        self._x = x
        self._y = y 


 # this is another way to write the getter method using pythonic style --> with a @property method 
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    # this is anoyher way to do it using the @attribute.setter

    @x.setter   # its the same name as the getter method but with a setter 
    def x(self,x):
        self._x = x
    @y.setter
    def y(self,y):
        self._y =y 



# normal methods 

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self,x ):
        self._x = x
    
    def set_y(self,y):
        self._y = y


if __name__ == "__main__":
    p1 = PointPublic(1,0)
    print("point P1 with public attributes")
    print("p1= (" + str(p1.x) + "," + str(p1.y)+")")
    p1.x = 2
    p1.y = 5
    print("p1= (" + str(p1.x) + "," + str(p1.y)+") \n")

    p2 = PointPrivateGetterSetter(1,0)
    print("point P1 with private attributes and getter and setter methods ")
    print("p2= (" + str(p2.get_x()) + "," + str(p2.get_y())+")")

    p2.set_x(2)
    p2.set_y(5)
    print("p2= (" + str(p2.get_x()) + "," + str(p2.get_y())+")")

    p3 = PointPrivateGetterSetter(1,0)
    print("p3= (" + str(p3.x) + "," + str(p3.y) + ")")





