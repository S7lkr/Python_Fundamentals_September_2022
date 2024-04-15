class People:
    def __init__(self):
        self.people = []


party = People()
name = input()

while name != 'End':
    party.people.append(name)
    name = input()

print(f"Going: {', '.join(party.people)}")
print(f'Total: {len(party.people)}')

# lst = ['1', '2', '3']
# print(', '.join(lst))