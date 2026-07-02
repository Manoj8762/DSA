
# Head Recursion


def greet1(co):
    if co==4:
        return
    print("Tanu",co)
    co+=1
    greet1(co)
greet1(co=0)

print('-------------------------------')
print('-------------------------------')

#Tail recursion
print('-------------------------------')
print('-------------------------------')

def greet(co):
    if co==4:
        return
    co+=1
    greet(co)
    print("Tanu",co)
greet(co=0)