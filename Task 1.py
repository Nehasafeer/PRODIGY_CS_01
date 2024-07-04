def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D) ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice, please enter 'E' to encrypt or 'D' to decrypt.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        another = input("Would you like to perform another operation? (Y/N) ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
