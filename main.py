import fileFunctions as ff
import string
from bs4 import BeautifulSoup as bs
import requests as rq
import random as rand
import collections as coll
import time
import re
#Imports

# Function to convert  
def listToString(s): 
#initialize an empty string
    str1 = "" 
#return string  
    return (str1.join(s)).strip()

words = []
        
r_html = rq.get('https://www.thefreedictionary.com/5-letter-words.htm')
#Requests HTML from the specified webpage

soup = bs(r_html.text, 'html.parser')
#Organizes the HTML into a parsable format

        
for i in soup.find_all('a'):
    if len(str(i.string)) == 5:
        words.append(str(i.string))
#Appends the text found within the <a> attribute to the Words list so long as it meats the specified conditon

count_times_played = ff.fileFunctions.readDictFile('TimesPlayed.txt')
play_again = 'y'
while 'y' in play_again:
#Primary outer loop. Repeats once every *GAME*.
    choice = rand.choice(words).lower()
    #Chooses word from Words
    user_name = ''
    lowercase = string.ascii_lowercase
    while user_name == '':
        count = 0
        user_name = str(input("What are your initials? "))
        for letter in user_name.lower():
            if letter not in lowercase:
                count += 1
        if count > 0:
            print("Please enter only your initials.")
            user_name = ''
    #Asks user for name
    guess_count = 5
    #Initializes count of guess remaining
    
    
    choiceWord = coll.Counter(choice)
    #Creates Dict of Choice word using Key:Value --> Value:Count(Value) Pairs

    #See Logic:
        #{} for i in range(len(choice)):
            #if choice[i] not in choiceWord:
            #   choiceWord[choice[i]] = 1
            #else:
            #    choiceWord[choice[i]] += 1

    time.sleep(1)
    print('\n' + "Welcome to Wordle, {}! A fun, interactive game all about educated guesses.".format(user_name.upper()))
    time.sleep(2.5)
    print("Letters surrounded by the '[]' character indicate that is the correct letter in the correct spot.")
    time.sleep(2)
    print("Letters surrounded by the '{}' character indicate that is the correct letter in the *incorrect* spot.")
    time.sleep(2)
    print("Letters not surrounded by anything indicate that is the incorrect letter.")
    time.sleep(2)
    print('\n' + "You have a total of {} guesses remaining. Good luck!".format(guess_count))


    guess = str(input('Pick a 5 letter word: '))
    #User guess
    result = "\n"
    #Initializes Result variable
    choiceCopy = choiceWord.copy()
    #Copies 
    
    while guess != choice:
    #Primary inner loop. Repeats once every *GUESS*. So, max 5(counting 1st) per game.
        replaceDict = {}
        if guess_count > 1:
            if len(guess) != 5 or listToString(re.findall('\D',guess)) != guess:
                print("Please enter a 5 letter word, {}.".format(user_name.upper()))
                guess = str(input('Pick a 5 letter word: '))
            else:
                for i in range(len(choice)):
                    if guess[i] == choice[i]:
                        replaceDict[i] = "[" + guess[i] + "]"
                        choiceWord[guess[i]] -= 1
                for i in range(len(choice)):
                    if i in replaceDict:
                            result += replaceDict[i]
                    elif guess[i] in choiceWord and choiceWord[guess[i]] > 0:
                            result += "{" + guess[i] + "}"
                            choiceWord[guess[i]] -= 1
                    else:
                        result += guess[i]
                
                choiceWord = choiceCopy.copy()
                result += '\n'
                print(result)
                guess_count -= 1
                print("You have a total of {} guesses remaining.".format(guess_count))
                guess = str(input('Pick a 5 letter word: '))
        else:
            break
    
    if guess == choice and guess_count != 0:  
        ff.fileFunctions.incrementDict_N(count_times_played, user_name.lower(),1)


        invert_guess_count = 5 - (guess_count) + 1
        print('\n' + "You nailed it in {} guesses!".format(invert_guess_count))
        time.sleep(2)
        print("Great job {}, we're very proud of you.".format(user_name.upper())+'\n')
        time.sleep(3.5)
        
    else:
        print('\n' + "{}... you've failed.".format(user_name.upper()))
        time.sleep(2)
        print("The word was {}.".format(choice.lower()))
        time.sleep(2)
        print("But that's ok! We still believe in you." + '\n')
        time.sleep(3.5)

    play_again = str(input('Would you like to play again? (Yes/No) '))
    
ff.fileFunctions.createDictFile('TimesPlayed.txt',count_times_played)

get_score = str(input("Would you like to check highscores?(Yes/No) "))

while 'y' in get_score.lower():
    check_name = str(input('Enter a name here: '))
    d = ff.fileFunctions.readDictFile('TimesPlayed.txt')
    if check_name.lower() in d:
        print("{} has won this game {} times!".format(
            ff.fileFunctions.getScore('TimesPlayed.Txt',check_name)[0].upper(),ff.fileFunctions.getScore('TimesPlayed.txt',check_name)[1])
            )
        get_score = str(input("Would you like to check more highscores?(Yes/No) "))
    else:
        print("Name does not exist.")
        get_score = str(input("Would you like to check more highscores?(Yes/No) "))