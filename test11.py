alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
text = "Блажен, кто верует, тепло ему на свете!"
shift = 10

result = []
for char in text:
    if char.lower() in alphabet:
        idx = alphabet.index(char.lower())
        new_idx = (idx + shift) % 32
        new_char = alphabet[new_idx]
        if char.isupper():
            new_char = new_char.upper()
        result.append(new_char)
    else:
        result.append(char)

print(''.join(result))