import State
import Heuristic
from heapq import heapify, heappush, heappop


class AStarSearch:
    explored = set()
    parentmap = {}
    frontierHeap = []
    frontierDict = {}
    goalState = 0

    def __init__(self):
        heapify(self.frontierHeap)
        s= State.State(0)
        self.goalState=s.getGoalState()

    def findPath(self, startingStateNum):
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


            # check goal, change letter to fit the state
            if (currentState.isGoalState()):
                # print("found")
                break

            # actual cost is depth of the tree to the father
            dummy, actualCost = self.parentmap[currentStateNum]

            # function to get neighbors
            for move in currentState.find_neighbours():
                if move not in self.explored and move not in self.frontierDict.keys():
                    # calc new cost
                    costToNext = actualCost + 1 + h.getHeuristicCost(moveNum=move)

                    # insert move to frontier and parent map
                    # insert to fronteir
                    heappush(self.frontierHeap, (costToNext, move))
                    self.frontierDict[move] = costToNext
                    # insert to parent map
                    self.parentmap[move] = (currentStateNum, actualCost+1)

                elif move not in self.explored:
                    costToNext = actualCost + 1 + h.getHeuristicCost(moveNum=move)
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

    def findPathAndDetails(self,startingStateNum):
        return {
            "path": self.findPath(startingStateNum),
            "explored": self.explored
        }


if __name__ == '__main__':
    Ast = AStarSearch()
    ans = Ast.findPathAndDetails(startingStateNum=12345678)
    # print("length of path")
    # print(len(ans["path"])-1)
    #
    # print("explored sets number")
    # print(len(ans["explored"]))
    # #
    # print(ans["path"])
    # print(ans["explored"])