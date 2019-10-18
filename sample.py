from hotel_california import Hotel,Room,Occupier

# Setup
hotelCalifornia = Hotel(20)
print("==Hotel California==")
print("Rooms: ",hotelCalifornia.getNumRooms())

# Day 1
alex = Occupier(1)
brian = Occupier(1)
clare = Occupier(2)
dave = Occupier(4)
emma = Occupier(2)
frank = Occupier(3)
hotelCalifornia.checkIn(alex,False)
hotelCalifornia.checkIn(brian,False)
hotelCalifornia.checkIn(clare,True)
hotelCalifornia.checkIn(dave,False)
hotelCalifornia.checkIn(emma,False)
hotelCalifornia.checkIn(frank,True)
print("--Day 1--")
print("Free rooms: ",hotelCalifornia.getNumFreeRooms())
hotelCalifornia.updateOvernight()
x= 0
while x <= (len(hotelCalifornia.rooms)-1):
    if hotelCalifornia.rooms[x].getOccupier() != None:
        hotelCalifornia.eatDinner(x)
        print("Room",x,"| Nights:",hotelCalifornia.rooms[x].getOccupier().getLengthOfStay(),"Meals:",hotelCalifornia.rooms[x].getOccupier().getNumDinners())  
    x += 1
print("Income: £",hotelCalifornia.getTotalIncome())

# Day 2
hotelCalifornia.checkOut(1)
hotelCalifornia.updateOvernight()
print("--Day 2--")
print("Free rooms: ",hotelCalifornia.getNumFreeRooms())
x= 0
while x <= (len(hotelCalifornia.rooms)-1):
    if hotelCalifornia.rooms[x].getOccupier() != None:
        hotelCalifornia.eatDinner(x)
        print("Room",x,"| Nights:",hotelCalifornia.rooms[x].getOccupier().getLengthOfStay(),"Meals:",hotelCalifornia.rooms[x].getOccupier().getNumDinners()) 
    x += 1
print("Income: £",hotelCalifornia.getTotalIncome())

# Day 3
hotelCalifornia.checkOut(3)
hotelCalifornia.checkOut(4)
print("--Day 3--")
print("Free rooms: ",hotelCalifornia.getNumFreeRooms())
hotelCalifornia.updateOvernight()
x= 0
while x <= (len(hotelCalifornia.rooms)-1):
    if hotelCalifornia.rooms[x].getOccupier() != None:
        hotelCalifornia.eatDinner(x)
        print("Room",x,"| Nights:",hotelCalifornia.rooms[x].getOccupier().getLengthOfStay(),"Meals:",hotelCalifornia.rooms[x].getOccupier().getNumDinners()) 
    x += 1
print("Income: £",hotelCalifornia.getTotalIncome())

# Day 4
george = Occupier(2)
hotelCalifornia.checkIn(george,True)
hotelCalifornia.checkOut(6)
print("--Day 4--")
print("Free rooms: ",hotelCalifornia.getNumFreeRooms())
hotelCalifornia.updateOvernight()
x= 0
while x <= (len(hotelCalifornia.rooms)-1):
    if hotelCalifornia.rooms[x].getOccupier() != None:
        hotelCalifornia.eatDinner(x)
        print("Room",x,"| Nights:",hotelCalifornia.rooms[x].getOccupier().getLengthOfStay(),"Meals:",hotelCalifornia.rooms[x].getOccupier().getNumDinners()) 
    x += 1
print("Income: £",hotelCalifornia.getTotalIncome())
