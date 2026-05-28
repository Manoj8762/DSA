n=253
num=n
ne=n
ln=0
total=0
while num>0:
    ln+=1
    
    num=num//10
while ne>0:
    rem=ne%10
    ne=ne//10
    total+=rem**ln
print(True if n==total else False)
     
    

