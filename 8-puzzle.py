initial_state = [[8,2,4],[3,0,1],[6,7,5]]
goal_state = [[1,2,3],[8,0,4],[7,6,5]]
def Cloning(li1): 
    li_copy =[] 
    li_copy = li1.copy() 
    return li_copy 
class puzzle:
    def __init__(self, initialState, goalState):
        self.initialstate = Cloning(initialState)
        self.goalState = Cloning(goalState)
        self.visitedStates = list()
    def find_value_index(self,value, lst):
     for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == value:
                return i, j  
     return -1, -1 
    def bfs(self):
        que= [self.initialstate]
        self.visitedStates.append(self.initialstate)
        print(f"{ self.initialstate[0]}\n{ self.initialstate[1]}\n{ self.initialstate[2]}")
        while(que):
          currentState = que.pop(0)
          i, j = self.find_value_index(0, currentState)
          print(f"{i} {j}")
          if(currentState == self.goalState):
              break
        #moveup
          if(i!=0 and currentState not in self.visitedStates):
             print("move up \n")
             moveupstate=Cloning(currentState)
             moveupstate[i][j],moveupstate[i-1][j]= moveupstate[i-1][j],moveupstate[i][j]
             que.append(moveupstate)
             self.visitedStates.append([moveupstate]) 
             print(f"{moveupstate[0]}\n{moveupstate[1]}\n{moveupstate[2]}")
        #movedown
          if(i!=2 and currentState not in self.visitedStates):
             print("move down \n")
             movedownstate=Cloning(currentState)
             movedownstate[i][j],movedownstate[i+1][j]=movedownstate[i+1][j],movedownstate[i][j]
             que.append([movedownstate])
             self.visitedStates.append(movedownstate) 
             print(f"{movedownstate[0]}\n{movedownstate[1]}\n{movedownstate[2]}")
        #moveleft
          if(j!=0 and currentState not in self.visitedStates):
             print("move left \n")
             moveleftstate=Cloning(currentState)
             moveleftstate[i][j],moveleftstate[i][j-1]= moveleftstate[i][j-1],moveleftstate[i][j]
             que.append(moveleftstate)
             self.visitedStates.append([moveleftstate]) 
             print(f"{moveleftstate[0]}\n{moveleftstate[1]}\n{moveleftstate[2]}")
        #moveright
          if(j!=2 and currentState not in self.visitedStates):
             print("move right \n")
             moverightstate=Cloning(currentState)
             moverightstate[i][j],moverightstate[i][j+1]= moverightstate[i][j+1],moverightstate[i][j]
             que.append(moverightstate)
             self.visitedStates.append([moverightstate]) 
             print(f"{moverightstate[0]}\n{moverightstate[1]}\n{moverightstate[2]}")
eightPuzzle = puzzle(initial_state,goal_state)
eightPuzzle.bfs()



             
          
          
         
         