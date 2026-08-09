import re

text = """
Contact us:
abc@gmail.com
support@yahoo.com
"""

emails = re.findall(r"\S+@\S+", text)

print(emails)