import collections
import string


def caesar_cypher_dequeu(message, shift_value):
    alphabet = string.ascii_uppercase
    dequeue_alphabet = collections.deque(alphabet)
    dequeue_alphabet.rotate(shift_value)

    shifted_alphabet = ''.join(dequeue_alphabet)
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)




def caesar_cypher_slice(message,shift_value):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift_value:] + alphabet[:shift_value]

    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


print(caesar_cypher_slice('meow meow', 1))

