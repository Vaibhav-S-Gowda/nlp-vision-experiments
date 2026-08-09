text = "Python is easy "
print("Original text: ",text)
new_text = text.replace("easy", "powerful")
print("New text: ",new_text)

vowels = "aeiouAEIOU"
count = 0
for ch in new_text:
    if ch in vowels:
        count += 1

print("Vowels: ", count)