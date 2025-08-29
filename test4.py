def caesar_decrypt_english(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    
    for char in text:
        if char.lower() in alphabet:
            # Определяем индекс буквы в алфавите
            idx = alphabet.index(char.lower())
            # Вычисляем новый индекс с обратным сдвигом (по модулю 26)
            new_idx = (idx - shift) % 26
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

# Зашифрованный текст
encrypted_text = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
# Обратный сдвиг на 25 влево
decrypted_text = caesar_decrypt_english(encrypted_text, 25)

print(decrypted_text)