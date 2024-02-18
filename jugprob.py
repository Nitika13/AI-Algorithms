# Water jug problem
class waterJug:
    def __init__(self, jug_1, jug_2,target):
        self.jug1capacity = jug_1
        self.jug2capacity = jug_2
        self.target = target
        self.visitedStates = set()
    # fill jug1
    def validState(self,jug1,jug2):
       return 0<=jug1<=self.jug1capacity and 0<=jug2<=self.jug2capacity
    def bfs(self):
       que = [(0,0)]
       self.visitedStates.add((0,0))
       print("jug1={} and jug2={}".format(0,0))
       while que:
           currentState=que.pop(0)
           jug1,jug2=currentState
           if(jug1== self.target or jug2==self.target):
               break
           #fill both jugs
           if(self.validState(self.jug1capacity,jug2) and (self.jug1capacity,jug2) not in self.visitedStates):
               que.append((self.jug1capacity,jug2))
               self.visitedStates.add((self.jug1capacity,jug2))
               print("jug1={} and jug2={}".format(self.jug1capacity,jug2))
           if(self.validState(jug1,self.jug2capacity) and (jug1,self.jug2capacity) not in self.visitedStates):
               que.append((jug1,self.jug2capacity))
               self.visitedStates.add((jug1,self.jug2capacity))
               print("jug1={} and jug2={}".format(jug1,self.jug2capacity))
           #empty both jugs
           if(self.validState(0,jug2) and (0,jug2) not in self.visitedStates):
               que.append((0,jug2))
               self.visitedStates.add((0,jug2))
               print("jug1={} and jug2={}".format(0,jug2))
           if(self.validState(jug1,0) and (jug1,0) not in self.visitedStates):
               que.append((jug1,0))
               self.visitedStates.add((jug1,0))
               print("jug1={} and jug2={}".format(jug1,0))
           #pour from one jug to other
           pourAmount = min(jug1,self.jug2capacity-jug2)
           if(self.validState(jug1-pourAmount,jug2+pourAmount) and (jug1-pourAmount,jug2+pourAmount) not in self.visitedStates):
               que.append((jug1-pourAmount,jug2+pourAmount))
               self.visitedStates.add((jug1-pourAmount,jug2+pourAmount))
               print("jug1={} and jug2={}".format(jug1-pourAmount,jug2+pourAmount))
           pourAmount = min(jug2,self.jug1capacity-jug1)
           if(self.validState(jug1+pourAmount,jug2-pourAmount) and (jug1+pourAmount,jug2-pourAmount) not in self.visitedStates):
               que.append((jug1+pourAmount,jug2-pourAmount))
               self.visitedStates.add((jug1+pourAmount,jug2-pourAmount))
               print("jug1={} and jug2={}".format(jug1+pourAmount,jug2-pourAmount))
waterjug = waterJug(3,4,2)
waterjug.bfs()

               
           
        

         
