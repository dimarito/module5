class House:
    houses_history = []

    def __new__(cls, *args):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args[1]

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            return new_floor
        else:
            return "Такого этажа не существует"

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

del h1
