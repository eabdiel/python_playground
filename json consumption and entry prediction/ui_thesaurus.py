from tkinter import *
from random import choice
#----Modules
import json
from difflib import get_close_matches

#-----Data variables
data = json.load(open("data.json"))  #data.json has the word list in the format of a dictionary;
                                     #download from my git

error = ["Sorry, I don't know that word", "What did you say?", "The word doesn't exist", "Please double check."]

root = Tk()
word = StringVar()
definition = StringVar()

root.title(" Simple Thesaurus ")
Label(root, text="Word: ").pack(side=LEFT)
Entry(root, textvariable=word).pack(side=LEFT)
Label(root, text="Definition: ").pack(side=LEFT)
Entry(root, textvariable=definition).pack(side=LEFT)

def main():
    question = word.get()

    w = question.lower()
    if w in data:   #if word is a key in data
        definition.set(choice(data[w]))   #return value of key
    elif w.title() in data:   #elseif capitalize the first letter with the tittle command and check again
        definition.set(choice(data[w.title()]))
    elif w.upper() in data:  # else check in full caps in case user enters words like USA or NATO
        definition.set(choice(data[w.upper()]))
    elif len(get_close_matches(w, data.keys())) > 0: #IF nothing is found yet, len get_close_matches from current key
                                                     #if a close match was found, get_close.. will be more than 0
        definition.set("Did you mean %s instead?" % get_close_matches(w, data.keys())[0])
    else:
        definition.set(choice(error))

Button(root, text="Define", command=main).pack(side=LEFT)

mainloop()
