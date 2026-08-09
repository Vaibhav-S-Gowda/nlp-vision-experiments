import string

text = "Hello, World! Welcome to NLP."

clean = ""

for ch in text:
    if ch not in string.punctuation:
        clean += ch

print(clean)