# BlackJack Statistics Program
# BlackJack Rules: 2 decks. 70% Penetration. Dealer hits on soft 17s
# bugs: splits inside of splits, Player Aces

# For a 2-Deck shoe:
one_suit_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
shoe = one_suit_cards * 8
player_cash = 100


# Function for player splits
def split(player_cards, dealer_cards, player_cash, bet_amount):
    split1 = [player_cards[0]]
    split2 = [player_cards[1]]
    new_card = shoe.pop(0)
    split1.append(new_card)
    new_card = shoe.pop(0)
    split2.append(new_card)

    print("Hand 1:", split1)
    print("Hand 2:", split2)

    # HAND 1
    move = input("Options for hand 1:\n h = hit\n s = stay\n d = double\n")
    bustchecker = True  # This is solely for a player bust on a split hand

    if move == 'd':
        player_cash -= bet_amount
        bet_amount = bet_amount * 2

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
            print('You now have', '$' + str(player_cash))

        move = 's'

    while move == 'h':
        split1.append(shoe.pop(0))

        player_ace_count = split1.count('A')
        if split1.count('A') > 0:
            player_ace_count = split1.count('A')
            for i in range(player_ace_count):
                split1[split1.index('A')] = 11
            for i in range(split1.count(11)):
                if sum(split1) > 21 and i != split1.count(11):
                    split1.remove(11)
                    split1.append(1)

        player_total = sum(split1)
        print(split1, "Total:", player_total)
        if player_total > 21:
            bustchecker = False
            move = 's'

        if bustchecker is True:
            move = input("Options:\n h = hit\n s = stay\n")

    if move == 's':

        # If there are aces in players cards
        player_ace_count = split1.count('A')
        if split1.count('A') > 0:
            for i in range(player_ace_count):
                split1[split1.index('A')] = 11
            for i in range(split1.count(11)):
                if sum(split1) > 21 and i != len(split1.count(11)):
                    split1.remove(11)
                    split1.append(1)

        if sum(split1) > 21:
            print('Player Bust. You lose')

        # HAND 2
        move = input("Options for hand 2:\n h = hit\n s = stay\n")
        bustchecker2 = True

        while move == 'h':
            split2.append(shoe.pop(0))

            player_ace_count = split2.count('A')
            if split2.count('A') > 0:
                player_ace_count = split2.count('A')
                for i in range(player_ace_count):
                    split2[split2.index('A')] = 11
                for i in range(split2.count(11)):
                    if sum(split2) > 21 and i != split2.count(11):
                        split2.remove(11)
                        split2.append(1)

                if sum(split2) > 21:
                    print('Player Bust. You lose')

            player_total2 = sum(split2)
            print(split2, "Total:", player_total2)
            if player_total2 > 21:
                print('Player Bust. You Lose')
                print()
                bustchecker2 = False
                move = 's'

            if bustchecker2 is True:
                move = input("Options:\n h = hit\n s = stay\n")

        if move == 's':

            # If there are aces in players cards
            player_ace_count = split2.count('A')
            for i in range(player_ace_count):
                split2[split2.index('A')] = 11
            for i in range(split2.count(11)):
                if sum(split2) > 21 and i != len(split2.count(11)):
                    split2.remove(11)
                    split2.append(1)

            if sum(split2) > 21:
                print('Player Bust. You lose')
                print()

            player_total2 = sum(player_cards)
            print("The Dealer Hand is:", dealer_cards)
            dealer_strategy(dealer_cards, player_cash, bet_amount)
            print()

        player_total = sum(split1)
        player_total2 = sum(split2)
        dealer_total = sum(dealer_cards)

        if dealer_total > 21 and player_total <= 21 and player_total2 <= 21:
            print('Dealer Bust. Player wins all hands')
            player_cash = player_cash + (bet_amount * 4)
        if dealer_total > 21 and player_total <= 21 and player_total2 > 21:
            print('Dealer Bust. Player wins Hand 1.')
            player_cash = player_cash + (bet_amount * 2)
        if dealer_total > 21 and player_total > 21 and player_total2 <= 21:
            print('Dealer Bust. Player wins Hand 2.')
            player_cash = player_cash + (bet_amount * 2)

        if player_total > 21:
            print("Player Bust on Hand 1")
        if player_total2 > 21:
            print("Player Bust on Hand 2")

        if 21 >= dealer_total > player_total <= 21:
            print('Dealer Wins Hand 1')
        if 21 > dealer_total < player_total <= 21:
            print('Player Wins Hand 1')
            player_cash = player_cash + (bet_amount * 2)
        if 21 >= dealer_total == player_total:
            print("Push on Hand 1")
            player_cash = player_cash + bet_amount
        if 21 >= dealer_total > player_total2:
            print('Dealer Wins Hand 2')
        if 21 > dealer_total < player_total2 <= 21:
            print('Player Wins Hand 2')
            player_cash = player_cash + (bet_amount * 2)
        if 21 >= dealer_total == player_total2:
            print("Push on Hand 2")
            player_cash = player_cash + bet_amount

        print('You now have:', '$' + str(player_cash))


# Function for dealer strategy
def dealer_strategy(dealer_cards, player_cash, bet_amount):
    global dealer_total
    global dealer_bust_check
    dealer_bust_check = False

    if dealer_cards[0] == 'A' and dealer_cards[
        1] == 'A':  # The next four if statements are for when there is an ace in the dealers initial hand
        dealer_cards[0] = 11
        dealer_cards[1] = 1

    if dealer_cards[0] == 'A' and dealer_cards[1] != 'A':
        dealer_cards[0] = 11

    if dealer_cards[0] != 'A' and dealer_cards[1] == 'A':
        dealer_cards[1] = 11

    if dealer_cards[0] != 'A' and dealer_cards[1] != 'A':  # If the dealer has no aces, we begin drawing cards...
        dealer_total = sum(dealer_cards)

        soft_17_check = False
        if dealer_cards.count(11) > 0:
            dealer_cards.remove(11)
            if sum(dealer_cards) == 6:
                soft_17_check = True
            dealer_cards.append(11)

        while dealer_total < 17 or soft_17_check is True:  # If his hand is not greater than 1
            new_card = shoe.pop(0)
            check = True

            if new_card == 'A' and dealer_total in [11, 12, 13, 14, 15, 16]:
                check = False
                new_card = 1
                dealer_cards.append(new_card)
                dealer_total = sum(dealer_cards)
                print("Dealer Hand:", dealer_cards, "Total:", dealer_total)

            if new_card == 'A' and dealer_total in [7, 8, 9, 10]:
                check = False
                new_card = 11
                dealer_cards.append(new_card)
                dealer_total = sum(dealer_cards)
                print("Dealer Hand:", dealer_cards, "Total:", dealer_total)

            if new_card == 'A' and dealer_total in [4, 5, 6]:
                check = False
                new_card = 11
                dealer_cards.append(new_card)
                dealer_total = sum(dealer_cards)
                print("Dealer Hand:", dealer_cards, "Total:", dealer_total)

            if check is True:
                dealer_cards.append(new_card)

                dealer_ace_count = dealer_cards.count(11)
                if dealer_ace_count > 0:
                    for i in range(dealer_ace_count):
                        if sum(dealer_cards) > 21 and i != dealer_ace_count:
                            dealer_cards.remove(11)
                            dealer_cards.append(1)

                dealer_total = sum(dealer_cards)
                print("Dealer Hand:", dealer_cards, "Total:", dealer_total)

            soft_17_check = False
            if dealer_cards.count(11) > 0:
                dealer_cards.remove(11)
                if sum(dealer_cards) == 6:
                    soft_17_check = True
                dealer_cards.append(11)

    dealer_total = sum(dealer_cards)
    if dealer_total > 21:
        dealer_bust_check = True  # This will make sure player_cash is assigned with the right amount in the blackjack function
        print("Dealer Bust. Player wins")
        player_cash1 = player_cash + (bet_amount * 2)
        print('You now have:', '$' + str(player_cash1))

    return ''


# Function to play BlackJack:
def blackjack(player_cash):
    import random as r
    global shoe
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
        global bet_amount
        bet_amount = (input('Enter your bet:'))
        try:
            int(bet_amount)
        except:
            print("please enter a number")
            bet_amount = (input('Enter your bet:'))

        bet_amount = int(bet_amount)
        player_cash -= bet_amount
        print('Player\'s Hand:', player_cards)
        print('Dealer\'s Hand:', dealer_cards[0])
        print()

        # Dealer BlackJack
        blackjack_hand = [['A', 10], [10, 'A']]
        if dealer_cards in blackjack_hand:
            print("Dealer BlackJack. You lose")
            print('You now have:', '$' + str(player_cash))
            continue

        # Player BlackJack
        blackjack_hand = [['A', 10], [10, 'A']]
        if player_cards in blackjack_hand:
            print("BlackJack. Winner Winner Chicken Dinner")
            player_cash = player_cash + bet_amount + (1.5 * bet_amount)
            print('You now have:', '$' + str(player_cash))
            continue

        move = input("Options:\n h = hit\n s = stay\n x = split\n d = double down\n\n")
        try:
            list1 = ['h', 's', 'x', 'd']
            if move not in list1:
                2 / 0
        except:
            print("Not a valid option. Please enter h, x, s, or d")
            move = input("Options:\n h = hit\n s = stay\n x = split\n d = double down\n\n")

        # If player splits
        if move == 'x' and player_cards[0] != player_cards[1]:
            print('You must have a pair to split.')
            move = input('Enter a different option for your hand:\n')

        if move == 'x' and player_cards[0] == player_cards[1]:
            var = False
            player_cash -= bet_amount
            split(player_cards, dealer_cards, player_cash, bet_amount)

        # If player hits
        if var is True:
            if move == 'd':
                player_cash = player_cash - bet_amount
                bet_amount = bet_amount * 2

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
                    print('You now have', '$' + str(player_cash))
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

                    if sum(player_cards) > 21:
                        print('Player Bust. You lose')

                # To calculate player score
                player_total = sum(player_cards)
                print(player_cards, "Total:", player_total)
                if player_total > 21:
                    print('Player Bust. You Lose')
                    print()
                    print('You now have', '$' + str(player_cash))
                    break
                move = input("Options:\n h = hit\n s = stay\n")

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

                player_total = sum(player_cards)
                print("The Dealer Hand is:", dealer_cards)
                dealer_strategy(dealer_cards, player_cash, bet_amount)
                print()

                dealer_total = sum(dealer_cards)
                if dealer_bust_check is False:
                    if 21 >= dealer_total > player_total:
                        print('Dealer Wins')
                    if 21 > dealer_total < player_total <= 21:
                        print('Player Wins')
                        player_cash = player_cash + bet_amount + bet_amount
                    if 21 >= dealer_total == player_total:
                        print("Push")
                        player_cash += bet_amount

                    print('You now have:', '$' + str(player_cash))

    return ''


if __name__ == '__main__':
    print("BlackJack Rules: 2 Decks, Dealer hits soft 17's, BlackJack pays 3:2")
    send = input("Welcome. Would you like to play a game of BlackJack? (y/n)\n")
    print('You have $100')
    while send == 'y':
        blackjack(player_cash)
        send = input("No more cards. Would you like to reshuffle and play another game of BlackJack? (y/n)\n")









