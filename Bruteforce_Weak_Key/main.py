# Auxiliary func:
from binascii import hexlify, unhexlify
cipher_hex = b'1525053514291239'


def xor(string1, string2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(string1,string2)])

#function used for decryption 

def brute_crack(cipher_hex):

# We define first the given ciphertext as a byte string. Then we open the file declaring the list of most common words in English.
# The code then iterates over all possible lowercase letters as the first character of the key and combines it
# with the key pattern to form a complete key. It then decodes the ciphertext with the key to get the plaintext.
# Finally, the code checks to see if the decrypted plaintext is among the most common words in the English language.

# If so, the plaintext is returned.
# If no successful decoding is found, the code exits without returning anything.

    c = unhexlify(cipher_hex).decode()
    with open("common_words.txt", mode="r") as file:
        words = file.read().split()
    for letter in range(256):
        k = (chr(letter) + "@") * 4
        m = xor(c, k)
#         print(m)
        if m in words:
            return m
brute_crack(cipher_hex)
