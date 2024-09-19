class MakeCar:
    def __init__(self, name, year, color, brand):
        self.name = name
        self.year= year
        self.color = color
        self.brand = brand


fortune_car = MakeCar()
fortune_car("Camry", 2025, "Gray", "Toyota")
print(fortune_car.name)