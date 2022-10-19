import math
class Heuristic:
    def getManhattenHeuristicCost(self, string):
        sum = 0
        for idx, c in enumerate(string):
            if c != '0':
                sum = sum + abs(idx - (ord(c) - ord('0')))
        return sum

    def getEuclideanHeuristicCost(self, string):
        sum = 0
        for idx, c in enumerate(string):
            if c != '0':
                # use x1 y1 for current place
                # use x2 y2 for place u want to go to which is the value of the char
                cNum = ord(c) - ord('0')
                x1 = idx % 3
                y1 = idx // 3

                x2 = cNum % 3
                y2 = cNum // 3

                currCost = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
                sum = sum + currCost
        return sum

    def getHeuristicCost(self,moveNum):
        string = str(moveNum)
        if(moveNum<1000000000):
            string = '0' + string
        return self.getManhattenHeuristicCost(string)
