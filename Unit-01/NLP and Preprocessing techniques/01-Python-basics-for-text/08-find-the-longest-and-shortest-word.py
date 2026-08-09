text = "Natural Language Processing using Python"
words = text.split()
longest = words[0]
shortest = words[-1]
for word in words:
    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Longest Word: ", longest)
print("Shortest Word: ", shortest)