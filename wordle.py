import time as t
import random as rand
import math as m
        
    

myFileName = "C:/work/FiveLetterWords.txt"
guess1 = "notes"

retr1 = ""

common_letters = ["a","r","i","l","c","u"]
num_common = 0
repeats = 0
wpg = []

txt_file = open(myFileName, "r") #open the file for reading
file_content = txt_file.read() #get all the data from the file

word_list = file_content.split("\n") #create a list of all the words
txt_file.close()

bestguess = [" "," "," "," "," "] #an array of 5 strings
bannedlist = []
wrongplace = []
word = True
alreadyGuessed = []
mywordChosen = word_list[rand.randint(0,len(word_list))]
print("i am trying to guess", mywordChosen)
#1st guess
print("input", guess1)

for p in range(10):
    #return
    retr1 = input("what did it return,use 012 format")
    
    #add new letters to banned and best list and wrong place list
    for i in range(0,5):
        if (retr1[i] == "0") and (not guess1[i] in wrongplace or bestguess):
            bannedlist.append(guess1[i])
            print("adding " + guess1[i] + " to bannedlist")
        elif retr1[i] == "2":
            bestguess[i] = guess1[i]
            wrongplace.append(guess1[i])
        elif retr1[i] == "1":
            wrongplace.append(guess1[i])
            for jokes in range(len(wrongplace)):
                a = guess1[i]
                b = i
                wpg.append((a,b))


    print(bannedlist)
    print(wrongplace)
    print(bestguess)
    #generate a guess
    for guessnumberlol in range(6):# a loop that runs 6 times to try and find the word with the most commons while trying to not repeat
        for doubles in range(2):
            guessGenerated = False
            for i in range(0,len(word_list)):#checking to see if the word is suitable
                word = True
                for x in range(len(bannedlist)): 
                    if bannedlist[x] in word_list[i]:
                        if (word_list[i]==mywordChosen):
                            print(bannedlist[x] + " is in word so not allowing word " + word_list[i])
                        word = False
                        break
                for x in range(len(wrongplace)):
                    if not wrongplace[x] in word_list[i]:
                        if (word_list[i]==mywordChosen):
                            print(wrongplace[x] + " is NOT in word so not allowing word " + word_list[i])
                        word = False
                        break
                    for y in range(len(wpg)):
                        if word_list[i].find(wpg[y][0]) == wpg[y][1]:
                            if (word_list[i]==mywordChosen):
                                print(" Not allowing word because of wpg condition " + word_list[i])
                            word = False
                            break
                    if word == False:
                        break
                
                for x in range(5):
                    if not bestguess[x]==" ":
                        if not bestguess[x] == word_list[i][x]:
                            word = False
                            break
                for x in range(len(alreadyGuessed)): 
                    if word_list[i] == alreadyGuessed[x]:
                        word = False
                        break
                
                

                    
                
                
                if word == True:#check if the word is good and if theres no better word justt pick the starting word
                    num_common = 0

                    repeats = 0
                    for z in range(len(common_letters)): #check how many commons are in the word and only allow the word with the most
                        if common_letters[z]  in word_list[i]:
                            num_common = num_common + 1
                                                    
                    if doubles == 0:#not allowing doubles unless the program as tried more than 3 times to get a good word
                        for letternum in range(5):
                            for checklet in range(5):
                                if word_list[i][letternum] == word_list[i][checklet]:#PROBLEM IS HERE,IM GOING TO SLEEP BUT IT ISNT ALLOWING DOUBLES AND ONLY DOUBLES
                                    repeats = repeats+1
                                                                
                    if repeats <= 5:
                        if num_common >= 5-guessnumberlol: 
                            print("please input",word_list[i])
                            print(wpg)
                            guess1 = word_list[i]
                            guessGenerated = True
                            alreadyGuessed.append(word_list[i])
                            print(alreadyGuessed)
                            print(wpg)
                            break
                        
                if guessGenerated == True:
                    break 

                            
                                        
                                
                        
                        
                    
            if guessGenerated == True:
                break
            
        if guessGenerated == True:
            break        
                    
                
                
            
    if not guessGenerated:
        
        print("Failed to find a suitable word!")
    



        
        

            





# word_list is a list. Each element of this list is a 5 letter word
