import secrets
# Rotate bits to the left
def left_rotate(value, bits):
    return ((value << bits) | (value >> (8 - bits))) & 255
  
# Rotate bits to the right
def right_rotate(value, bits):
    return ((value >> bits) | (value << (8 - bits))) & 255

# Encryption function
def encrypt(plaintext, key):
    data = plaintext.encode()
    key = key.encode()
    nonce = secrets.token_bytes(8)
    ciphertext = bytearray()
    for i, byte in enumerate(data):
        k = key[i % len(key)] ^ nonce[i % 8] ^ ((i * 17 + 31) & 255)
        # Step 1: XOR
        value = byte ^ k
        # Step 2: Bit rotation
        value = left_rotate(value, 3)
        # Step 3: Position-based addition
        value = (value + (i * 7 + 13)) & 255
        ciphertext.append(value)
    return nonce.hex() + ":" + ciphertext.hex()

# Decryption function
def decrypt(encrypted_text, key):
    key = key.encode()
    nonce_hex, cipher_hex = encrypted_text.split(":")
    nonce = bytes.fromhex(nonce_hex)
    ciphertext = bytes.fromhex(cipher_hex)
    plaintext = bytearray()

    for i, byte in enumerate(ciphertext):
        k = key[i % len(key)] ^ nonce[i % 8] ^ ((i * 17 + 31) & 255)
        # Step 1: Reverse addition
        value = (byte - (i * 7 + 13)) & 255
        # Step 2: Reverse bit rotation
        value = right_rotate(value, 3)
        # Step 3: Reverse XOR
        value = value ^ k
        plaintext.append(value)
    return plaintext.decode()

# Main program
def main():
    while True:
        print("\n===== CUSTOM ENCRYPTION SYSTEM =====")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            message = input("Enter plaintext: ")
            key = input("Enter encryption key: ")
            if not key:
                print("Key cannot be empty!")
                continue
            encrypted = encrypt(message, key)
            print("\nEncrypted Ciphertext:", encrypted)
        elif choice == '2':
            encrypted = input("Enter ciphertext: ")
            key = input("Enter decryption key: ")
            if not key:
                print("Key cannot be empty!")
                continue
            try:
                decrypted = decrypt(encrypted, key)
                print("\nDecrypted Plaintext:", decrypted)
            except (ValueError, UnicodeDecodeError):
                print("\nInvalid ciphertext or incorrect key!")
        elif choice == '3':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice! Please try again.")
main()

# ===== CUSTOM ENCRYPTION SYSTEM =====
# 1. Encrypt Message
# 2. Decrypt Message
# 3. Exit

# Enter your choice: 1

# Enter plaintext: Hello World
# Enter encryption key: secret123

# Encrypted Ciphertext: [Generated nonce and ciphertext]

# Enter your choice: 2

# Enter ciphertext: [Paste generated ciphertext]
# Enter decryption key: secret123

# Decrypted Plaintext: Hello World
