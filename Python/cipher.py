# The function should take two parameters: the text to encrypt and the shift amount
shift_amount = 5
message = "This is an example of the text to be encrypted."
def cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decipher(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            decrypted_text += chr((ord(char) - 65 - shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift_amount) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

encryption = cipher(message, shift_amount)
decryption = decipher(encryption, shift_amount)
print("Encrypted text: " + encryption)
print("Decrypted text: " + decryption)
