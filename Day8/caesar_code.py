alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(text_p, shift_p, direction_p):
    new_word = ""
    if direction_p == "decode":
        shift_p *= -1
    for letter in text_p:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter = alphabet[letter_index + shift_p]
            new_word += new_letter
        else:
            new_word += letter
    print(f"Here is de {direction}d code: {new_word}")

keep = True
while keep:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26

        caesar(text, shift, direction)
        decision = input("Do you want to continue? [Y] for YES || [N] for NO ").lower()
        if decision == "n":
            keep = False
    else:
        print("Please, type ENCODE our DECODE, only! ")
