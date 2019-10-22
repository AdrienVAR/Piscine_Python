from random import shuffle
import sys

def removeDuplicates(param):
    uniqueList = []
    for elem in param:
        if elem not in uniqueList:
            uniqueList.append(elem)
    return uniqueList

def generator(text, sep, option=None):
    '''Option is an optionnal arg, sep is mandatory'''
    if type(text) is not str:
        print("ERROR")
        exit()  
    if option != "ordered" and option != "shuffled" and option != "unique" and option != None:
        print("Option ERROR")
        exit()
    words = text.split(sep)
    if option is "ordered":
        words.sort(key=lambda x:(not x.islower(), x))
    elif option is "shuffled":
        shuffle(words)
    elif option is "unique":
        words = removeDuplicates(words)
    i = 0
    while i < len(words):
        yield words[i]
        i += 1

if __name__ == "__main__" :
    #text = 1
    text = "Le Lorem Ipsum est simplement est du faux texte faux est faux oui."
    for words in generator(text, sep=" ", option="unique"):
        print (words)
