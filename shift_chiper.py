def encrypt(message, key):
    """Mengenkripsi pesan dengan metode Shift Cipher"""
    cipher_text = ""
    for char in message:
        if char.isdigit():
            # Jika karakter adalah angka, maka geser sejumlah kunci (mod 10)
            new_char = str((int(char) + key) % 10)
        elif char.isupper():
            # Jika karakter adalah huruf kapital, maka geser sejumlah kunci (mod 26)
            new_char = chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            # Jika karakter adalah huruf kecil, maka geser sejumlah kunci (mod 26)
            new_char = chr((ord(char) + key - 97) % 26 + 97)
        else:
            # Jika karakter bukan huruf atau angka, maka tidak dienkripsi
            new_char = char
        cipher_text += new_char
    return cipher_text

def decrypt(cipher_text, key):
    """Mendekripsi pesan dengan metode Shift Cipher"""
    return encrypt(cipher_text, -key)

# Contoh penggunaan
plain_text = "PESAN RAHASIA"
key = 54
cipher_text = encrypt(plain_text, key)
print("Pesan asli         :", plain_text)
print("Kunci              :", key)
print("Pesan terenkripsi  :", cipher_text)
print("Pesan terdekripsi  :", decrypt(cipher_text, key))
