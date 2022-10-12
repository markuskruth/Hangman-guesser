import random, time

#load in the words from the original text file
def load_words():
    with open('english_words_v7.txt') as word_file:
        #No need to wrap this into a list since it already returns a list
        valid_words = word_file.read().splitlines()

    return valid_words

english_words = load_words()

print("Choose a word that is 4-8 characters long \n")

word_length = int(input("How long is your word? "))

#word_length = 6

#remove words all words that are not *word_length* letters long using list comprehension
english_words = [word for word in english_words if len(word) == word_length]

time.sleep(0.5)
print("Aight, let's go! \n")
time.sleep(0.5)

monta = 0
new_letters = []
totalGuesses = 10
väärin = 0
guess_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                 "p","r","s","t","u","v","w","y",]

def bestLetter(words,guess_letters):
    letters = []
    for word in words:
        for i in range(len(word)):
            if word[i] in guess_letters:
                letters.append(word[i])

    return letters

while True:
    try:
        if totalGuesses-väärin == 0 or len(english_words) == 1:
            break
        else:
            print("")
            if monta == word_length:
                break
            
            new_lista = []
            
            print(f"I have used {väärin}/{totalGuesses} of my guesses")

            guess = random.choice(bestLetter(english_words,guess_letters))
            guess_letters.remove(guess)

            osuiko = input("Does your word contain the letter \"" + guess + "\"? (y/n): ")
            if osuiko == "y":
                paikka = input("Enter all of the character positions (1-" +
                               str(word_length) + ") in which the letter \"" + guess +
                               "\" appears: ")

                paikka = paikka.split()
                for i in range(len(paikka)):
                    paikka[i] = int(paikka[i])
                    monta += 1
                
                for j in range(len(english_words)):
                    try:
                        if english_words[j][paikka[0]-1] == guess and english_words[j][paikka[1]-1] == guess:
                            new_lista.append(english_words[j])
                            
                    except:
                        if english_words[j][paikka[0]-1] == guess:
                            new_lista.append(english_words[j])

                english_words = new_lista
                new_letters = []
                
                for letter in guess_letters:
                    for i in range(len(english_words)):
                        try:
                            if letter in english_words[i]:
                                new_letters.append(letter)
                        except:
                            pass
                                    
                new_letters_v2 = []
                
                hyväksytty = 0
                for letter in guess_letters:
                    hyväksytty = 0
                    for i in range(len(new_letters)):
                        if letter == new_letters[i] and hyväksytty == 0:
                            new_letters_v2.append(letter)
                            hyväksytty = 1

                        
                guess_letters = new_letters_v2

            else:
                väärin += 1
    except:
        print("Sorry, but either you fucked up or your word is not in my dictionary")
        väärin = 100
        break
        
                        
                
print("")
if väärin == 0:
    print("I ran out of tries :(")

elif väärin == 100:
    pass

else:
    print("Your word is:", english_words)
