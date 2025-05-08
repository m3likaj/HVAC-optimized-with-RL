class Thermostat:
    def __init__(self, outTemp, inTemp, optimalTemp, threshold, energyConsumption):
        self.outTemp = outTemp
        self.inTemp = inTemp
        self.energyConsumption = energyConsumption
        self.optimalTemp = optimalTemp
        self.threshold = threshold
        self.heatOn = False
        self.coolOn = False
    def setTemp(self, inTemp, outTemp):
        self.inTemp = inTemp
        self.outTemp = outTemp
    def HeatingOn(self):
        self.heatOn = True
        self.coolOn = False
    def CoolingOn(self):
        self.coolOn = True
        self.heatOn = False
    def turnOff(self):
        self.heatOn = False
        self.coolOn = False

class Office:
    def __init__(self, inTemp, outTemp,optimalTemp, isOccupied):
        self.inTemp = inTemp
        self.outTemp = outTemp
        self.optimalTemp = optimalTemp
        self.thermostat = Thermostat(inTemp, outTemp, optimalTemp, 2, 50)
        self.isOccupied = isOccupied
    def setTemp(self, inTemp, outTemp):
        self.inTemp = inTemp
        self.outTemp = outTemp
    def setOccupied(self, isOccupied):
        self.isOccupied = isOccupied
