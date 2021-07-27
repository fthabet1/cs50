class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Luffy", "Zoro", "Sanji", "Nami", "Ussop", "Chopper", "Robin", "Franky", "Brook"]
for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} to the flight successfully.")
    else:
        print(f"No available seats for {person}")
