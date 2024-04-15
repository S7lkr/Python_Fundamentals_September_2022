company_name = input()
result = {}

while company_name != 'End':
    company, employee_id = company_name.split(" -> ")
    if company not in result.keys():
        result[company] = []
    if employee_id not in result[company]:
        result[company].append(employee_id)
    company_name = input()

for key in result.keys():
    print(key)
    for value in result[key]:
        print(f"-- {value}")