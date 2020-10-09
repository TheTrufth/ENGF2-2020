import enchant # A spell checking library  https://pypi.org/project/pyenchant/ for more info
d = enchant.Dict("en_US")
alphabet = {                   # Unmodified library
        "A": "1",
        "B": "2",
        "C": "3",
        "D": "4",
        "E": "5",
        "F": "6",
        "G": "7",
        "H": "8",
        "I": "9",
        "J": "10",
        "K": "11",
        "L": "12",
        "M": "13",
        "N": "14",
        "O": "15",
        "P": "16",
        "Q": "17",
        "R": "18",
        "S": "19",
        "T": "20",
        "U": "21",
        "V": "22",
        "W": "23",
        "X": "24",
        "Y": "25",
        "Z": "26"
        }
def ciphershift(cipherword, shift):             # This function takes in an encrypted word and
    alphabetcopy = alphabet.copy()              # shift number to and returns the plaintext and cipheralphabet used
    for letter, number in alphabetcopy.items():
        if (int(number) + shift) > 26:
            alphabetcopy.update({letter: str(((int(number) + shift)%26))})
        else:
            alphabetcopy.update({letter: str(int(number) + shift)})

    ciphertextalphabet = {}
    for x, y in alphabet.items():
        for i, j in alphabetcopy.items():
            if y == j:
                ciphertextalphabet.update({i: x})

    plaintext = ""
    for let in cipherword:
        plaintext += ciphertextalphabet.get(let)
    
    return plaintext, ciphertextalphabet

def break_cipher(cipherword):           # Main function to find compatible words using the spell checker imported earlier
    for num in range(26):
        output = ciphershift(cipherword, num)
        testword = output[0]
        cipheralphabet = output[1]
        if d.check(testword) == True:
            print("The decrypted word is: " + testword + "\n")
            print("The ciphertext alphabet: " + str(cipheralphabet) + "\n")
            
    
    


cipherword = input("Enter a word to decrypt (CAPS) \n").upper() # Asking the user for a encrypted word using ceaser cipher
break_cipher(cipherword) # Starting the computation


