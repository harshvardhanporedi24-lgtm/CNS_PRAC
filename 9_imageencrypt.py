
# Secure Image Transmission using AES-256-GCM
# User 1: Alice (Sender)
# User 2: Bob (Receiver)

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag


# Generate encryption key from password
def generate_key(password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )

    return kdf.derive(password.encode())


# USER 1: ALICE - SENDER
def sender():

    print("\n===== ALICE : SENDER =====")

    image_path = input("Enter image path: ")
    password = input("Enter shared password: ")

    if not os.path.isfile(image_path):
        print("Image not found!")
        return

    # Read original image
    with open(image_path, "rb") as file:
        image_data = file.read()

    # Generate salt and nonce
    salt = os.urandom(16)
    nonce = os.urandom(12)

    # Generate AES-256 key
    key = generate_key(password, salt)

    # Encrypt image
    aes = AESGCM(key)
    encrypted_data = aes.encrypt(nonce, image_data, None)

    # Save encrypted image
    with open("encrypted_image.enc", "wb") as file:
        file.write(salt + nonce + encrypted_data)

    print("\nAlice encrypted the image successfully!")
    print("Encrypted image: encrypted_image.enc")
    print("Image sent securely through the network.")


# USER 2: BOB - RECEIVER
def receiver():

    print("\n===== BOB : RECEIVER =====")

    encrypted_path = input("Enter received encrypted file path: ")
    password = input("Enter shared password: ")

    if not os.path.isfile(encrypted_path):
        print("Encrypted file not found!")
        return

    # Read encrypted image
    with open(encrypted_path, "rb") as file:
        data = file.read()

    if len(data) < 44:
        print("Invalid encrypted file!")
        return

    # Extract salt, nonce and ciphertext
    salt = data[:16]
    nonce = data[16:28]
    encrypted_data = data[28:]

    # Generate the same key
    key = generate_key(password, salt)

    try:

        # Decrypt image
        aes = AESGCM(key)
        decrypted_data = aes.decrypt(
            nonce, encrypted_data, None
        )

        # Save original image
        output_path = input("Enter received image name: ")

        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        print("\nBob decrypted the image successfully!")
        print("Received image:", output_path)
        print("Image integrity verified!")

    except InvalidTag:

        print("\nAuthentication Failed!")
        print("Wrong password or image was modified!")
        print("Image rejected by Bob.")


# MAIN PROGRAM
while True:

    print("\n================================")
    print(" SECURE IMAGE TRANSMISSION")
    print("================================")
    print("1. Alice - Send Image")
    print("2. Bob - Receive Image")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sender()

    elif choice == "2":
        receiver()

    elif choice == "3":
        print("Communication ended.")
        break

    else:
        print("Invalid choice!")

#pip install cryptography
# ================================
#  SECURE IMAGE TRANSMISSION
# ================================
# 1. Alice - Send Image
# 2. Bob - Receive Image
# 3. Exit
# Enter your choice: 1

# ===== ALICE : SENDER =====
# Enter image path: test.jpg
# Enter shared password: 123

# Alice encrypted the image successfully!
# Encrypted image: encrypted_image.enc
# Image sent securely through the network.

# ================================
#  SECURE IMAGE TRANSMISSION
# ================================
# 1. Alice - Send Image
# 2. Bob - Receive Image
# 3. Exit
# Enter your choice: 2

# ===== BOB : RECEIVER =====
# Enter received encrypted file path: photo.jpg
# Enter shared password: 1111
# Encrypted file not found!

# ================================
#  SECURE IMAGE TRANSMISSION
# ================================
# 1. Alice - Send Image
# 2. Bob - Receive Image
# 3. Exit
# Enter your choice: 2        

# ===== BOB : RECEIVER =====
# Enter received encrypted file path: encrypted_image.enc
# Enter shared password: 11111

# Authentication Failed!
# Wrong password or image was modified!
# Image rejected by Bob.

# ================================
#  SECURE IMAGE TRANSMISSION
# ================================
# 1. Alice - Send Image
# 2. Bob - Receive Image
# 3. Exit
# Enter your choice: 2

# ===== BOB : RECEIVER =====
# Enter received encrypted file path: encrypted_image.enc
# Enter shared password: 123
# Enter received image name: hello.jpg

# Bob decrypted the image successfully!
# Received image: hello.jpg
# Image integrity verified!

#################################################
#pip install requests cryptography(if external asks for url of image from internet)

#if external asks implementation of url of image from internet replace sender function
# def sender():

#     print("\n===== ALICE : SENDER =====")

#     # Take image URL from user
#     image_url = input("Enter image URL: ")
#     password = input("Enter shared password: ")

#     try:
#         # Download image from URL
#         response = requests.get(image_url, timeout=20)
#         response.raise_for_status()

#         image_data = response.content

#         if not image_data:
#             print("Downloaded image is empty!")
#             return

#         print("Image downloaded successfully!")

#         # Generate salt and nonce
#         salt = os.urandom(16)
#         nonce = os.urandom(12)

#         # Generate encryption key
#         key = generate_key(password, salt)

#         # Encrypt image
#         aes = AESGCM(key)
#         encrypted_data = aes.encrypt(nonce, image_data, None)

#         # Save encrypted image
#         with open("encrypted_image.enc", "wb") as file:
#             file.write(salt + nonce + encrypted_data)

#         print("\nAlice encrypted the image successfully!")
#         print("Encrypted file: encrypted_image.enc")
#         print("Image sent securely!")

#     except requests.RequestException as e:
#         print("Unable to download image:", e)