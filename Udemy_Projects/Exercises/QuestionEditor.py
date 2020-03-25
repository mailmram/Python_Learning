def sentence_marker(mySentence):
    interogatives = ("how", "what", "why")
    capitalizedSen = mySentence.capitalize()
    if mySentence.startswith(interogatives):
        return "{}?".format(capitalizedSen)
    else:
        return "{}.".format(capitalizedSen)


results = []
while True:
    userInput = input("Say Something: ")
    if userInput == "/end":
        break
    else:
        results.append(sentence_marker(userInput))
    
print(" ".join(results))