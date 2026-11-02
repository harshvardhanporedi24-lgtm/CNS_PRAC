from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate public and private keys
def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()

    print("\nKeys generated successfully!")
    return private_key, public_key

# Generate digital signature
def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),
        hashes.SHA256()
    )
    print("\nMessage signed successfully!")
    print("Digital Signature:", signature.hex())
    return signature


# Verify digital signature
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            hashes.SHA256()
        )
        print("\nSignature is VALID!")

    except InvalidSignature:
        print("\nSignature is INVALID!")
        print("Message integrity verification failed.")


# Main program
def main():
    private_key = None
    public_key = None
    message = None
    signature = None

    while True:
        print("\n===== DIGITAL SIGNATURE SYSTEM =====")
        print("1. Generate Keys")
        print("2. Sign Message")
        print("3. Verify Signature")
        print("4. Modify Message and Verify")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            private_key, public_key = generate_keys()
            message = None
            signature = None

        elif choice == '2':
            if private_key is None:
                print("\nGenerate keys first!")
            else:
                message = input("Enter the message: ")
                signature = sign_message(private_key, message)

        elif choice == '3':
            if signature is None:
                print("\nSign a message first!")
            else:
                verify_signature(public_key, message, signature)

        elif choice == '4':
            if signature is None:
                print("\nSign a message first!")
            else:
                modified_message = input("Enter modified message: ")
                verify_signature(public_key, modified_message, signature)

        elif choice == '5':
            print("\nExiting program...")
            break
        else:
            print("\nInvalid choice! Try again.")
main()


# 1
# 2
# Hello World
# 3
# 4
# Hello World123
# 5
