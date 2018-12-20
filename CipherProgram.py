def substitutionCipher (message,cipherString):
    alphabet = #use the ascii_lowercase string constant to put the lowercase letters in alphabet
    encryptedMessage = ""
    message = #use the lower string function() to change message to lowercase
    for letter in range(len(message)):
        found = False
        #put another for loop here using alphaLetter and length of alphabet (look 2 lines up)
             if(message[letter] == alphabet[alphaLetter]):
                #add cipherString[alphaLetter] to encryptedMessage (look 3 lines down)
                #set found equal to true
        if found == False:
            encryptedMessage += message[letter]
    return encryptedMessage

userMessage = #ask user to input their message
mappingString = #ask user to input their cipher string
print("The encrypted message = " + #run substitutionCipher function sending in the correct argument)
