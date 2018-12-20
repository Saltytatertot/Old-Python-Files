secret_word = "giraffe"
guess = ""
guess_count = 0
guess_Limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_Limit:   
        guess = input("Enter guess:  ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, NERD! GO BACK TO SCHOOL!")
else:
    print("You got it.")
