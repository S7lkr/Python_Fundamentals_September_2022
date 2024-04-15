class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.radius    # 2nr

    def calculate_area(self):
        result = Circle.__pi * pow(self.radius, 2)  # nr2
        return result

    def calculate_area_of_sector(self, angle):
        return Circle.__pi * self.radius * self.radius * angle / 360


diameter = int(input())
figure = Circle(diameter)
angle = int(input())

print(f'{figure.calculate_circumference():.2f}')
print(f'{figure.calculate_area():.2f}')
print(f'{figure.calculate_area_of_sector(angle):.2f}')