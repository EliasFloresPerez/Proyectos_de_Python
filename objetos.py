class gato:
    color = ""
    legs = 0
    def __init__ (self,color,legs):
        self.color = color
        self.legs = legs
    def hablar(self):
        print("miau")
    

Felix = gato("Red",4)
Gati =  gato("Blue",5)


Felix.hablar()



