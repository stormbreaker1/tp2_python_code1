# This is the class and we have defined __init__ which is constructor in 
 # python. We need to pass the "self" keyword in it and other methods.

class Testing:
    
    def __init__(self):
        print("Hello, Welcome to Anedya")
        
    def saying(self):
        print("I am gonna tell you something.")
        
    def CallingName(self, x):
        self.name = x
        print("Your Name is ",self.name)    
       
obj1 = Testing()     
obj1.saying()  
obj1.CallingName("Meliodas")                                   

      