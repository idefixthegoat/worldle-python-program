



#inports
import random

#open the file
myFile = open("wordlist")

#read the file and make a list and checking it twice 
wordData = myFile.read().split("\n")

listLength = len(wordData)

random.randint( 0 , listLength )

print(wordData[0] )

randindex = random.randint( 0 , listlength - 1)

wordle = wordlist[ randindex ]
while True:
    guess = input("enter a guess: ").upper()
    
    if guess == wordle:
        print("you win!")
        break
    
    if len(guess) != 5:
        print("type a 5 letter word")
        guess = input("enter a guess: ").upper()
    
    for i in range(5):
        print( wordle[i] + " - " + guess[i] )
        result = result + "-"
        
    for i in range(5):
        if guess[i] == wordle[i]:
            result = result + guess[i]
        elif guess[i] in wordle:
            result = result + guess[i] + "* "
        else:
            result = result + " - "
    print(result)