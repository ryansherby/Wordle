
class fileFunctions:

    def createDictFile(filename, dictionary):
        f = open(str(filename),'w')
        dic_tuple = dictionary.items()
        for pair in dic_tuple:
            f.write(str(pair[0])+" ")
            f.write(str(pair[1]) + "\n")
        f.close()
    #Creates a file and appends a dictionary to that file through spacially organized 'Key' + ' ' + 'Value' + '\n' pairs

    def readDictFile(filename):
            d = {}
            try:
                f = open(str(filename),'r')
                for line in f:
                    (key,value) = line.split()
                    d[key] = int(value)
                f.close()
                return d
            except:
                return d
    #Reads a file created and organized through the createDictFile method and returns the full dictionary

    def incrementDict_N(dictionary,key,n):
        if key not in dictionary:
            dictionary[key] = n
        else:
            dictionary[key] += n
    #Increments by N a Value according to a Dictionary and Key; Creates this Key:Value pair if necessary

    def getScore(filename, name):
            d = fileFunctions.readDictFile(filename)
            score = d[name.lower()]
            return [name, score]
    #Returns a specified Key:Value pair for a File read through the readDictFile method


class playWordle(fileFunctions):

    from bs4 import BeautifulSoup as bs
    import requests as rq
    import random as rand
    import collections as coll
    import time
    #Imports

    words = []
            
    r_html = rq.get('https://www.thefreedictionary.com/5-letter-words.htm')
    #Requests HTML from the specified webpage

    soup = bs(r_html.text, 'html.parser')
    #Organizes the HTML into a parsable format
    
            
    for i in soup.find_all('a'):
        if len(str(i.string)) == 5:
            words.append(str(i.string))
    #Appends the text found within the <a> attribute to the Words list so long as it meats the specified conditon

    count_times_played = fileFunctions.readDictFile('TimesPlayed.txt')
    play_again = 'y'
    while 'y' in play_again:
    #Primary outer loop. Repeats once every *GAME*.
        choice = rand.choice(words).lower()
        #Chooses word from Words
        user_name = str(input("What is your name? "))
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
        print('\n' + "Welcome to Wordle, {}! A fun, interactive game all about educated guesses.".format(user_name.capitalize()))
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
        result = ""
        #Initializes Result variable
        choiceCopy = choiceWord.copy()
        #Copies 
        
        
        while guess != choice:
        #Primary inner loop. Repeats once every *GUESS*. So, max 5(counting 1st) per game.
            replaceDict = {}
            #
            if guess_count > 1:
                if len(guess) != 5:
                    print("Please enter a 5 letter word, {}.".format(user_name.capitalize()))
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
            fileFunctions.incrementDict_N(count_times_played, user_name.lower(),1)
    

            invert_guess_count = 5 - (guess_count) + 1
            print('\n' + "You nailed it in {} guesses!".format(invert_guess_count))
            time.sleep(2)
            print("Great job {}, we're very proud of you.".format(user_name.capitalize())+'\n')
            time.sleep(3.5)
            
        else:
            print('\n' + "{}... you've failed.".format(user_name.capitalize()))
            time.sleep(2)
            print("The word was {}.".format(choice.lower()))
            time.sleep(2)
            print("But that's ok! We still believe in you." + '\n')
            time.sleep(3.5)
    
        play_again = str(input('Would you like to play again? (Yes/No) '))
        
    fileFunctions.createDictFile('TimesPlayed.txt',count_times_played)

    get_score = str(input("Would you like to check highscores?(Yes/No) "))

    while 'y' in get_score.lower():
        check_name = str(input('Enter a name here: '))
        d = fileFunctions.readDictFile('TimesPlayed.txt')
        if check_name.lower() in d:
            print("{} has won this game {} times!".format(
                fileFunctions.getScore('TimesPlayed.Txt',check_name)[0].capitalize(),fileFunctions.getScore('TimesPlayed.txt',check_name)[1])
                )
            get_score = str(input("Would you like to check more highscores?(Yes/No) "))
        else:
            print("Name does not exist.")
            get_score = str(input("Would you like to check more highscores?(Yes/No) "))

