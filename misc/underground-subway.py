class UndergroundSystem:
    def __init__(self):
        self.stations = {}
        self.people = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.people:
            self.people[id] = [stationName, t]
        if stationName not in self.stations:
            self.stations[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        averageTime = t - self.people[id][1]
        startingStation = self.people[id][0]
        if id in self.people:
            startStation = self.stations[startingStation]
            if stationName in startStation:
                self.stations[startingStation][stationName].append(averageTime)
            else:
                self.stations[startingStation][stationName] = [averageTime]
            del self.people[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stations[startStation][endStation]) / len(self.stations[startStation][endStation])
