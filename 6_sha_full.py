def left_rotate(value, bits):
    return ((value << bits) | (value >> (32 - bits))) & 0xffffffff
    
def sha1(message):
    data = bytearray(message.encode())
    original_length = len(data) * 8

    # Padding
    data.append(0x80)
    while len(data) % 64 != 56:
        data.append(0)

    data += original_length.to_bytes(8, 'big')

    # Initial hash values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Process each 512-bit block
    for i in range(0, len(data), 64):
        block = data[i:i + 64]
        w = []

        for j in range(16):
            w.append(int.from_bytes(block[j*4:j*4+4], 'big'))

        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if j < 20:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff

            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}'


# Main program
msg1 = input("Enter original message: ")
msg2 = input("Enter modified message: ")

hash1 = sha1(msg1)
hash2 = sha1(msg2)

print("\nOriginal Message:", msg1)
print("SHA-1 Digest:", hash1)

print("\nModified Message:", msg2)
print("SHA-1 Digest:", hash2)

if hash1 != hash2:
    print("\nBoth digests are different.")
    print("Small change in input produces a different digest.")
else:
    print("\nBoth digests are same.")
    


# Test Case 1:
# Original Message: Hello
# Modified Message: Hello1

# Test Case 2:
# Original Message: hello
# Modified Message: Hello

# Test Case 3:
# Original Message: Computer Networks
# Modified Message: Computer Network

# Test Case 4:
# Original Message: 123456
# Modified Message: 123457

# Test Case 5:
# Original Message: Cryptography is used for secure communication.
# Modified Message: Cryptography is used for secure communications.
