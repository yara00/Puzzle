from queue import Queue
import State
import time


class Bfs:

    def __init__(self, initialState):
        self.state = initialState
        self.goalState = 12345678
        self.fringe = Queue()
        self.explored = set()

    def algorithm(self):
        # append init state to fringe queue
        self.fringe.put(self.state.num)

        while not self.fringe.empty():
            currentStateNum = self.fringe.get()
            currentState = State.State(currentStateNum)
            # append current state to explored set
            self.explored.add(currentStateNum)
            print("explored ", currentStateNum)
            # check goal state
            if currentState.isGoalState():
                return currentStateNum

            # expand current state node
            for neighbour in currentState.find_neighbours():
                if neighbour not in self.explored and not self.fringe.queue:  # et2ky mn queue condition
                    # append neighbour to fringe queue
                    self.fringe.put(neighbour)

        return False


if __name__ == '__main__':
    state = State.State(125346780)
    bfs = Bfs(state)
    startTime = time.time_ns()
    bfs.algorithm()
    endTime = time.time_ns()
    print(endTime - startTime)
    print("ana fe bfs now")
