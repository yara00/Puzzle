import math
class Heuristic:
    def getManhattenHeuristicCost(self, string):
        sum = 0
        for idx, c in enumerate(string):
            if c != '0':
                cNum = ord(c) - ord('0')

                x1 = idx % 3
                y1 = idx // 3

                x2 = cNum % 3
                y2 = cNum // 3
                sum = sum + abs(x1 - x2 ) + abs(y1 - y2)
        return sum


    def getEuclideanHeuristicCost(self, string):
        sum = 0.0
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


    # returns hueristic cost when choice = 0 hueristic is manhattan and when it is 1 hueristic is euclidean
    def getHeuristicCost(self,moveNum,choice):
        string = str(moveNum)
        if len(string)==8:
            string = '0' + string
        if choice == 0:
            return self.getManhattenHeuristicCost(string)
        else:
            return self.getEuclideanHeuristicCost(string)

if __name__ == '__main__':
    h=Heuristic()
    print( h.getHeuristicCost(123456780,1) )


