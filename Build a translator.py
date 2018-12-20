
#converting real words into fucking gibberish.
#where every vowel converts to g. |:

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase and see what it is in the made up language this guy makes:  ")))







#Comments are used for us humans. >:]
'''
grouped comments
are used with 3 of those apostrophy.
'''

#hashtags or pounds are fine tho. apparently the best way to do it.
#comments are also used for getting rid of code without actually deleting it.
