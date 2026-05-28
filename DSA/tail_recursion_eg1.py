c1=0
def function():
    global c1
    if c1 == 4 :
         return 
    
    c1+=1    
    function() #first function call
    
    print("A") # last job 
    
    
   
    
function()
    
    