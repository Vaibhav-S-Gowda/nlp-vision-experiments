text = "Natural    Language     Processing   is   fun"

words = text.split()

print(words)
print("Number of words:", len(words))

clean = " ".join(text.split())
print(clean)