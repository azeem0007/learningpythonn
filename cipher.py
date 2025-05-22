import string


alphabets=list(string.ascii_lowercase)
print(alphabets)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text=input("enter the text: ").lower()
shift=int(input("enter the shift number: "))

def encrypt(original_text ,shift_amount):
    encoded_cipher=""
    for char in original_text:
        ciper_text =alphabets.index(char)
        ciper_text= ciper_text + shift_amount
        if ciper_text >= 25:
            encoded_cipher = encoded_cipher + alphabets[ciper_text-26]   
        else:
            encoded_cipher = encoded_cipher + alphabets[ciper_text]
    print(encoded_cipher)


def decrypt(original_text ,shift_amount):
    decoded_cipher=""
    for char in original_text:
        deciper_text =alphabets.index(char)
        deciper_text= deciper_text - shift_amount
        decoded_cipher= decoded_cipher + alphabets[deciper_text]
    print(decoded_cipher)


if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Invalid input!")

