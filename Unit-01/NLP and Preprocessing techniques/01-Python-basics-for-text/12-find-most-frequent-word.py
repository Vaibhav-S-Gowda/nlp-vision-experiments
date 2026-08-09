text = "apple banana apple mongo apple banana"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

highest = max(frequency, key=frequency.get)

print("Most Frequent: ", highest)
print("Count: ", frequency[highest])