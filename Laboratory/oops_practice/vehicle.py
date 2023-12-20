class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


modelX = vehicle("meow", 500, 12)
print(modelX.max_speed, modelX.mileage)


class bus(vehicle):
    def seatingcap(self,seatingcapacity=50):
        return super().seating_capacity(capacity=50)


schoolvolvo = bus("schoolvolvo", 100, 8)
print("vehicle name:", schoolvolvo.name, "speed:",
      schoolvolvo.max_speed, "mileage:", schoolvolvo.mileage)
