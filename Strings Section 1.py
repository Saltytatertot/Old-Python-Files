#Strings Section 1
#Tatum Gray
#4/23/2016

def vowel(word):
    a = word.count('a')
    e = word.count('e')
    i = word.count('i')
    o = word.count('o')
    u = word.count('u')
    A = word.count('A')
    E = word.count('E')
    I = word.count('I')
    O = word.count('O')
    U = word.count('U')
    print(a + e + i + o + u + A + E + I + O + U)
word = input("Enter a word. >> ")
vowel(word)
