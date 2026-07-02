def use_hash1(n,m):
    result=[0]*26
    for ch in n:
        #print(ch)
        result[ord(ch)-ord('a')]+=1
    #print(result)
    for ch in m:
        print(result[ord(ch) - ord('a')])
        
    
use_hash1('aacdnsvdjsbamshsvdhdjsajdhekwska',['a','b','c','d','e','f','g','s','m','n'])




def use_hash(n, m):
    result = [0] * 26

    # build frequency array
    for ch in n:
        result[ord(ch) - ord('a')] += 1
        

    # query characters
    for ch in m:
        print(f"{ch} : {result[ord(ch) - ord('a')]}")

use_hash(
    'aacdnsvdjsbamshsvdhdjsajdhekwska',
    ['a','b','c','d','e','f','g','s','m','n']
)