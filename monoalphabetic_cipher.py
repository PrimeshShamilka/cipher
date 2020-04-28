import sys, random

def converter(key,plain_text, mode, letters):

    if mode == 'encrypt':
        translated = encryptMessage(key, plain_text, letters)
    elif mode == 'decrypt':
        translated = decryptMessage(key, plain_text, letters)
    
    return translated

def encryptMessage(key, message, letters):
    return translateMessage(key, message, 'encrypt', letters)


def decryptMessage(key, message, letters):
    return translateMessage(key, message, 'decrypt', letters)


def translateMessage(key, message, mode, letters):
    translated = ''
    if mode == 'decrypt':

        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        letters, key = key, letters

    for symbol in message:
        if symbol in letters:
            # encrypt/decrypt the symbol
            symIndex = letters.find(symbol)
            translated += key[symIndex]

        else:
            translated += symbol

    return translated






