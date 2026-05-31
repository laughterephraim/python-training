#Building a Caesar Cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[0:5]
print(shifted_alphabet)

