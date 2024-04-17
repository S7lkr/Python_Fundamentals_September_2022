text = input().split("\\")
# file, extension = text[-1].split(".")
file, extension = text[len(text)-1].split(".")

print(f"File name: {file}")
print(f"File extension: {extension}")