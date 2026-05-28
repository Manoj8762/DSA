def combination(ar):
    combination1={}
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            combination1.append(j)
string = "abc"

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])
            