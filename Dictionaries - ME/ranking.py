def contest_validator(name):
    if name in passwords.keys():
        return True
    return False


def password_validator(pass_code):
    if pass_code == passwords[event]:
        return True
    return False


passwords = {}
while True:
    text = input()
    if "end of" in text:
        break
    contest, password = text.split(":")
    if contest not in passwords.keys():
        passwords[contest] = password

results = {}
while True:
    some_text = input()
    if "end of" in some_text:
        break
    event, password2, user, points = some_text.split("=>")
    if not contest_validator(event):
        continue
    if not password_validator(password2):
        continue
    if user not in results.keys():
        results[user] = {}
    if event not in results[user].keys():
        results[user][event] = []
    results[user][event].append(int(points))

user_points = {}
for username, info in results.items():
    for lang, score in info.items():
        if username not in user_points.keys():
            user_points[username] = 0
        user_points[username] += max(score)

print(f"Best candidate is {max(user_points)} with total {max(user_points.values())} points.")
print("Ranking:")
for username, info in sorted(results.items()):
    print(username)
    for lang, score in sorted(info.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {lang} -> {max(score)}")
