import time

import State
import Heuristic
from heapq import heapify, heappush, heappop


class AStarSearch:
    explored = set()
    parentmap = {}
    frontierHeap = []
    frontierDict = {}
    goalState = 0
    maxDepth = 0

    def __init__(self):
        heapify(self.frontierHeap)
        s= State.State(0)
        self.goalState=s.getGoalState()

    def findPath(self, startingStateNum,hNum):
        h = Heuristic.Heuristic()
        # insert to frontier 2 data Structures
        heappush(self.frontierHeap, (0, startingStateNum))
        self.frontierDict[startingStateNum] = 0

        # Set parent of first state to itself
        self.parentmap[startingStateNum] = (-1, 0)

        while (len(self.frontierHeap) != 0):

            # frontier.pull
            costToCurrent, currentStateNum = heappop(self.frontierHeap)
            if currentStateNum in self.explored:
                continue
            self.frontierDict.pop(currentStateNum)
            # Create new state object to access state functions
            currentState = State.State(currentStateNum)
            # Add to explored
            self.explored.add(currentStateNum)

            # actual cost is depth of the tree to the father
            dummy, actualCost = self.parentmap[currentStateNum]

            if actualCost > self.maxDepth:
                self.maxDepth=actualCost

            # check goal, change letter to fit the state
            if (currentState.isGoalState()):
                # print("found")

                break

            # function to get neighbors
            for move in currentState.find_neighbours():
                if move not in self.explored and move not in self.frontierDict.keys():
                    # calc new cost
                    costToNext = actualCost + 1 + h.getHeuristicCost(move,hNum)

                    # insert move to frontier and parent map
                    # insert to fronteir
                    heappush(self.frontierHeap, (costToNext, move))
                    self.frontierDict[move] = costToNext
                    # insert to parent map
                    self.parentmap[move] = (currentStateNum, actualCost+1)

                elif move not in self.explored:
                    costToNext = actualCost + 1 + h.getHeuristicCost(move, hNum)
                    if costToNext < self.frontierDict[move]:
                        heappush(self.frontierHeap, (costToNext, move))
                        self.frontierDict[move] = costToNext
                        self.parentmap[move] = (currentStateNum,actualCost+1)

        if self.goalState not in self.parentmap.keys():
            # print("didn't find goal state")
            return []
        else:
            state = self.goalState
            path = []
            while state != -1:
                path.append(state)
                state,x = self.parentmap[state]

            path.reverse()
            return path

    def findPathAndDetails(self,startingStateNum,hNum):
        startTime = time.time()
        path = self.findPath(startingStateNum,hNum)


        endTime = time.time()
        print(startTime)
        print(endTime)
        return {
            "path": path,
            "explored": self.explored,
            "cost": len(path) - 1,
            "maxDepth":self.maxDepth,
            "expanded": len(self.explored) - 1,
            "time": endTime - startTime
        }

    def AlgorithmManhattanH(self,startingStateNum):
        return self.findPathAndDetails(startingStateNum,0)


    def AlgorithmEuclideanH(self,startingStateNum):
        return self.findPathAndDetails(startingStateNum,1)

if __name__ == '__main__':
    Ast = AStarSearch()
    ans = Ast.findPathAndDetails(812043765,0)