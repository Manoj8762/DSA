import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def calculator(hand):
    if sum(hand)==21 and len(hand)==2:
        return 0

    while 11 in hand and 21 > sum(hand):
        hand[hand.index(11)]=1
    return sum(hand)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return 'draw'
    elif user_score==0:
        return 'you loss'
    elif computer_score==0:
        return 'you win'
    elif user_score>21:
        return 'you went over you loss'
    elif computer_score>21:
        return 'opponent went over you loss'
    elif computer_score<user_score:
        return 'you win'
    else:
        return 'you loss'

while True:
    play=input('do you want to play "y" or "n" ')
    if play !='y':
        print('good bye')
        break
    else:
        # print(#logo)

        user_cards=[]
        computer_cards=[]

        for _ in range(2):
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))


        game_over=False

        while not game_over:


            computer_score=calculator(computer_cards)
            user_score=calculator(user_cards)

            print(f'your cards: {user_cards} and current score: {user_score}')
            print(f'computer\'s first card: {computer_cards[0]}')


            if user_score==0 or computer_score==0 or user_score>21:
                game_over=True
            else:
                choice=input(" 'y' to get another card else 'n' ")

                if choice=='y':
                    user_cards.append(random.choice(cards))
                else:
                    game_over=True

        computer_score=calculator(computer_cards)

        while computer_score !=0 and computer_score<17:
            computer_cards.append(random.choice(cards))
            computer_score=calculator(computer_cards)
        
        user_score=calculator(user_cards)
        computer_score=calculator(computer_cards)

        print(f' final result')
        print(f' user cards: {user_cards} and current score {user_score}')
        print(f'computer cards {computer_cards} and final score{computer_score}')
        print(computer_cards(user_score,computer_score))

