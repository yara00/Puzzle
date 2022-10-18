import State
import Heuristic
from heapq import heapify, heappush, heappop


class AStarSearch:
    explored = set()
    parentmap = {}
    frontierHeap = []
    frontierDict = {}
    goalState = 12345678

    def __init__(self):
        heapify(self.frontierHeap)

    def find(self, startingStateNum):
        h = Heuristic.Heuristic()

        # insert to frontier 2 data Structures
        heappush(self.frontierHeap, (0, startingStateNum))
        self.frontierDict[startingStateNum] = 0

        # Set parent of first state to itself
        self.parentmap[startingStateNum] = (-1, 0)

        while (len(self.frontierHeap) != 0):
            # frontier.pull
            costToCurrent, currentStateNum = heappop(self.frontierHeap)
            self.frontierDict.pop(currentStateNum)

            currentState = State.State(currentStateNum)
            self.explored.add(currentStateNum)
            # check goal, change letter to fit the state
            if (currentState.isGoalState()):
                print("found")
                break

            # function to get neighbors
            for move in currentState.find_neighbours():
                if move not in self.explored and move not in self.frontierDict:
                    costToNext = costToCurrent + 1 + h.getHeuristicCost(moveNum=move)

                    # insert move to frontier and parent map
                    # calc new cost

                    # insert to fronteir
                    heappush(self.frontierHeap, (costToNext, move))
                    self.frontierDict[move] = costToNext
                    # insert to parent map
                    self.parentmap[move] = (currentStateNum, costToNext)

                elif move not in self.explored:
                    costToNext = costToCurrent + 1 + h.getHeuristicCost(moveNum=move)
                    if costToNext < self.frontierDict[move]:
                        heappush(self.frontierHeap, (costToNext, move))
                        self.frontierDict[move] = costToNext
                        self.parentmap[move] = currentState
        print(len(self.frontierHeap))

        print("exited while loop")
        if self.goalState not in self.parentmap:
            print("did not find the goal")


        else:
            state = self.goalState
            path = []
            while state != -1:
                print(state)
                path.append(state)
                state,x = self.parentmap[state]

            # print("PARENT MAP")
            # for p in self.parentmap:
            #     print(str(p) + " " + str(self.parentmap[p]))
            #
            # print("FRONTIER DICT")
            # for p in self.frontierDict:
            #     print(str(p) + " " + str(self.frontierDict[p]))
            #
            # print("EXPLORED")
            # for s in self.explored:
            #     print(s)


if __name__ == '__main__':
    start = State.State(102345678)
    Ast = AStarSearch()
    Ast.find(startingStateNum=102345678)
