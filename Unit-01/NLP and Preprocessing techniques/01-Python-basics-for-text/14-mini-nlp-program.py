# Count Word Frequency

text = """
Python is easy.
Python is powerful.
Python is popular.
"""

text = text.lower()
text = text.replace(".", "")
words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, ":", count)