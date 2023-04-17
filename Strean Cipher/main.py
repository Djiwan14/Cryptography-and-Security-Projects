def bin_string_to_string(binary_string):
    # This function receives a binary string as an argument and returns the corresponding ASCII string
    return ''.join(chr(int(binary_string[item * 8:item * 8 + 8], 2)) for item in range(len(binary_string) // 8))


def lfsr_generator(seed, mask, n):
    # This function implements the LFSR algorithm for generating a pseudorandom bit sequence
    seed = int(seed, 2)
    mask = int(mask, 2)
    key = ''

    for i in range(n):
        feedback = 0
        for j in range(n):
            if mask & (1 << j):
                # If the j-th bit of the mask is set to 1, then use it for feedback
                feedback ^= (seed >> j) & 1
        # Shift the seed one bit to the right and add the feedback bit to the leftmost bit
        seed = (seed >> 1) | (feedback << 7)
        key = key + str(feedback)

    return key


def xor(string1, string2):
    # This function performs the XOR operation between two strings of equal length
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string1, string2)])


def read_char_and_return_key():
    code = ""
    mask = '10000011'
    key = ""
    with open("data_stream.txt", mode="r") as file:
        while True:
            c = file.read(1)  # Read one character at a time
            if not c:
                break
            char_seed = format(ord(c), '08b')  # Convert the character to a binary string
            char_key = bin_string_to_string(lfsr_generator(char_seed, mask, 8))  # Generate the key for the character
            key = key + char_key
            xor_result = xor(char_key, c)  # Perform the XOR operation between the key and the character
            code = code + xor_result

    return code, key


def xor_decrypt(string1, string2):
    # This function performs the XOR decryption between the key and the ciphertext
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string1, string2)])


def main():
    txt = "this is a stream of data to be transferred securely."
    code, total__key = read_char_and_return_key()  # Read the characters from the input file and generate the key
    print(code)
    plaintext = xor_decrypt(code, total__key)  # Decrypt the ciphertext using the key
    print(plaintext)


if __name__ == "__main__":
    main()
