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

def cesar_algotithm(text, k):
    text_symbols = [x for x in text]
    encoded_text = ''
    for symbol in text_symbols:
        encoded_text += english_alphabet[((english_alphabet_pos[symbol]+k)%len(english_alphabet))]
    return encoded_text

def decode_cesar(text, k):
    text_symbols = [x for x in text]
    decoded_text = ''
    for symbol in text_symbols:
        decoded_text += english_alphabet[((english_alphabet_pos[symbol]-k)%len(english_alphabet))]
    return decoded_text

text = 'cesar el emperador ha sido asesinado'
encode = cesar_algotithm(text, 3)
decode = decode_cesar(encode, 3)
print(encode)
print(decode)