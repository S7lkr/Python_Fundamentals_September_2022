import re

message_count = int(input())
attacked_planets = []
destroyed_planets = []

for message in range(message_count):
    current_message = input()
    star = r"[star]"
    letters_cnt = re.findall(star, current_message, flags=re.IGNORECASE)
    number = len(letters_cnt)
    decrypted_msg = ''
    for ch in current_message:
        decrypted_msg += chr(ord(ch) - number)
    planet_pattern = r"(?:[^\@\-\!\:\>]*)@([A-Z][a-z]+)(?:[^\@\-\!\:\>]*):(?:[^\@\-\!\:\>]*)\d+(?:[^\@\-\!\:\>]*)" \
                     r"!(A|D)!(?:[^\@\-\!\:\>]*)->\d+(?:[^\@\-\!\:\>]*)"
    planet = re.findall(planet_pattern, decrypted_msg)
    if planet:
        if planet[0][1] == "A":
            attacked_planets.append(planet[0][0])
        else:
            destroyed_planets.append(planet[0][0])

print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets) > 0:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets) > 0:
    for planet2 in sorted(destroyed_planets):
        print(f"-> {planet2}")