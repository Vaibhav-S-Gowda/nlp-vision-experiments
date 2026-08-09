text = "Python is easy. NLP is interesting. Practice daily"
sentences = text.split(".")
count = 0

for sentence in sentences:
    if sentence.strip():
        count += 1

print("Sentence Count:", count)

for sentence in sentences:
    print(sentence[::-1]) # String Slicing