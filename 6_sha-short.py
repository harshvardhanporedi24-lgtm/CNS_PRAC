import hashlib

def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

msg1 = input("Enter original message: ")
msg2 = input("Enter modified message: ")

hash1 = sha1(msg1)
hash2 = sha1(msg2)

print("\nOriginal Hash:", hash1)
print("Modified Hash:", hash2)

if hash1 == hash2:
    print("Both hashes are same.")
else:
    print("Both hashes are different!")
    print("Avalanche Effect Demonstrated.")
  
# Enter original message: Hello
# Enter modified message: Hello1
