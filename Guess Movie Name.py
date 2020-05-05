import random  #library to choose random words from list of words.
name = input("What's your name: ")
print("Hello ",name.upper(), "! lets play Bollywood :-)")
print("Have a Good Time in Playing! ", name)
words = open("/home/devilyash/Documents/Python/Bollywood game/Movietitles.txt").readlines()
#words=[ 'Dil Chahta Hai', 'Maqbool', 'Chameli', 'Taare Zameen Par', 'Kahaani' ,
#        'Queen', 'Haider', 'Highway', 'Tamasha', 'Andhadhun', 'Dangal', 'Raajneeti', 
#        'Dhobi Ghat']

words = [x.lower() for x in words]
word = random.choice(words)
print("I have Selected a Movie for you but you should guess it first :-) ")
guesses = ''

turns = 9  # Because bollywood contain 9 character so 9 chances

while turns > 0:
    failed = 0  # Counting number of times user fails
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'  or char=='2' or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char == ":" or char == "."):
                print(char, end="")
            elif (char == " " or char == "-"):
                print(" / ", end="")
            elif (char == "'"):
                print("", end="")
            elif (char == "," or char == "("):
                break
            else:
                print("*",end="")
                failed += 1
    if failed == 0:
        print("\nCongratulations! You got it right.")                
        print("The word is: ",word.replace(",", "")) #because word it was printing contains "," at the end because we have put "," in text file. 
        break
    print("\n")
    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        # if not match wrong is given
        print("Wrong")
        print("You have ", +turns, 'turns left' )

        if turns == 0:
            print("You Loose! ")
            print(word, " was the movie you was supposed to guess")
            print("Better Luck next time. ")