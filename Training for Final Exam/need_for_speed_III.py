def drive(a_car, dist, fuel_to_burn):
    garage[a_car][0] += dist
    garage[a_car][1] -= fuel_to_burn
    return garage


def refuel(a_car, fuel_to_refill):
    fuel_before = garage[a_car][1]
    garage[a_car][1] += fuel_to_refill
    if garage[a_car][1] > 75:
        garage[a_car][1] = 75
    print(f"{a_car} refueled with {garage[a_car][1] - fuel_before} liters")
    return garage


def revert(a_car, km_reverted):
    garage[a_car][0] -= km_reverted
    return garage


cars = int(input())
garage = {}

for vehicle in range(cars):
    info = input().split("|")
    car, mileage, fuel = info[0], int(info[1]), int(info[2])
    if car not in garage.keys():
        garage[car] = []
    garage[car] = [mileage, fuel]

command = input().split(" : ")
while command[0] != "Stop":
    a_car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel <= garage[a_car][1]:
            garage = drive(a_car, distance, fuel)
            print(f"{a_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if garage[a_car][0] >= 100000:
            del garage[a_car]
            print(f"Time to sell the {a_car}!")
    elif command[0] == "Refuel":
        fuel = int(command[2])
        garage = refuel(a_car, fuel)
    elif command[0] == "Revert":
        kilometers_reverted = int(command[2])
        garage = revert(a_car, kilometers_reverted)
        if garage[a_car][0] >= 10000:
            print(f"{a_car} mileage decreased by {kilometers_reverted} kilometers")
        if garage[a_car][0] < 10000:
            garage[a_car][0] = 10000
    command = input().split(" : ")

for car, km_fuel in garage.items():
    print(f"{car} -> Mileage: {km_fuel[0]} kms, Fuel in the tank: {km_fuel[1]} lt.")