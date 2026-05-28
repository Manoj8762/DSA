Problem_Statement=''' While playing an RPG game, you were assigned to complete one of the hardest quests in this game. There are n monsters you’ll need to defeat in this quest.
Each monster i is described with two integer numbers – poweri and bonusi. To defeat this monster, you’ll need at least poweri experience points. If you try fighting this monster without having enough experience points, you lose immediately. You will also gain bonusi experience points if you defeat this monster. You can defeat monsters in any order.
The quest turned out to be very hard – you try to defeat the monsters but keep losing repeatedly. Your friend told you that this quest is impossible to complete.
Input:
The first line contains an integer, n, denoting the number of monsters. The next line contains an integer, e, denoting your initial experience.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, poweri, which represents power of the corresponding monster.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, bonusi, which represents bonus for defeating the corresponding monster.

'''


n=int(input(" Enter the number of monsters againist we compete "))
level=int(input("enter the initial experience "))

power=[int(input()) for _ in range(n)]
bonus=[int(input()) for _  in range(n)]

a=sorted(zip(power,bonus))
ans=0

for power,bonus in a:
    if level<power:
        break
    
    level+=bonus
    ans+=1
print(ans)



n=int(input("enter the number of compitators"))
level=int(input('enetr the initial level '))

powe=[int(input() for _ in range(n))]
bonus=[int(input()) for _ in range(n)]
ans=0
sor=sorted(zip(powe,bonus))

for powe,bonus in sor:
    if powe>level:
        break
    level+=bonus
    ans+=1
print(ans)