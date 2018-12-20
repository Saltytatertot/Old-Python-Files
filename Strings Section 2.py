#Strings Section 2
#Tatum Gray
#4/23/2016

import string

def substitutionCipher(message,cipherString):
    alphabet = string.ascii_lowercase
    encryptedMessage = ""
    message = alphabet.lower()
    for letter in range(len(message)):
        found = False
        for alphaLetter in range(len(alphabet)):
            if(message[letter] == alphabet[alphaLetter]):
                cipherString[alphaLetter] += encryptedMessage
                found = True
        if found == False:
            message[letter] += encryptedMessage
    return encryptedMessage

userMessage = input("Enter in a message. >> ")
mappingString = input("Enter the cipher. >> ")
print("The encrypted message =" + substitutionCipher(userMessage,mappingString))
               
