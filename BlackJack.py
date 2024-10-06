import random

def deal_card(hand):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    hand.append(random.choice(cards))
    return hand
def calc_score(hand):
    score = sum(hand)
    if 11 in hand and sum(hand) > 21:
        score = sum(hand) - 10
    return score
def play_game():
    print("""


  ____  _            _    _            _    
 |  _ \| |          | |  (_)          | |   
 | |_) | | __ _  ___| | ___  __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                        _/ |                
                       |__/                 


""")
    player_hand = []
    comp_hand = []

    game_over = False
    deal_card(deal_card(player_hand))
    deal_card(comp_hand)
    while not game_over:
        print(f"Your cards: {player_hand}, current score: {calc_score(player_hand)}\nComputer's first card:{comp_hand[0]}")
        if calc_score(player_hand) == 21:
            game_over = True
            break
        elif calc_score(player_hand) > 21:
            game_over = True
            break
        want_card = str(input("Type 'y' to get another card, Type 'n' to pass: ")).lower()
        if want_card == 'y':
            deal_card(player_hand)
        else:
            game_over = True
    while calc_score(comp_hand) < 17:
        deal_card(comp_hand)
    if calc_score(player_hand) > 21:
        print(f"Your final hand: {player_hand}, final score: {calc_score(player_hand)}\nComputer's final hand: {comp_hand}, final score: {calc_score(comp_hand)}")
        print('You lose')
    elif calc_score(comp_hand) == 21:
        print(f"Your final hand: {player_hand}, final score: {calc_score(player_hand)}\nComputer's final hand: {comp_hand}, final score: {calc_score(comp_hand)}")
        print('You lose')
    elif calc_score(comp_hand) > 21:
        print(f"Your final hand: {player_hand}, final score: {calc_score(player_hand)}\nComputer's final hand: {comp_hand}, final score: {calc_score(comp_hand)}")
        print('you win')
    elif calc_score(player_hand) < calc_score(comp_hand):
        print(f"Your final hand: {player_hand}, final score: {calc_score(player_hand)}\nComputer's final hand: {comp_hand}, final score: {calc_score(comp_hand)}")
        print('You lose')
    elif calc_score(player_hand) == calc_score(comp_hand):
        print(f"Your final hand: {player_hand}, final score: {calc_score(player_hand)}\nComputer's final hand: {comp_hand}, final score: {calc_score(comp_hand)}")
        print("It's a draw")
    else:
        print(f"Your final hand: {player_hand}, final score: {calc_score(player_hand)}\nComputer's final hand: {comp_hand}, final score: {calc_score(comp_hand)}")
        print('You win')

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n"*20)
    play_game()