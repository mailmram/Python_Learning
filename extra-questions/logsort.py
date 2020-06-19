#import sys
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #print(logs.split())
        #logs.sort(key = lambda n: n.split()[1])
        list1 = []
        list2 = []
        #list3 =[]
        for log in logs:
            if not log.split()[1].isalpha():
                list1.append(log)
            else:
                list2.append(log)
        list2.sort(key = lambda n: n.split()[0])
        list2.sort(key = lambda n: n.split()[1:])
        return (list2 + list1)