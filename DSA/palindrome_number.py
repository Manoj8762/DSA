def check_palindrome(num):
    n=int(num)
    result=0
    while(num>0):
        remainder=num%10
        result=(result*10)+remainder
        num=num//10
    return True if result==n else False
print(check_palindrome(123456))
print(check_palindrome(12321))
