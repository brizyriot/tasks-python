def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

encrypted_text = "Hawnj pk swhg xabkna ukq nqj."
# Правильный сдвиг - 22
decrypted_text = caesar_decrypt(encrypted_text, 22)
print(decrypted_text)