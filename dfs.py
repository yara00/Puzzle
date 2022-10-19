import State
import time
from collections import deque




class dfs:

    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.frontier = deque() #stack
        self.explored = set()
        self.parentMap = {}
        self.TempNeighbours = []

    def algorithm(self):

        self.frontier.append(self.state.num)
        self.parentMap.update({self.state.num: -1})

        while self.frontier:
            currentNum = self.frontier.pop()
            currentState = State.State(currentNum)
            self.explored.add(currentNum)
            print("Current state number is >>", currentNum)

            if currentState.isGoalState():
                print("reacheddd heeeee")
                break

            for neighbour in currentState.find_neighbours():
                if neighbour not in self.frontier:
                    if neighbour not in self.explored:
                        #  print("My neighbour is >>> ", neighbour)
                        self.TempNeighbours.append(neighbour)

            while self.TempNeighbours:
                temp = self.TempNeighbours.pop()
                self.frontier.append(temp)
                self.parentMap.update({temp: currentNum})

            #  print(self.frontier)
            #  print(self.explored)
            #  print(self.parentMap.items())
        if self.goalState not in self.parentMap.keys():
            return False
        else:
            state = self.goalState
            path = []
            while state != -1:
                path.append(state)
                state = self.parentMap[state]

            path.reverse()
         #   print("Path is ", path)
            print("Cost is ", len(path) - 1)
            return path


if __name__ == '__main__':
    print("ana fe dfs now")

    s = State.State(125340678) #182043765
    search = dfs(s)
    startTime = time.time()
    search.algorithm()
    end = time.time()
    print(end - startTime)
