from room import Room
from calculator import Calculator

room_width = input("Type the room width: ")
room_depth = input("Type the room depth: ")

room = Room(room_width, room_depth)

calculator = Calculator(room)

print("The necessary amount of paint liters is: ", calculator.calculate_necessary_paint_liters())