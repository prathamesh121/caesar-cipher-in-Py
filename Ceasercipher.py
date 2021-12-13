alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

global cipher_text


def encrypt(t=text, s=shift):
    cipher_text = ""
    for letter in t:
        pos = alphabet.index(letter)
        new_pos = pos + s
        new_letter = alphabet[new_pos]
        cipher_text += new_letter

    print(f"The messgage is {cipher_text}")


def decode(ct=text, sd=shift):
    plain_txt = ""
    for letter in ct:
        pos = alphabet.index(letter)
        new_pos = pos - sd
        plain_txt += alphabet[new_pos]

    print(f"The Decoded messge is {plain_txt}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decode(text, shift)
