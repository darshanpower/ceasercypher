def caesar_cipher(text, shift):
     result = ""
     for char in text:
         if char.isupper():
             result += chr((ord(char) + shift - 65) % 26 + 65)
         elif char.islower():
             result += chr((ord(char) + shift - 97) % 26 + 97)
         else:
             result += char
 
     return result
    if __name__ == "__main__":
     plaintext = "suraj!"
     shift = 3
     encrypted_text = caesar_cipher(plaintext, shift)
     print(f"Plaintext: {plaintext}")
     print(f"Encrypted: {encrypted_text}")
     decrypted_text = caesar_cipher(encrypted_text, -shift)
     print(f"Decrypted: {decrypted_text}")