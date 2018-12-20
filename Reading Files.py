#Reading from files outside of other files using the Read command

#enter directory information. If they are in the same directory, then nevermind

#"r" read only, "w" write new info, "a" basically add to the existing code without changing it
#and "r+" read and write.

#good to store in a variable
#be sure to close file before and after editing.
character_file = open("Characters_and_their_class.txt", "r") #"a" writes where cursor is.
#figuring out what is in the file and making sure it can be read.

#character_file.write("Jackie - Solo") #writes a new value

#can print out multiple lines
#print(character_file.readline())
#print(character_file.readline())
#print(character_file.readline())
#if file is writtable, .read will False.


#creates a list for the file
print(character_file.readlines()[0])
character_file.close()

