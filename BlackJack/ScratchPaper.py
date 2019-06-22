def second_split(player_cards, dealer_cards):
    split101 = [player_cards[0]]
    split201 = [player_cards[1]]
    new_card = shoe.pop(0)
    split101.append(new_card)
    new_card = shoe.pop(0)
    split201.append(new_card)


    print("Hand A:", split101)
    print("Hand B:", split201)

    # HAND 1
    print("For hand A:")
    move = basic_player_strategy(split101, dealer_cards[0])
    bust_checker = True  # This is solely for a player bust on a split hand

    if move == 'x':
        print("Splitting again")
        if move == 'x' and split1[0] == split1[1]:
            split(split1, dealer_cards)

    if move == 'd':

        split101.append(shoe.pop(0))

        player_ace_count = split101.count('A')  # For when player hits and receives an Ace
        if split101.count('A') > 0:
            player_ace_count = split101.count('A')
            for i in range(player_ace_count):
                split101[split101.index('A')] = 11
            for i in range(split101.count(11)):
                if sum(split101) > 21 and i != split1.count(11):
                    split101.remove(11)
                    split101.append(1)

            if sum(split101) > 21:
                print('Player Bust. You lose')

        player_total = sum(split101)
        print(split101, "Total:", player_total)
        if player_total > 21:
            print('Player Bust. You Lose')
            print()

        move = 's'

    while move == 'h':
        split101.append(shoe.pop(0))

        player_ace_count = split101.count('A')
        if split101.count('A') > 0:
            player_ace_count = split101.count('A')
            for i in range(player_ace_count):
                split101[split101.index('A')] = 11
            for i in range(split101.count(11)):
                if sum(split101) > 21 and i != split101.count(11):
                    split101.remove(11)
                    split101.append(1)

        player_total = sum(split1)
        print(split101, "Total:", player_total)
        if player_total > 21:
            bust_checker = False
            move = 's'

        if bust_checker is True:
            move = basic_player_strategy(split1, dealer_cards[0])

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

        # HAND 2 -------------------------------------------------------------------------
        print("For the second hand:")
        move = basic_player_strategy(split2, dealer_cards[0])
        bust_checker2 = True

        if move == 'x':
            print("Splitting again on your second hand")
            if move == 'x' and split2[0] == split2[1]:
                split(split2, dealer_cards)

        if move == 'd':

            split2.append(shoe.pop(0))

            player_ace_count = split2.count('A')  # For when player hits and receives an Ace
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

            player_total = sum(split2)
            print(split2, "Total:", player_total)
            if player_total > 21:
                print('Player Bust. You Lose')
                print()

            move = 's'

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
                bust_checker2 = False
                move = 's'

            if bust_checker2 is True:
                move = basic_player_strategy(split2, dealer_cards[0])

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

            print("The Dealer Hand is:", dealer_cards)
            dealer_strategy(dealer_cards, dealer_busts_tally_hand)
            print()

        player_total = sum(split1)
        player_total2 = sum(split2)
        dealer_total = sum(dealer_cards)

        if dealer_total > 21 >= player_total2 and player_total <= 21:
            print('Dealer Bust. Player wins all hands')
        if dealer_total > 21 >= player_total and player_total2 > 21:
            print('Dealer Bust. Player wins Hand 1.')
        if dealer_total > 21 >= player_total2 and player_total > 21:
            print('Dealer Bust. Player wins Hand 2.')

        if player_total > 21:
            print("Player Bust on Hand 1")
        if player_total2 > 21:
            print("Player Bust on Hand 2")

        if 21 >= dealer_total > player_total:
            print('Dealer Wins Hand 1')
        if 21 > dealer_total < player_total <= 21:
            print('Player Wins Hand 1')
        if 21 >= dealer_total == player_total:
            print("Push on Hand 1")

        if 21 >= dealer_total > player_total2:
            print('Dealer Wins Hand 2')
        if 21 > dealer_total < player_total2 <= 21:
            print('Player Wins Hand 2')
        if 21 >= dealer_total == player_total2:
            print("Push on Hand 2")

        print()
