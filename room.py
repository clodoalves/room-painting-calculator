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
        try:            
            self.__width = float(value)
            if (self.is_input_negative(self.__width)):
                print("Type only positive values")
                exit()
        except Exception:
            print("Invalid input")
            exit()

    @property
    def depth(self):
        return self.__depth    
    
    @depth.setter
    def depth(self, value):
        try:            
            self.__depth = float(value)
            if (self.is_input_negative(self.__depth)):
                print("Type only positive values")
                exit()
        except Exception:
            print("Invalid input")
            exit()

    @property  
    def heigth(self):
        return self.__heigth
    
    def is_input_negative(self, value):
        return value < 0