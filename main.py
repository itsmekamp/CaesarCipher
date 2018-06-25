#Caesar Cipher by Kamp
#v1.0

originalAlph = "abcdefghijklmnopqrstuvwxyz"
alteredAlph = "defghijklmnopqrstuvwxyzabc"

result = ""

def encode(input):
    global result
    for letter in input:
        if letter in originalAlph:
            originalIndex = originalAlph.index(letter)
            alteredLetter = alteredAlph[originalIndex]
            result += alteredLetter
        elif letter == " ":
            result += " "
        else:
            result += letter
    print(result)

def decode(input):
    global result
    for letter in input:
        if letter in originalAlph:
            alteredIndex = alteredAlph.index(letter)
            originalLetter = originalAlph[alteredIndex]
            result += originalLetter
        elif letter == " ":
            result += " "
        else:
            result += letter
    print(result)

print("Welcome to Caesar Cipher Encoder/Decoder by Kamp")
choice = input("Do you want to encode or decode?\n")
if choice == "encode":
    rawInput = input("Enter your word\n")
    encode(rawInput)
elif choice == "decode":
    rawInput = input("Enter your word\n")
    decode(rawInput)