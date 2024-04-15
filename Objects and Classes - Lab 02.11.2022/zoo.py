class Zoo:
    __animals = 0

    def __init__(self, zoo_named):
        self.name = zoo_named
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, info):
        result = ''
        if info == 'mammal':
            result += f"Mammals in {zoo_name}: {', '.join(self.mammals)}\n"
        elif info == 'fish':
            result += f"Fishes in {zoo_name}: {', '.join(self.fishes)}\n"
        elif info == 'bird':
            result += f"Birds in {zoo_name}: {', '.join(self.birds)}\n"
        result += f'Total animals: {total_animals}'
        return result


zoo_name = input()
animal_in_zoo = Zoo(zoo_name)
total_animals = int(input())

for _ in range(total_animals):
    current_animal = input()
    specie, names = current_animal.split()
    animal_in_zoo.add_animal(specie, names)

infou = input()
print(animal_in_zoo.get_info(infou))