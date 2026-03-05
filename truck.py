from vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def load(self, weight):

        if weight > self.load_capacity:
            print("Error: muatan melebihi kapasitas truck")

        else:
            print(f"Loaded {weight} kg.")