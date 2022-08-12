#EA SPORT
# welcome to fifa 23 =)  
# development by arian salemabadi
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
class player :
    def __init__(self,name,x,y,z,ballx,bally,energy):
        self.name=name
        self.x=x
        self.y=y
        self.z=z
        self.ballx=ballx
        self.bally=bally
        self.energy=energy
    #----------------------------
    # motion player----
    # move in the X direction
    
    def move_x_front(self):
        self.x+=2
        if self.energy > 0 :
            self.energy-=1
        else:
            pass
    def move_x_back(self):
        self.x-=2
        if self.energy > 0 :
            self.energy-=1
        else:
            pass
     #---------------------------
     # move in the Y direction 
    
    def move_y_right(self):
        self.y+=1
        if self.energy > 0 :
            self.energy-=1
        else:
            pass
    def move_y_left(self):
        self.y-=1
        if self.energy > 0 :
            self.energy-=1
        else:
            pass
     #----------------------------
     # sprint player----
     # sprint in the X direction
    def sprint_x_front(self):
        self.x+=4
        if self.energy > 0 :
            self.energy-=5
        else:
            pass
    def sprint_x_back(self):
        self.x+=3
        if self.energy > 0 :
           self.energy-=5
        else:
            pass
    #------------------------------
    # sprint in the Y direction
    def sprint_y_right(self):
        self.y+=2
        if self.energy > 0 :
            self.energy-=2
        else:
            pass
    def sprint_y_left(self):
        self.y+=2
        if self.energy > 0 :
            self.energy-=2
        else:
            pass
    #------------------------------
    # jump player
    def jump_for_head(self):
     if self.z < 3 :
        self.z+=3
     else:
        pass
    #------------------------------
    #--------------------------------------
    #shoot and pass and cross player----
    def shoot_on_leg(self):
                self.ballx+=5
                self.bally+=5
    def shoot_on_head(self):
        if z > 1 :
                self.ballx+=4
                self.bally+=4    
        else:
            pass
    def _pass(self):
                self.ballx+=3
                self.bally+=3 
    def cross(self):
                self.ballx+=8
                self.bally+=8
                
    # information of player mode
    def info(self):
        print(self.name , "at x: " , self.x , "and y:" , self.y , "and z:" , self.z,"and energy :",self.energy,"and position of ball x:",self.ballx,"and y:",self.bally)
        fig = plt.figure(figsize = (50, 7))
        ax = plt.axes(projection ="3d")
        ax.scatter3D(self.x,self.y, self.z, color = "blue")
        plt.title("3D position of player")
        ax.set_xlabel('X - position', fontweight ='medium')
        ax.set_ylabel('Y - position', fontweight ='medium')
        ax.set_zlabel('Z - position', fontweight ='medium')
        plt.show()
#---------------------------------
bayern = player("Robert Lewandowski",0,0,0,0.25,0.25,100)
bayern.move_x_front()
bayern.shoot_on_leg()
bayern.info()


bayern.shoot_on_leg()
bayern.info()



bayern.move_y_right()
bayern.info()
