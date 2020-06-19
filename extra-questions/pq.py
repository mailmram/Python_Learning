from heapq import heapify,heappop,heappush
def mincost(myList):
    print(myList)
    heapify(myList)
    print(myList)
    cost = 0
    while len(myList) > 1:
        a, b = heappop(myList), heappop(myList)
        print(a,b)
        cost += a+b
        if myList:
            heappush(myList, a+b)
    return cost

print(mincost([8, 4, 6, 12]))