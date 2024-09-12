
class Car:
    # constructor method  #dunder method
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def start(self):
        print(f"You have started the {self.color} {self.model}, which was made in {self.year}")

    def drive(self):
        print(f"You are driving the car {self.color} {self.model}, which was made in {self.year}")

    def stop(self):
        print(f"You have stopped the car {self.color} {self.model}, which was made in {self.year}")


    def describe(self):
        print(f"{self.year} {self.color} {self.model}")