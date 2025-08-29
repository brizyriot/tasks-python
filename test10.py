def caesar_encrypt_english(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    
    for char in text:
        if char.lower() in alphabet:
            # Определяем индекс буквы в алфавите
            idx = alphabet.index(char.lower())
            # Вычисляем новый индекс со сдвигом (по модулю 26)
            new_idx = (idx + shift) % 26
            # Получаем новую букву
            new_char = alphabet[new_idx]
            # Сохраняем регистр
            if char.isupper():
                new_char = new_char.upper()
            result.append(new_char)
        else:
            # Не буквы оставляем как есть
            result.append(char)
    
    return ''.join(result)

# Исходный текст
text = "To be, or not to be, that is the question!"
# Сдвиг на 17 вправо
encrypted_text = caesar_encrypt_english(text, 17)

print(encrypted_text)