c1=0
def function():
    global c1
    if c1 == 4 :
         return 
        
    
    print("A") # first job 
    c1+=1
    function() # last function call
   
    
function()
    
    