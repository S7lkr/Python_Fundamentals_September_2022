population = list(map(int, input().split(", ")))
min_wealth = int(input())
total_sum = 0

for finances in population:
    if finances < min_wealth:
        population[population.index(finances)] = min_wealth
        total_sum += min_wealth - finances

wealthiest = population.index(max(population))
population[wealthiest] -= total_sum

if population[wealthiest] <= min_wealth:
    print("No equal distribution possible")
else:
    print(population)