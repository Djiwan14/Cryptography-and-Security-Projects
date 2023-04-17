import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def start():
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    global word
    word = input(f"Please type the word you want to {choice}\n")
    global length_of_input
    length_of_input = len(word)
    random_keyword(length_of_input)
    if choice == 'encode':
        encoding(word)
    elif choice == 'decode':
        decoding(word)

def encoding(word):
    # This function takes as a parameter word which was entered by the user and randomly generates keyword
    # the same length as the inputted word itself. Then using OTP method indexes of these two words are being added and it
    # creates new encrypted word.
    global encrypted_word
    encrypted_word = ""
    original_positions = []
    shift_positions = []
    for letter in word:
        original_positions.append(alphabet.index(letter))
    print(f"Indexes of plain text = {original_positions}")
    for letter in keyword_word:
        shift_positions.append(alphabet.index(letter))
    print(f"Indexes of keyword text = {shift_positions}")
    positions = [original_positions, shift_positions]
    indexes = [sum(x) for x in zip(*positions)]
    print(f"Indexes of encrypted text = {indexes}")
    for index in indexes:
        encrypted_word += alphabet[index]
    print(f"Encrypted text: {encrypted_word}")




def decoding(word):
    # This function takes as a parameter word which was entered by the user and randomly generates keyword
    # the same length as the inputted word itself. Then using OTP method indexes of these two words are being substracted
    # and it decrypts the encrypted word.
    decrypted_word = ""
    original_positions = []
    shift_positions = []
    for letter in word:
        original_positions.append(alphabet.index(letter))
    print(f"Indexes of plain text = {original_positions}")
    for letter in keyword_word:
        shift_positions.append(alphabet.index(letter))
    print(f"Indexes of keyword text = {shift_positions}")
    indexes = []
    for item1, item2 in zip(shift_positions, original_positions):
        indexes.append(item1 - item2)
    print(f"Indexes of decrypted text = {indexes}")
    for index in indexes:
        decrypted_word += alphabet[index]
    print(f"Decrypted text: {decrypted_word}")


def random_keyword(length):
    # this method creates random keyword for inputted by user words making them same length as inputted words
    global keyword_word
    keyword_word = ""
    keyword_array = []
    for i in range(length):
        keyword_array.append(random.choice(alphabet))
    for letter in keyword_array:
        keyword_word += letter
    print(f"Keyword : {keyword_word}")

start()
