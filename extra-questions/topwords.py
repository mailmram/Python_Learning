def topwords(reviews, keywords, k):
    keyList = {key.lower() : 0 for key in keywords}
    keyList.getkeys()
    print(keyList)
    for review in reviews:
        wordoccured = {}
        words = review.split()
        for word in words:
            if word in keyList and word not in wordoccured:
                #print(word)
                wordoccured[word] = True
                keyList[word] = keyList[word] + 1
    for items in keyList:
        print(keyList[items])
    print(keyList)
    print(sorted(keyList, key = keyList.get,reverse=True))
    #print(sorted(keyList,key= keyList.get, reverse=True)[0:k])





k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than eurocell",
  "betacellular is better than deltacellular",
]
topwords(reviews, keywords, k)