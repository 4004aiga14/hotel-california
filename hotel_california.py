'''
Hotel California Simulator 2019
(C) 2019 Copyright of Aiden Gall
Licensed under MIT License
'''

class Room:
    def __init__(self, seaView):
        try:
            if type(seaView) is bool:
                self.seaView = seaView
            else:
                raise TypeError("Not Type 'Boolean'")
        except TypeError as te:
            print(te)
        self.occupier = None

    def hasSeaView(self):
        return self.seaView

    def setOccupier(self, occupier):
        try:
            if type(occupier) is Occupier or occupier == None:
                self.occupier = occupier
            else:
                raise TypeError("Not Type 'Occupier' or Boolean 'None'")
        except TypeError as te:
            print(te)

    def getOccupier(self):
        return self.occupier

class Occupier:
    def __init__(self, numGroup):
        self.numGroup = numGroup
        self.numNights = 0
        self.numDinner = 0

    def getLengthOfStay(self):
        return self.numNights

    def getNumInGroup(self):
        return self.numGroup

    def getNumDinners(self):
        return self.numDinner

    def stayNight(self):
        self.numNights += 1
        return

    def eatDinner(self):
        self.numDinner += 1

class Hotel:
    ROOM_PRICE = 20
    SEAVIEW_SUPPLEMENT = 5
    SINGLE_OCCUPIER_SUPPLEMENT = 5
    DINNER_PRICE = 9

    def __init__(self, numRooms):
        self.numRooms = numRooms
        self.money = 0
        self.rooms = []
        for i in range(self.numRooms):
            if i % 2 == 0:
                self.rooms.append(Room(True))
            else:
                self.rooms.append(Room(False))

    def findVacantRoom(self):
        i = 0
        for room in self.rooms:
            if room.getOccupier() == None:
                return i
            else:
                i += 1
        return -1

    def findVacantSeaView(self):
        i = 0
        for room in self.rooms:
            if room.getOccupier() == None and room.hasSeaView() == True:
                return i
            else:
                i += 1
        return -1

    def checkIn(self,occupier,seaView):
        if seaView:
            room = self.findVacantSeaView()
            if room == -1:
                room = self.findVacantRoom()
        else:
            room = self.findVacantRoom()
        if room == -1:
            return room
        self.rooms[room].setOccupier(occupier)
        return room

    def getBill(self, room):
        total = 0
        lengthOfStay = self.rooms[room].getOccupier().getLengthOfStay()
        numInGroup = self.rooms[room].getOccupier().getNumInGroup()
        if self.rooms[room].hasSeaView():
            total += lengthOfStay * self.SEAVIEW_SUPPLEMENT
        if numInGroup == 1:
            total += lengthOfStay * self.SINGLE_OCCUPIER_SUPPLEMENT
        total += lengthOfStay * self.ROOM_PRICE * numInGroup
        total += self.rooms[room].getOccupier().getNumDinners() * self.DINNER_PRICE
        return total

    def checkOut(self, room):
        self.money += self.getBill(room)
        self.rooms[room].setOccupier(None)
        return

    def updateOvernight(self):
        for room in self.rooms:
            if room.getOccupier() != None:
                room.getOccupier().stayNight()
        return

    def eatDinner(self, room):
        for i in range(self.rooms[room].getOccupier().getNumInGroup()):
            self.rooms[room].getOccupier().eatDinner()
        return

    def getTotalIncome(self):
        return self.money

    def getNumFreeRooms(self):
        freeRooms = 0
        for room in self.rooms:
            if room.getOccupier() != None:
                freeRooms += 1
        return self.numRooms - freeRooms

    def getNumRooms(self):
        return self.numRooms