def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
