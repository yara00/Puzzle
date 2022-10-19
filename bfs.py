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

    def algorithm(self):
        # append init state to fringe queue
        self.fringe.put(self.state.num)
        self.parentMap.update({self.state.num: -1})

        while not self.fringe.empty():
            currentStateNum = self.fringe.get()
            currentState = State.State(currentStateNum)
            # append current state to explored set
            self.explored.add(currentStateNum)

            # check goal state
            if currentState.isGoalState():
                print("Expanded Len: ", len(self.explored) - 1)
                print("Fringe Len: ", self.fringe.qsize())
                break

            # expand current state node
            for neighbour in currentState.find_neighbours():
                if neighbour not in self.explored and neighbour not in self.fringe.queue:
                    # append neighbour to fringe queue
                    self.fringe.put(neighbour)
                    self.parentMap.update({neighbour: currentStateNum})

        # unsolvable case
        if self.goalState not in self.parentMap.keys():
            return False
        else:
            state = self.goalState
            path = []
            while state != -1:
                path.append(state)
                state = self.parentMap[state]

            path.reverse()
            print("Path is ", path)
            print("Cost is ", len(path) - 1)
            return path


if __name__ == '__main__':
    s = State.State(125340678)
    bfs = Bfs(s)
    startTime = time.time_ns()
    bfs.algorithm()
    endTime = time.time_ns()
    print(endTime - startTime)
