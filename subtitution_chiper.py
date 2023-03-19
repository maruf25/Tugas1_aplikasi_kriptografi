import random

def generate_key():
    """Menghasilkan kunci acak dengan cara mengacak alfabet"""
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabets = "".join(random.sample(alphabets, len(alphabets)))
    return shuffled_alphabets

def encrypt(message, key):
    """Mengenkripsi pesan dengan metode Substitution Cipher"""
    cipher_text = ""
    for char in message:
        if char.isalpha():
            # Mengganti karakter dengan karakter pada kunci
            char_index = ord(char.upper()) - 65
            cipher_char = key[char_index]
            cipher_text += cipher_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    """Mendekripsi pesan dengan metode Substitution Cipher"""
    message = ""
    for char in cipher_text:
        if char.isalpha():
            # Mengganti karakter dengan karakter asli pada alfabet
            char_index = key.index(char.upper())
            message_char = chr(char_index + 65)
            if char.islower():
                message_char = message_char.lower()
            message += message_char
        else:
            message += char
    return message

# Contoh penggunaan
plain_text = "PESAN RAHASIA"
key = generate_key()
cipher_text = encrypt(plain_text, key)
print("Pesan asli         :", plain_text)
print("Kunci acak         :", key)
print("Pesan terenkripsi  :", cipher_text)
print("Pesan terdekripsi  :", decrypt(cipher_text, key))
