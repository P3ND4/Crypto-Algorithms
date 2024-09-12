english_alphabet_pos = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
    'z': 25, ' ': 26
}
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z', ' ']

def vegenere_algorithm(alphabet, alphabet_pos, text, key):
    encoded_text = ''
    for i in range(0, len(text)):
        encoded_text += alphabet[ (alphabet_pos[text[i]] + alphabet_pos[key[i%len(key)]])%len(alphabet_pos)]
    return encoded_text


def decode_vegenere(alphabet, alphabet_pos, text, key):
    decoded_text = ''
    for i in range(0, len(text)):
        decoded_text += alphabet[ (alphabet_pos[text[i]] - alphabet_pos[key[i%len(key)]])%len(alphabet_pos)]
    return decoded_text

text = 'cesar el emperador ha sido asesinado'
key = 'clave'

encoded = vegenere_algorithm(english_alphabet, english_alphabet_pos, text, key)
decoded = decode_vegenere(english_alphabet, english_alphabet_pos, encoded, key)

print(encoded)
print(decoded)