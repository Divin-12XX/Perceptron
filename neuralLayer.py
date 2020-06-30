import random 

class neural:

    #initializing weights and bias
    def __init__ (self,noInputNeurons):
        self.bias = 1               
        self.weights = []
        for i in range(noInputNeurons):           
            self.weights.append(random.random())
        
    
    #this is for output (0 or 1)
    def  activation(self,sum):     
        if sum > 0 :
            return 1
        else:
            return 0

    #summation of product of weights and activations
    def think(self,input):
        sum=0
        for i in range(len(self.weights)):
            try:
                sum += input[i] * self.weights[i]
            except IndexError:
                sum += self.bias * self.weights[i]    

        return self.activation(sum)
    

    def train(self,inputs,outputs):
        for i in range(len(inputs)):
            guess=self.think(inputs[i]) 
            error=outputs[i]-guess
            for j in range(len(self.weights)): 
                try:
                    self.weights[j] += error * inputs[i][j]
                except IndexError:
                    self.weights[j] += error * self.bias
        
inputs=[[0,0],[0,1],[1,0],[1,1]]
outputs=[0,1,1,1]


lg=neural(2)

for i in range(50):
    lg.train(inputs,outputs)


print("values are " +str(lg.think([0,0]))+str(lg.think([0,1]))+str(lg.think([1,1]))+str(lg.think([1,0])))
