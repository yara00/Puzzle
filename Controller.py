import State
import bfs
import dfs
import astar


class Controller:

    def input_validation(self, inputState):
        if inputState < 12345678 or inputState > 876543210:
            return False
        if inputState < 100000000:
            s = set('0' + str(inputState))
        else:
            s = set(str(inputState))

        return s.issuperset("012345678")

    def solve(self, method, initialState):
        # verify input validity
        if not self.input_validation(initialState):
            return "Invalid Input"

        state = State.State(initialState)
        result = 0
        if method == "BFS":
            result = bfs.Bfs(state).algorithm()
        elif method == "DFS":
            result = dfs.dfs(state).algorithm()
        elif method == "A*":
            result = astar.AStarSearch().findPathAndDetails(initialState)

        return result


if __name__ == '__main__':
    ctrl = Controller()
    print(ctrl.solve("bfs", 876543889))
    print("ana t7t el control now")
