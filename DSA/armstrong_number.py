def check_arm(num):
    n=num
    n1=n
    c1=0
    while num>0:
        num=num//10
        c1+=1
    s1=0
    while n>0:
        remainder=n%10
        s1=s1+(remainder**c1)
        n=n//10
    return True if n1==s1 else False
print(check_arm(153))
print(check_arm(1633))
print(check_arm(1634))

# for 153 1 power len(153)+ 5 power len(153) + 3 power len(153)==150 then that number is armstrong      
