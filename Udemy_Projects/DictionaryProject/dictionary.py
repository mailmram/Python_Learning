import json
import difflib

with open("data.json") as loadData:
    data = json.load(loadData)

def findWord(word):
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        suggestedWord = difflib.get_close_matches(word, data.keys(), cutoff=0.8)[0]
        userConfirmation = input("Did you mean %s instead? Enter Y or N" % suggestedWord)
        print(userConfirmation)
        if (userConfirmation.lower() == 'y') or (userConfirmation.lower() == 'yes'):
            print(findWord(suggestedWord.lower())) 
        else:
            return "Word not found."
    else:
        return "Word not found."

searchword = input("Enter word: ")
print(findWord(searchword.lower()))