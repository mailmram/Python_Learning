def topwords(reviews, keywords, k):
    keyList = {key.lower() : 0 for key in keywords}
    for review in reviews:
        words = review.split()
        for word in words:
            if word.lower() in keyList:
                keyList[word.lower()] = keyList[word.lower()] + 1
    print(keyList.get)
    print(sorted(keyList,key= keyList.get, reverse=True)[0:k])





k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
topwords(reviews, keywords, k)