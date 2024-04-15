countries = input().split(', ')
capitals = input().split(', ')

# result = {countries[index]: capitals[index] for index in range(len(countries))}
result = dict(zip(countries, capitals))
for key, value in result.items():
    print(f"{key} -> {value}")

# for index in range(len(countries)):
#     key = countries[index]
#     value = capitals[index]
#     result[key] = value
#
# for key, value in result.items():
#     print(f'{key} -> {value}')