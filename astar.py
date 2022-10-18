import State
import math
from heapq import heapify, heappush, heappop



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
            string = string+'0'
        return self.getManhattenHeuristicCost(string)


class AStarSearch:
    explored = set()
    parentmap = {}
    frontierHeap = []
    frontierDict = {}
    goalState = 12345678
    def __init__(self):
        heapify(self.frontierHeap)

    def find(self,startingStateNum):
        h = Heuristic

        # insert to frontier 2 data Structures
        heappush(self.frontierHeap,(0,startingStateNum))
        self.frontierDict[startingStateNum]=0

        # Set parent of first state to itself
        self.parentmap[startingStateNum]=(startingStateNum,0)


        while (self.frontierHeap.__len__() != 0):
            # frontier.pull
            costToCurrent,currentState = heappop(self.frontierHeap)
            self.frontierDict.pop(currentState)

            # check goal, change letter to fit the state
            if(self.isGoalState(currentState)):
                break

            # function to get neighbors
            for move in self.getNeighborsOfState(currentState):
                if move not in self.explored and move not in self.frontierDict:
                    costToNext = costToCurrent + 1 + h.getHeuristicCost(moveNum=move)

                    # insert move to frontier and parent map
                    # calc new cost

                    # insert to fronteir
                    heappush(self.frontierHeap,(costToNext,move))
                    self.frontierDict[move]=costToNext
                    # insert to parent map
                    self.parentmap[move] = (currentState, costToNext)

                elif move not in self.explored:
                    costToNext = costToCurrent + 1 + h.getHeuristicCost(moveNum=move)
                    if costToNext<self.frontierDict[move]:
                        heappush(self.frontierHeap,(costToNext,move))
                        self.frontierDict[move]=costToNext
                        self.parentmap[move]=currentState

        if self.goalState not in self.parentmap:
            print("did not find the goal")
            return []

        else:
            totalCost=0
            pathToGoal = []
            currentState= self.goalState
            while True :
                nextState,cost=self.parentmap[currentState]
                if(currentState==nextState):
                    break
                else:
                    totalCost=totalCost+cost
                    pathToGoal.append(nextState)
                    currentState=nextState
            print("found goal")
            print(pathToGoal)





    # dummy goal state chech
    def isGoalState(self,stateNum):
        return stateNum == 12345678

    # dummy get possible moves function
    def getNeighborsOfState(self,stateNum):
        #convert state to string
        #get possible moves
        return []



if __name__ == '__main__':
    state = State.State()
    print("ana fe a* now")
