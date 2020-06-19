class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #products = sorted(products)
        products.sort()
        print(products)
        wordDict = {}
        #print(len(searchWord))
        for i in range(len(searchWord)):
            #print(searchWord[0:i+1])
            wordDict[searchWord[:i+1]] = []
        for product in products:
            key = ""
            for i in product:
                key += i
                if key in wordDict and len(wordDict[key]) <3:
                    wordDict[key].append(product)
        #print(wordDict)
        return wordDict.values()
        #for product in products
        