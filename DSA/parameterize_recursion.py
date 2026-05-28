def par_sum(sum,i,n):
    if i>n:
        print(sum)
        return 
    
    par_sum(sum+i,i+1,n)
par_sum(0,1,5)