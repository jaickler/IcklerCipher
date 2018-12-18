import string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_ceaser(Message, Key):
    Encoded_Message = ''
    Message = Message.lower()
    for letter in Message:
        Encoded_Message += alphabet[alphabet.index(letter) + (Key % 26)]
    return Encoded_Message

def decode_ceaser(Encoded_Message, Key):
    Decoded_Message = ''
    Encoded_Message = Encoded_Message.lower()
    for letter in Encoded_Message:
        Decoded_Message += alphabet[alphabet.index(letter) - (Key % 26)]
    return Decoded_Message

print(decode_ceaser(encode_ceaser("TEST", 4), 4))
        