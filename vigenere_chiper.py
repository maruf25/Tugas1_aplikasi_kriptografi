def vigenere_encrypt(plain_text, key):
    """Mengenkripsi pesan dengan metode Vigenere Cipher"""
    cipher_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            # Jika karakter adalah huruf, maka enkripsi dengan aturan Vigenere Cipher
            char_value = ord(char.lower()) - 97
            key_value = int(key[key_index]) - 1
            new_char_value = (char_value + key_value) % 26
            new_char = chr(new_char_value + 97)
            key_index = (key_index + 1) % len(key)
        else:
            # Jika karakter bukan huruf, maka tidak dienkripsi
            new_char = char
        cipher_text += new_char
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    """Mendekripsi pesan dengan metode Vigenere Cipher"""
    plain_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            # Jika karakter adalah huruf, maka dekripsi dengan aturan Vigenere Cipher
            char_value = ord(char.lower()) - 97
            key_value = int(key[key_index]) - 1
            new_char_value = (char_value - key_value) % 26
            new_char = chr(new_char_value + 97)
            key_index = (key_index + 1) % len(key)
        else:
            # Jika karakter bukan huruf, maka tidak didekripsi
            new_char = char
        plain_text += new_char
    return plain_text

# Contoh penggunaan
plain_text = "PESAN RAHASIA"
key = "254"
cipher_text = vigenere_encrypt(plain_text, key)
print("Pesan asli         :", plain_text)
print("Kunci              :", key)
print("Pesan terenkripsi  :", cipher_text)
print("Pesan terdekripsi  :", vigenere_decrypt(cipher_text, key))
