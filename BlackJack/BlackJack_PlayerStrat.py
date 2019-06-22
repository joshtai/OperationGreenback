def basic_player_strategy(player_cards, dealer_card):  # when calling: dealer_card = dealer_cards[0]

    check1 = False

    if player_cards[0] == player_cards[1]:  # Splits
        if dealer_card in ['A', 10]:
            if player_cards[0] in ['A', 8]:
                move = 'x'

            if player_cards[0] in [2, 3, 4, 5, 6, 7, 9, 10]:
                check1 = True

        if dealer_card in [9, 8]:
            if player_cards[0] in ['A', 8, 9]:
                move = 'x'

            if player_cards[0] in [2, 3, 4, 5, 6, 7, 10]:
                check1 = True

        if dealer_card == 7:
            if player_cards[0] in ['A', 8, 7, 3, 2]:
                move = 'x'

            if player_cards[0] in [4, 5, 6, 10]:
                check1 = True

        if dealer_card in [5, 6]:
            if player_cards[0] in ['A', 2, 3, 4, 6, 7, 8, 9]:
                move = 'x'

            if player_cards[0] in [5, 10]:
                check1 = True

        if dealer_card == [2, 3, 4]:
            if player_cards[0] in ['A', 2, 3, 6, 7, 8, 9]:
                move = 'x'

            if player_cards[0] in [4, 5, 10]:
                check1 = True

    if (player_cards.count('A') == 0 and player_cards[0] != player_cards[1]) or check1 is True:  # Hard Totals, no aces or splits
        player_total = sum(player_cards)

        if dealer_card == 'A' or dealer_card == 10:
            if player_total >= 17:
                move = 's'
            if player_total in [16, 15, 14, 13, 12, 10, 9, 8, 7, 6, 5, 4]:
                move = 'h'
            if player_total == 11:
                move = 'd'

        if dealer_card in [7, 8, 9]:
            if player_total >= 17:
                move = 's'
            if player_total in [16, 15, 14, 13, 12, 9, 8, 7, 6, 5, 4]:
                move = 'h'
            if player_total in [10, 11]:
                move = 'd'

        if dealer_card in [4, 5, 6]:
            if player_total >= 12:
                move = 's'
            if player_total in [8, 7, 6, 5, 4]:
                move = 'h'
            if player_total in [9, 10, 11]:
                move = 'd'

        if dealer_card == 3:
            if player_total >= 13:
                move = 's'
            if player_total in [12, 8, 7, 6, 5, 4]:
                move = 'h'
            if player_total in [9, 10, 11]:
                move = 'd'

        if dealer_card == 2:
            if player_total >= 13:
                move = 's'
            if player_total in [12, 9, 8, 7, 6, 5, 4]:
                move = 'h'
            if player_total in [10, 11]:
                move = 'd'

    if player_cards.count('A') == 1 and player_cards[0] != player_cards[1]:  # Soft Total. no splits
        player_cards.remove('A')
        player_total = sum(player_cards)
        player_cards.append('A')

        if dealer_card in [9, 10, 'A']:
            if player_total in [8, 9]:
                move = 's'
            if player_total in [7, 6, 5, 4, 3, 2]:
                move = 'h'

        if dealer_card in [7, 8]:
            if player_total in [8, 9]:
                move = 's'
            if player_total in [7, 6, 5, 4, 3, 2]:
                move = 'h'

        if dealer_card == 6:
            if player_total in [9]:
                move = 's'
            if player_total in [8, 7]:
                if len(player_cards) == 2:
                    move = 'd'
                else:
                    move = 's'
            if player_total in [2, 3, 4, 5, 6]:
                move = 'd'

        if dealer_card == 5:
            if player_total in [9, 8]:
                move = 's'
            if player_total in [7]:
                if len(player_cards) == 2:
                    move = 'd'
                else:
                    move = 's'
            if player_total in [2, 3, 4, 5, 6]:
                move = 'd'

        if dealer_card == 4:
            if player_total in [9, 8]:
                move = 's'
            if player_total in [7]:
                if len(player_cards) == 2:
                    move = 'd'
                else:
                    move = 's'
            if player_total in [4, 5, 6]:
                move = 'd'
            if player_total in [2, 3]:
                move = 'h'

        if dealer_card == 3:
            if player_total in [9, 8]:
                move = 's'
            if player_total in [7]:
                if len(player_cards) == 2:
                    move = 'd'
                else:
                    move = 's'
            if player_total in [6]:
                move = 'd'
            if player_total in [2, 3, 4, 5]:
                move = 'h'

        if dealer_card == 2:
            if player_total in [9, 8]:
                move = 's'
            if player_total in [7]:
                if len(player_cards) == 2:
                    move = 'd'
                else:
                    move = 's'

            if player_total in [2, 3, 4, 5, 6]:
                move = 'h'

    return move

#########################################
'''def blackjack():
    dealer_blackjack_tally = []
    player_blackjack_tally = []
    player_wins_tally = []
    dealer_wins_tally = []
    player_busts_tally = []
    dealer_busts_tally = []
    push_tally = []

    import random as r
    global shoe
    one_suit_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    shoe = one_suit_cards * 8
    r.shuffle(shoe)
    del shoe[0]  # Dealer always burns first card

    while len(shoe) > 34:
        var = True
        player_cards = [shoe.pop(0)]
        dealer_cards = [shoe.pop(0)]
        player_cards.append(shoe.pop(0))
        dealer_cards.append(shoe.pop(0))

        print('-------------------------New hand------------------------------\n')
        print('Player\'s Hand:', player_cards)
        print('Dealer\'s Hand:', dealer_cards[0])
        print()

        # Dealer BlackJack
        blackjack_hand = [['A', 10], [10, 'A']]
        if dealer_cards in blackjack_hand:
            print("Dealer BlackJack. You lose")
            dealer_blackjack_tally.append(1)
            continue

        # Player BlackJack
        blackjack_hand = [['A', 10], [10, 'A']]
        if player_cards in blackjack_hand:
            print("BlackJack. Winner Winner Chicken Dinner")
            player_blackjack_tally.append(1)
            continue

        move = basic_player_strategy(player_cards, dealer_cards[0])

        # If player splits
        'if move == 'x' and player_cards[0] != player_cards[1]:
            print('You must have a pair to split.')
            move = input('Enter a different option for your hand:\n')

        if move == 'x' and player_cards[0] == player_cards[1]:
            var = False
            split(player_cards, dealer_cards) ''

        # If player hits
        if var is True:

            if move == 'd':

                player_cards.append(shoe.pop(0))

                player_ace_count = player_cards.count('A')  # For when player hits and recieves an Ace
                if player_cards.count('A') > 0:
                    player_ace_count = player_cards.count('A')
                    for i in range(player_ace_count):
                        player_cards[player_cards.index('A')] = 11
                    for i in range(player_cards.count(11)):
                        if sum(player_cards) > 21 and i != player_cards.count(11):
                            player_cards.remove(11)
                            player_cards.append(1)

                    if sum(player_cards) > 21:
                        print('Player Bust. You lose')

                player_total = sum(player_cards)
                print(player_cards, "Total:", player_total)
                if player_total > 21:
                    print('Player Bust. You Lose')
                    print()
                    player_busts_tally.append(1)
                    break

                move = 's'

            while move == 'h':
                player_cards.append(shoe.pop(0))

                # For when player hits and recieves an Ace
                player_ace_count = player_cards.count('A')
                if player_cards.count('A') > 0:
                    player_ace_count = player_cards.count('A')
                    for i in range(player_ace_count):
                        player_cards[player_cards.index('A')] = 11
                    for i in range(player_cards.count(11)):
                        if sum(player_cards) > 21 and i != player_cards.count(11):
                            player_cards.remove(11)
                            player_cards.append(1)

                # To calculate player score
                player_total = sum(player_cards)
                print(player_cards, "Total:", player_total)
                if player_total > 21:
                    print('Player Bust. You Lose')
                    print()
                    player_busts_tally.append(1)
                    break
                move = basic_player_strategy(player_cards, dealer_cards[0])

        # If player stands
        if var is True:
            if move == 's':

                # If there are aces in players cards
                player_ace_count = player_cards.count('A')
                for i in range(player_ace_count):
                    player_cards[player_cards.index('A')] = 11
                for i in range(player_cards.count(11)):
                    if sum(player_cards) > 21 and i != len(player_cards.count(11)):
                        player_cards.remove(11)
                        player_cards.append(1)

                if sum(player_cards) > 21:
                    print('Player Bust. You lose')
                    player_busts_tally.append(1)

                player_total = sum(player_cards)
                print("The Dealer Hand is:", dealer_cards)
                dealer_strategy(dealer_cards)
                print()

                dealer_total = sum(dealer_cards)
                if 21 >= dealer_total > player_total:
                    print('Dealer Wins')
                    dealer_wins_tally.append(1)
                if 21 > dealer_total < player_total <= 21:
                    print('Player Wins')
                    player_wins_tally.append(1)
                if 21 >= dealer_total == player_total:
                    print("Push")
                    push_tally.append(1)

    dealer_blackjack_final = 'The number of dealer blackjacks are:' + str(sum(dealer_blackjack_tally))

    return (dealer_blackjack_final, player_blackjack_tally, player_wins_tally, dealer_wins_tally, player_busts_tally,
            dealer_busts_tally, push_tally)


if __name__ == "__main__":
    blackjack()
'''




