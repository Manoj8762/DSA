
#head recursion

def func(x,n):
    
    if n==0:
        return
    print(n)
    n-=1
    func(x,n)
   
func(15,4)

print('------------')
print('------------')

#tail recursion

def func1(x,n):
    
    if n==0:
        return
  
    n-=1
    func1(x,n)
    print(n)
   
    
    
func1(15,4)