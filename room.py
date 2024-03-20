class Room:
    __width:float
    __depth:float
    __heigth:float

    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.__heigth = 2.9

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def depth(self):
        return self.__depth    
    
    @depth.setter
    def depth(self, value):
        self.__depth = value

    @property  
    def heigth(self):
        return self.__heigth