from queue import Queue
import State
import time


class Bfs:
    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.fringe = Queue()
        self.explored = set()
        self.parentMap = {}
        self.maxDepth = 0

    def getPath(self, state):
        path = []
        while state != -1:
            path.append(state)
            state = self.parentMap[state]
        return path

    def algorithm(self):
        startTime = time.time()
        # append init state to fringe queue
        self.fringe.put(self.state.num)
        self.parentMap.update({self.state.num: -1})

        while not self.fringe.empty():
            currentStateNum = self.fringe.get()
            currentState = State.State(currentStateNum)
            path = self.getPath(currentStateNum)
            depth = len(path)
            self.maxDepth = max(depth, self.maxDepth)
            # append current state to explored set
            self.explored.add(currentStateNum)
            # check goal state
            if currentState.isGoalState():
                break

            # expand current state node
            for neighbour in currentState.find_neighbours():
                if neighbour not in self.explored: # and neighbour not in self.fringe.queue:
                    # append neighbour to fringe queue
                    self.fringe.put(neighbour)
                    self.parentMap.update({neighbour: currentStateNum})

        # unsolvable case
        """
        if self.goalState not in self.parentMap.keys():
            return False
        else:
            state = self.goalState
            path = []
            while state != -1:
                path.append(state)
                state = self.parentMap[state]
        """
        path.reverse()
        endTime = time.time()

        return path, len(path) - 1, self.maxDepth, len(self.explored) - 1, endTime - startTime


if __name__ == '__main__':
    s = State.State(125340678)
    bfs = Bfs(s)
    # startTime = time.time_ns()
    print(bfs.algorithm())
    #  endTime = time.time_ns()
    # print(endTime - startTime)
