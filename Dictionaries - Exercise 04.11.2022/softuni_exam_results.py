results = {}    # here we store student: [points]
tries = {}  # here -> language: tries

while True:
    participant = input()
    if participant == "exam finished":
        break
    if "banned" in participant:
        participant = participant.split("-")
        name = participant[0]
        if name in results.keys():
            results.pop(name)
            continue
    student, language, points = participant.split("-")
    if student not in results.keys():
        results[student] = []
    results[student].append(int(points))
    if language not in tries.keys():
        tries[language] = 0
    tries[language] += 1

print("Results:")
for key, value in results.items():
    print(f"{key} | {max(value)}")
print("Submissions:")
for lang, cnt in tries.items():
    print(f"{lang} - {cnt}")