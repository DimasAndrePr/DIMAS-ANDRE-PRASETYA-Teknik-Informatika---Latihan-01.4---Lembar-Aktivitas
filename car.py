from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def honk(self):
        print("Beep! Beep!")