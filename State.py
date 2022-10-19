class State:
    num = 0
    goalState = 12345678

    def __init__(self, stateNum):
        self.num = stateNum

    def isGoalState(self):
        return self.num == self.goalState

    def getGoalState(self):
        return self.goalState

    def find_possible_moves(self):
        stringState = str(self.num)

        if (self.num < 100000000):
            stringState = '0' + stringState
        moves = [0, 0, 0, 0]
        emptyPlace = stringState.index('0')  # find the empty place
        if (emptyPlace >= 0 and emptyPlace <= 5):  # Up Move
            moves[1] = 3

        if (emptyPlace >= 3 and emptyPlace <= 8):  # Down Move
            moves[0] = -3

        if (
                emptyPlace == 0 or emptyPlace == 1 or emptyPlace == 3 or emptyPlace == 4 or emptyPlace == 6 or emptyPlace == 7):  # Left Move
            moves[3] = 1

        if (
                emptyPlace == 2 or emptyPlace == 1 or emptyPlace == 5 or emptyPlace == 4 or emptyPlace == 8 or emptyPlace == 7):  # Right Move
            moves[2] = -1

        return moves

    ## function to generate a next state from the intial state according to the given index to be swapped with
    def generate_state(self, index):
        newStateNum = self.num

        newState = str(newStateNum)
        if (newStateNum < 100000000):
            newState = '0' + newState

        emptyPlace = newState.index('0')

        # swap emptyplace with emptyplace+index
        newState = self.swapCharacters(newState, emptyPlace, emptyPlace + index)

        return newState

    def swapCharacters(self, string, ind, jnd):
        if (ind < jnd):
            i = ind
            j = jnd
        else:
            j = ind
            i = jnd

        return ''.join([string[:i], string[j], string[i + 1:j], string[i], string[j + 1:]])

    ## Function finds all the states that can be found from the intial state
    def find_neighbours(self):
        moves = self.find_possible_moves()  # find possible moves
        neighbours = []
        for x in range(4):
            if moves[x] != 0:
                neighbour = self.generate_state(moves[x])  # generate possible states
                neighbours.append(neighbour)
        return map(int, neighbours)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = State(102345678)
    for n in s1.find_neighbours():
        print(n)
