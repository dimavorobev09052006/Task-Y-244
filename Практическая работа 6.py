text = input()
new_text = ''
for ch in text:
    if ch.islower():
        new_text += ch.upper()
    else:
        new_text += ch.lower()
print(new_text)