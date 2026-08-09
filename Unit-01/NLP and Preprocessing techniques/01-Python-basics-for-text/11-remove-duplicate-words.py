text = "Python is easy Python is powerful"

words = text.split()

unique = []

for word in words:
    if word not in unique:
        unique.append(word)

print(unique)