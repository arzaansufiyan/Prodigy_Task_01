def caesar_cipher(text, shift, direction):
    # Adjust shift for decryption
    if direction == 'decrypt':
        shift = -shift

    result = ""
    
    # Iterate through each character in the text
    for char in text:
        if char.isalpha():
            # Handle upper and lowercase letters separately
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters remain the same
            result += char
            
    return result

# Get input from the user
text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
direction = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Encrypt or decrypt the message
result = caesar_cipher(text, shift, direction)

# Output the result
print(f"The {direction}ed message is: {result}")
