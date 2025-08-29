def caesar_decrypt_russian(text, shift):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = []
    
    for char in text:
        if char.lower() in alphabet:
            # Определяем индекс буквы в алфавите
            idx = alphabet.index(char.lower())
            # Вычисляем новый индекс с обратным сдвигом (по модулю 32)
            new_idx = (idx - shift) % 32
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
encrypted_text = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
# Обратный сдвиг на 7 влево
decrypted_text = caesar_decrypt_russian(encrypted_text, 7)

print(decrypted_text)