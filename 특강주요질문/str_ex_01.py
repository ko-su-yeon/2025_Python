class Car:
    def __init__(self, speed=0, gear=1, color="white"):
        self.speed = speed
        self.gear = gear
        self.color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return f"속도: {self.speed}, 기어: {self.gear}, 색상: {self.color}"
    
myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.setColor("red")

print(myCar)