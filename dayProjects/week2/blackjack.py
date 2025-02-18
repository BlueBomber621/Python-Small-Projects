import random

default_cards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
 '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
 '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
 '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']

checkboard = {
    "Wins": 0,
    "Draws": 0,
    "Losses": 0,
}

cont_play = True

def draw_card():
    draw_index = random.randint(0, len(cards) - 1)
    drawn_card = cards[draw_index]
    cards.remove(cards[draw_index])

    return [drawn_card, cards]

def add_points(old_points, card):
    
    if card[0] == "J" or card[0] == "Q" or card[0] == "K" or (card[0] + card[1]) == "10":
        new_points = old_points + 10
    elif card[0] == "A":
        if old_points + 11 <= 21:
            new_points = old_points + 11
        else:
            new_points = old_points + 1
    else:
        new_points = old_points + int(card[0])

    return new_points

def dealer_draw(points):
    card_input = draw_card()
    new_card = card_input[0]
    cards = card_input[1]
    dealer_cards.append(new_card)
    points = add_points(points, new_card)

    return [points, cards]

def player_draw(points):
    card_input = draw_card()
    new_card = card_input[0]
    cards = card_input[1]
    player_cards.append(new_card)
    points = add_points(points, new_card)

    return [points, cards]

def list_cards(list):
    new_string = ""
    for item in list:
        new_string += item
        if list.index(item) != len(list) - 1:
            new_string += ", "
    
    return new_string

while cont_play:
    cards = []
    for item in default_cards:
        cards.append(item)

    dealer_cards = []
    dealer_points = 0
    player_cards = []
    player_points = 0


    dealer_input = dealer_draw(dealer_points)
    dealer_points = dealer_input[0]
    cards = dealer_input[1]
    dealer_input = dealer_draw(dealer_points)
    dealer_points = dealer_input[0]
    cards = dealer_input[1]
    print(f"Dealer's Cards: {dealer_cards[0]}, ???")
    player_input = player_draw(player_points)
    player_points = player_input[0]
    cards = player_input[1]
    player_input = player_draw(player_points)
    player_points = player_input[0]
    cards = player_input[1]
    print(f"Your Cards: {list_cards(player_cards)}\nYour Points: {player_points}")
    pchoice = input("Do you want to draw another card?\n(Y/N): ").lower()
    print("")
    if pchoice == "y":
        player_input = player_draw(player_points)
        player_points = player_input[0]
        cards = player_input[1]
    if dealer_points < 17:
        dealer_input = dealer_draw(dealer_points)
        dealer_points = dealer_input[0]
        cards = dealer_input[1]
    if player_points > 21:
        print(f"You got {player_points} points with the cards {list_cards(player_cards)}! Bust! You lose!")
        checkboard['Losses'] += 1
    else:
        print(f"Dealer's Cards: {list_cards(dealer_cards)}\nDealer's Points: {dealer_points}")
        print(f"Your Cards: {list_cards(player_cards)}\nYour Points: {player_points}")
        if dealer_points > 21:
            print(f"Dealer had {dealer_points}! Bust! You Win!")
            checkboard['Wins'] += 1
        elif player_points > dealer_points:
            print("You beat the dealer in points! You win!")
            checkboard['Wins'] += 1
        elif player_points == dealer_points:
            print("You had the same points as the dealer! It's a draw!")
            checkboard['Draws'] += 1
        else:
            print("You had less points than the dealer. You lose!")
            checkboard['Losses'] += 1
    
    print(f"\nWins: {checkboard['Wins']}\nLosses: {checkboard['Losses']}\nDraws: {checkboard['Draws']}\n")
    pchoice = input("Would you like to play again?\n(Y/N): ").lower()
    if pchoice == "n":
        cont_play = False
    else:
        print("")
