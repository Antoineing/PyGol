# A Faire :

# ajout time et itérations pour autre bouton
# ajout flexibilité dans les conditions de birth et de fin
# ajout gestion d'autres états


from tkinter import *

activeColor="#FF00FF"

#↓ class of one cell, contains the
class squareItem():
    def __init__(self,canvas,index,line,squareSize):
        self.canvas = canvas
        self.index=index
        self.line=line
        self.color = "blue"
        self.status= "dead"
        self.intermediateStatus="dead"
        self.squareSize = squareSize
        self.drawSquare(self.index)
        
    # dessine le carré et lui assigne la fonction changeStatus
    def drawSquare(self,index):
        """draw a square to its assigned position"""
        self.index =index
        self.square = self.canvas.create_rectangle(100+(self.index * self.squareSize),
                                                   100+(self.line * self.squareSize),
                                                   100 + self.squareSize+(self.index * self.squareSize),
                                                   100 +self.squareSize+ (self.squareSize*self.line),
                                                   fill=self.color,
                                                   activefill=activeColor)
        self.canvas.tag_bind(self.square, '<B1-Motion>', self.changeAllStatus)
        self.canvas.tag_bind(self.square, '<Button-1>', self.changeAllStatus)
        
    def changeAllStatus(self,*arg):
        """Change the status and the intermediate status of one square"""
        self.changeStatus()
        self.intermediateStatus=self.status

    def changeStatus(self,*arg):
        """Change the status and the color of one square"""
        if self.status == "dead":

            print("index :",self.index, "line: ", self.line)
            self.status="alive"
            self.color = "white"
            self.canvas.itemconfig(self.square, fill=self.color)
        elif self.status =="alive":
            self.status="dead"
            self.color = "blue"
            self.canvas.itemconfig(self.square, fill=self.color)


# class generating the grid and contains the game of life function
class squareGrid():
    def __init__(self,numberSquare=10,squareSize=25,birth=3,underpop=2):

        self.app = Tk()
        self.app.geometry("800x800")
        
        self.numberSquare = numberSquare
        self.squareSize = squareSize
        
        self.birth=birth
        self.underpop=underpop
        
        self.canvas = Canvas(self.app, width=600, height=600)
        self.drawgrid(self.canvas)
        self.canvas.pack()
        
        self.button1 = Button(self.app, height=2, width=5,command=self.GameOfLife, text="X1")
        self.canvas.pack()
        self.button1.pack()
        
        #test
        print(self.squareArray[1][0].line)

    def drawgrid(self,*arg):
        """Generates a Grid of SquareItem of dimensions numberSquare x numberSquare"""
        self.squareArray =[[squareItem(self.canvas, i,j,self.squareSize) for i in range(self.numberSquare)] for j in range (self.numberSquare)]
    
    #fonction jeu de la vie
    def GameOfLife(self):
        """ Game of life rules and updates the grid"""
        
        for i in range (self.numberSquare):
            for j in range (self.numberSquare):
                if (self.sumNeighbors(i,j)== self.birth) and self.squareArray[i][j].status == "dead":
                    self.squareArray[i][j].intermediateStatus="alive"
                elif ((self.sumNeighbors(i,j)> self.birth) or (self.sumNeighbors(i,j)<self.underpop)) and (self.squareArray[i][j].status=="alive") :
                    self.squareArray[i][j].intermediateStatus="dead"
                else:
                    pass
      
          
        for i in range (self.numberSquare):
            for j in range (self.numberSquare):
                if self.squareArray[i][j].status=="alive" and self.squareArray[i][j].intermediateStatus=="dead":
                    self.squareArray[i][j].changeStatus()
                elif self.squareArray[i][j].status=="dead" and self.squareArray[i][j].intermediateStatus=="alive":
                    self.squareArray[i][j].changeStatus()
        print("One Iteration")
 
    def sumNeighbors(self,i,j):
        """Count the number of alive neighbors"""
        counter = 0
        for a in range(i-1,i+2) :
            for b in range(j-1,j+2):
                if a in range(1,self.numberSquare) and b in range(1,self.numberSquare):
                    if self.squareArray[a][b].status=="alive":
                        counter = counter + 1
                    else:
                        pass
        if self.squareArray[i][j].status=="alive":
            counter = counter -1
        return counter
        
        
        
#Main
a=squareGrid(100,squareSize=10,birth=3)

a.app.mainloop()