from room import Room

class Calculator:
    __room_wall_area:float
    __ceiling_area:float
    __room: Room

    def __init__(self, room):
        self.__room = room

    def __calculate_room_wall_area(self):
        return 2 * (self.__room.width + self.__room.depth) * self.__room.heigth
        
    def __calculate_ceiling_area(self):
        return self.__room.width * self.__room.depth

    def calculate_necessary_paint_liters(self):
        self.__room_wall_area = self.__calculate_room_wall_area()
        self.__ceiling_area = self.__calculate_ceiling_area()

        paint_liters = (self.__room_wall_area + self.__ceiling_area)/10.0

        return paint_liters