import State
import time

class dfs:

   def __init__(self , intialState ):
        self.state = intialState
        self.frontier = []
        self.explored = set()
        self.parents = {}
        self.TempNeighbours = []

   def Algoritm(self):

        self.frontier.append(self.state.num)
        self.parents.update({self.state.num : self.state.num})

        while self.frontier :
            currentNum = self.frontier.pop()
            currentState = State.State(currentNum)
            self.explored.add(currentNum)
            print("Current state number is >>",currentNum)

            if currentNum == 12345678 :
                print("reacheddd heeeee")
                return True

            for neighbour in currentState.find_neighbours():
                if neighbour not in self.frontier :
                    if neighbour not in self.explored :
                      #  print("My neibhour is >>> ", neighbour)
                        self.TempNeighbours.append(neighbour)

            while self.TempNeighbours:
                temp = self.TempNeighbours.pop()
                self.frontier.append(temp)
                self.parents.update({temp: currentNum})

          #  print(self.frontier)
            print(self.explored)
            print(self.parents.items())
        return False


if __name__ == '__main__':
    print("ana fe dfs now")


    s = State.State(312045678)
    search = dfs(s)
    startTime = time.time()
    print("returned >>>>>>>>>>>>>",search.Algoritm())
    end =  time.time()
    print(end-startTime)