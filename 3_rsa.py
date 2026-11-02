
# RSA Performance Analysis

import time
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

print("===== RSA PERFORMANCE ANALYSIS =====")

# Take inputs
key_sizes = list(map(int, input(
    "Enter RSA key sizes: ").split()))

msg_sizes = list(map(int, input(
    "Enter message sizes in bits: ").split()))

# Test different key sizes
for size in key_sizes:

    print("\nRSA Key Size:", size, "bits")

    # Measure key generation time
    start = time.perf_counter()

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=size
    )

    public_key = private_key.public_key()

    key_time = time.perf_counter() - start

    print("Key Generation Time:", key_time, "seconds")

    # Test different message sizes
    for bits in msg_sizes:

        message = os.urandom(bits // 8)

        # Maximum message size for OAEP-SHA256
        max_size = size // 8 - 66

        if bits <= 0 or bits % 8 != 0 or len(message) > max_size:
            print("\nMessage size", bits, "bits is not supported!")
            continue

        # Measure encryption time
        start = time.perf_counter()

        encrypted = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        encryption_time = time.perf_counter() - start

        # Measure decryption time
        start = time.perf_counter()

        decrypted = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        decryption_time = time.perf_counter() - start

        print("\nMessage Size:", bits, "bits")
        print("Encryption Time:", encryption_time, "seconds")
        print("Decryption Time:", decryption_time, "seconds")

        if message == decrypted:
            print("Message verified successfully!")

print("\nExperiment completed!")

#########for testing#############
# PS D:\College subjects\CNS\CNS PRAC> python .\3_rsa.py
# ===== RSA PERFORMANCE ANALYSIS =====
# Enter RSA key sizes: 1024 2048 3072
# Enter message sizes in bits: 64 128 256 512