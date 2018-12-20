#Strings Section 3
#Tatum Gray
#5/1/2016

def removeDups(string):
    chars = ''
    vowels = ('a','e','i','o','u')
    for x in string:
        if x not in vowels:
            chars = chars + x
    return chars

print(removeDups("mississippi"))
