#Домашняя работа по уроку "Специальные методы классов"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


house = House('ЖК Эльбрус', 30)

print(len(house))
print(house)
