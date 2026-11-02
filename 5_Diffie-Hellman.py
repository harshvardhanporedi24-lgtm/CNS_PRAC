
# Diffie-Hellman Key Exchange with MITM Attack

# Function to generate public key
def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)


# Function to generate shared secret
def generate_shared_key(public_key, private_key, p):
    return pow(public_key, private_key, p)


print("====================================")
print(" DIFFIE-HELLMAN WITH MITM ATTACK")
print("====================================")

# Taking public parameters from user
p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

# Taking private keys
alice_private = int(input("Enter Alice's private key: "))
bob_private = int(input("Enter Bob's private key: "))

print("\n--- NORMAL DIFFIE-HELLMAN EXCHANGE ---")

# Generate public keys
alice_public = generate_public_key(alice_private, g, p)
bob_public = generate_public_key(bob_private, g, p)

print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

# Generate shared secret keys
alice_shared = generate_shared_key(
    bob_public, alice_private, p
)

bob_shared = generate_shared_key(
    alice_public, bob_private, p
)

print("\nAlice's Shared Key:", alice_shared)
print("Bob's Shared Key:", bob_shared)

if alice_shared == bob_shared:
    print("Normal Key Exchange Successful!")


# MITM ATTACK
print("\n--- MAN IN THE MIDDLE ATTACK ---")

# Eve's private keys
eve_private1 = int(input("Enter Eve's first private key: "))
eve_private2 = int(input("Enter Eve's second private key: "))

# Eve generates public keys
eve_public1 = generate_public_key(eve_private1, g, p)
eve_public2 = generate_public_key(eve_private2, g, p)

print("\nEve intercepts both public keys.")

print("Eve sends first public key to Alice:", eve_public1)
print("Eve sends second public key to Bob:", eve_public2)

# Alice calculates key with Eve
alice_eve = generate_shared_key(
    eve_public1, alice_private, p
)

# Eve calculates key with Alice
eve_alice = generate_shared_key(
    alice_public, eve_private1, p
)

# Bob calculates key with Eve
bob_eve = generate_shared_key(
    eve_public2, bob_private, p
)

# Eve calculates key with Bob
eve_bob = generate_shared_key(
    bob_public, eve_private2, p
)

print("\n--- GENERATED SHARED KEYS ---")

print("Alice-Eve Key:", alice_eve)
print("Eve-Alice Key:", eve_alice)

print("Bob-Eve Key:", bob_eve)
print("Eve-Bob Key:", eve_bob)

# Verify attack
if alice_eve == eve_alice and bob_eve == eve_bob:
    print("\nEve successfully established two shared keys!")

if alice_eve != bob_eve:
    print("Alice and Bob have different shared keys.")
    print("MITM Attack Successful!")


# Message interception
print("\n--- MESSAGE INTERCEPTION ---")

message = input("\nEnter message from Alice to Bob: ")

print("\nAlice sends:", message)
print("Eve intercepts and reads:", message)

modified_message = input("Enter modified message by Eve: ")

print("Eve forwards modified message to Bob:")
print(modified_message)

# Enter prime number (p): 23
# Enter generator (g): 5
# Enter Alice's private key: 6
# Enter Bob's private key: 15

# Enter Eve's first private key: 7
# Enter Eve's second private key: 9

# Enter message from Alice to Bob: Transfer Rs. 5000
# Enter modified message by Eve: Transfer Rs. 50000