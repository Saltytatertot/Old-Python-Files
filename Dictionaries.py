#Dictionaries are what we call key value pairs.
#Access these, use key
#converts 3 digit month name to full name

#Dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions["Dec"])
print(monthConversions["Sep"])
print(monthConversions.get("LUV","Ain't here bud. Sorry."))
#Returns None for something not in dictionary

#Can be numbers as long as the keys are unique.
#Useful for assigning values to other values.
