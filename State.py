# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class State :
    state = [0,0,0,0,0,0,0,0,0]

    def set_state( self, newState ):
        self.state = newState

    def get_state(self):
        return self.state

    ## function generate an array with the possible moves ( up - down - left - right )
    ## the impossible move will be represented by 0
    ## the possible move will be represented by the differnce between the empty place and the movable number
    def find_possible_moves(self ):
        moves = [0,0,0,0]
        emptyPlace = self.state.index(0)        # find the empty place

        if(emptyPlace>=0 and emptyPlace <=5):       #Up Move
            moves[0] = 3

        if (emptyPlace >= 3 and emptyPlace <= 8):      #Down Move
            moves[1] = -3

        if (emptyPlace==0 or emptyPlace==1 or emptyPlace==3 or emptyPlace==4 or emptyPlace==6 or emptyPlace==7):    #Left Move
            moves[2] = 1

        if (emptyPlace==2 or emptyPlace==1 or emptyPlace==5 or emptyPlace==4 or emptyPlace==8 or emptyPlace==7):    #Right Move
            moves[3] = -1

        return moves

    ## function to generate a next state from the intial state according to the given index to be swapped with
    def generate_state(self ,index):
        newState = self.state.copy()

        emptyPlace = newState.index(0)
        newState[emptyPlace], newState[emptyPlace+index] = newState[emptyPlace+index], newState[emptyPlace]

        return newState


    ## Function finds all the states that can be found from the intial state
    def find_neighbours(self):
        moves = self.find_possible_moves()              # find possible moves
        neighbours = []
        for x in range(4):
            if(moves[x] != 0):
                neighbour = self.generate_state(moves[x])     # generate possible states
                neighbours.append(neighbour)
        return neighbours



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = State()
    s1.set_state([1,2,3,4,5,6,7,8,0])
    print(s1.find_neighbours())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
