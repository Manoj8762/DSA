def rev(s):
    result=[]
    for word in s.split():
        words=list(word)
        left,right=0,len(words)-1
        while left<right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1
        result.append(''.join(words))
        
    return ' '.join(result)
        

print(rev('I love python'))

