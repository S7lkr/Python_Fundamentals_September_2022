centuries = int(input())
years = centuries * 100
days = int(365.2422 * years)    # i.e. there cannot be 17.83 days, 'int' ignores everything after the dot, and takes 17
hours = 24 * days               # NOTE that 'int' makes the same as 'math.floor', but faster !!
minutes = 60 * hours

print(f'{centuries} centuries = {years} years = {round(days)} days = {round(hours)} hours = {round(minutes)} minutes')