"""
Bugs:
1. splits and doubles inside of splits
2. Counting stats for split plays
3. collecting stats on splits
4. collecting stats on doubles
5. Create a betting strategy
6. keep count of cards
"""

# Imports and globals go here:
one_suit_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
shoe = one_suit_cards * 8

dealer_blackjack_tally = []
player_blackjack_tally = []
player_wins_tally = []
dealer_wins_tally = []
player_busts_tally = []
dealer_busts_tally = []
push_tally = []


# Functions go here:

# Function for basic strategy
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

            if player_cards[0] in [4, 5, 6, 9, 10]:
                check1 = True

        if dealer_card in [5, 6]:
            if player_cards[0] in ['A', 2, 3, 4, 6, 7, 8, 9]:
                move = 'x'

            if player_cards[0] in [5, 10]:
                check1 = True

        if dealer_card in [2, 3, 4]:
            if player_cards[0] in ['A', 2, 3, 6, 7, 8, 9]:
                move = 'x'

            if player_cards[0] in [4, 5, 10]:
                check1 = True

    if (player_cards.count('A') == 0 and player_cards[0] != player_cards[1]) or (
            check1 is True):  # Hard Totals, no aces or splits
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
        player_cards.append("A")

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

        if player_total == 10:
            move = 's'

    return move


# Function to get the statistics
def stats(dealer_blackjack_tally, player_blackjack_tally, player_wins_tally, dealer_wins_tally,
          player_busts_tally, dealer_busts_tally, push_tally, dealer_blackjack_tally_hand, player_blackjack_tally_hand,
          player_wins_tally_hand, dealer_wins_tally_hand, player_busts_tally_hand, de0aler_busts_tally_hand,
          push_tally_hand):
    dealer_blackjack_final_hand = 'The number of dealer blackjacks in this shoe are:' + ' ' + str(
        sum(dealer_blackjack_tally_hand))
    player_blackjack_final_hand = 'The number of player blackjacks in this shoe are:' + ' ' + str(
        sum(player_blackjack_tally_hand))

    player_wins_final_hand = 'The number of player wins in this shoe are:' + ' ' + str(sum(player_wins_tally_hand))
    dealer_wins_final_hand = 'The number of dealer wins in this shoe are:' + ' ' + str(sum(dealer_wins_tally_hand))
    player_busts_final_hand = 'The number of player busts in this shoe are:' + ' ' + str(sum(player_busts_tally_hand))
    dealer_busts_final_hand = 'The number of dealer busts in this shoe are:' + ' ' + str(sum(dealer_busts_tally_hand))
    push_final_hand = 'The number of pushes in this shoe are:' + ' ' + str(sum(push_tally_hand))

    player_wins_hand = sum(player_wins_tally_hand) + sum(dealer_busts_tally_hand) + sum(player_blackjack_tally_hand)
    player_losses_hand = (sum(dealer_wins_tally_hand) + sum(player_busts_tally_hand) + sum(dealer_blackjack_tally_hand))
    total_player_wins_hand = 'The total number of hands the player won in this shoe was:' + ' ' + str(player_wins_hand)
    total_player_losses_hand = 'The total number of hands the player lost in this shoe was:' + ' ' + str(
        player_losses_hand)

    print(dealer_blackjack_final_hand)
    print(player_blackjack_final_hand)
    print(player_wins_final_hand)
    print(dealer_wins_final_hand)
    print(player_busts_final_hand)
    print(dealer_busts_final_hand)
    print(push_final_hand)
    print(total_player_wins_hand)
    print(total_player_losses_hand)

    # Stats for all shoes played
    dealer_blackjack_final = 'The number of dealer blackjacks are:' + ' ' + str(sum(dealer_blackjack_tally))
    player_blackjack_final = 'The number of player blackjacks are:' + ' ' + str(sum(player_blackjack_tally))
    player_wins_final = 'The number of player wins are:' + ' ' + str(sum(player_wins_tally))
    dealer_wins_final = 'The number of dealer wins are:' + ' ' + str(sum(dealer_wins_tally))
    player_busts_final = 'The number of player busts are:' + ' ' + str(sum(player_busts_tally))
    dealer_busts_final = 'The number of dealer busts are:' + ' ' + str(sum(dealer_busts_tally))
    push_final = 'The number of pushes are:' + ' ' + str(sum(push_tally))

    player_wins = sum(player_wins_tally) + sum(dealer_busts_tally) + sum(player_blackjack_tally)
    player_losses = (sum(dealer_wins_tally) + sum(player_busts_tally) + sum(dealer_blackjack_tally))
    total_player_wins = 'The total number of hands the player won was:' + ' ' + str(player_wins)
    total_player_losses = 'The total number of hands the player lost was:' + ' ' + str(player_losses)
    print()
    print()
    lead = "The stats for all hands played in total are:"
    num_hands = player_wins + player_losses + sum(push_tally)
    num_hands_string = 'Total number of hands played:', str(player_wins + player_losses)
    wins = (player_wins / num_hands) * 100
    win_percentage = "{} {:.2f}{}".format('Percentage of wins:', wins, '%')
    lose_percentage = "{} {:.2f}{}".format('Percentage of losses:', (player_losses / num_hands) * 100, '%')
    tie_percentage = "{} {:.2f}{}".format('Percentage of ties:', (sum(push_tally) / num_hands) * 100, '%')
    return (
        lead, dealer_blackjack_final, player_blackjack_final, player_wins_final, dealer_wins_final, player_busts_final,
        dealer_busts_final, push_final, total_player_wins, total_player_losses, num_hands_string, win_percentage,
        lose_percentage, tie_percentage)


# Function for dealer strategy
def dealer_strategy(dealer_cards, dealer_busts_tally_hand):
    global dealer_total

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

            if new_card == 'A' and dealer_total in [11, 12, 13, 14, 15, 16, 17]:
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
                    for v in range(dealer_ace_count):
                        if sum(dealer_cards) > 21 and v != dealer_ace_count:
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
        print("Dealer Bust. Player wins")
        dealer_busts_tally.append(1)
        dealer_busts_tally_hand.append(1)

    return ''


# Function for player splits
def split(player_cards, dealer_cards):
    split1 = [player_cards[0]]
    split2 = [player_cards[1]]
    new_card = shoe.pop(0)
    split1.append(new_card)
    new_card = shoe.pop(0)
    split2.append(new_card)

    print("Hand 1:", split1)
    print("Hand 2:", split2)

    ace_check = False
    if player_cards == ['A', 'A']:
        move = "s"
        ace_check = True

    # HAND 1
    if ace_check is False:
        print("For the first hand:")
        move = basic_player_strategy(split1, dealer_cards[0])
        bust_checker = True  # This is solely for a player bust on a split hand

        if move == 'x':
            print("Splitting again on your first hand")
            if move == 'x' and split1[0] == split1[1]:
                split(split1, dealer_cards)

        if move == 'd':

            split1.append(shoe.pop(0))

            # For when player hits and receives an Ace
            if split1.count('A') > 0:
                player_ace_count = split1.count('A')
                for y in range(player_ace_count):
                    split1[split1.index('A')] = 11
                for z in range(split1.count(11)):
                    if sum(split1) > 21 and z != split1.count(11):
                        split1.remove(11)
                        split1.append(1)

                if sum(split1) > 21:
                    print('Player Bust. You lose')

            player_total = sum(split1)
            print(split1, "Total:", player_total)
            if player_total > 21:
                print('Player Bust. You Lose')
                print()

            move = 's'

        while move == 'h':
            split1.append(shoe.pop(0))

            if split1.count('A') > 0:
                player_ace_count = split1.count('A')
                for q in range(player_ace_count):
                    split1[split1.index('A')] = 11
                for w in range(split1.count(11)):
                    if sum(split1) > 21 and w != split1.count(11):
                        split1.remove(11)
                        split1.append(1)

            player_total = sum(split1)
            print(split1, "Total:", player_total)
            if player_total > 21:
                bust_checker = False
                move = 's'

            if bust_checker is True:
                move = basic_player_strategy(split1, dealer_cards[0])

        if move == 's':

            # If there are aces in players cards
            player_ace_count = split1.count('A')
            if split1.count('A') > 0:
                for k in range(player_ace_count):
                    split1[split1.index('A')] = 11
                for j in range(split1.count(11)):
                    if sum(split1) > 21 and j != split1.count(11):
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

                # For when player hits and receives an Ace
                if split2.count('A') > 0:
                    player_ace_count = split2.count('A')
                    for g in range(player_ace_count):
                        split2[split2.index('A')] = 11
                    for u in range(split2.count(11)):
                        if sum(split2) > 21 and u != split2.count(11):
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

                if split2.count('A') > 0:
                    player_ace_count = split2.count('A')
                    for p in range(player_ace_count):
                        split2[split2.index('A')] = 11
                    for n in range(split2.count(11)):
                        if sum(split2) > 21 and n != split2.count(11):
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
            for r in range(player_ace_count):
                split2[split2.index('A')] = 11
            for c in range(split2.count(11)):
                if sum(split2) > 21 and c != split2.count(11):
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


# Function to play BlackJack:
def blackjack():
    import random as r
    global shoe
    shoe = one_suit_cards * 8
    r.shuffle(shoe)
    del shoe[0]  # Dealer always burns first card

    dealer_blackjack_tally_hand = []
    player_blackjack_tally_hand = []
    player_wins_tally_hand = []
    dealer_wins_tally_hand = []
    player_busts_tally_hand = []
    global dealer_busts_tally_hand
    dealer_busts_tally_hand = []
    push_tally_hand = []

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
            dealer_blackjack_tally_hand.append(1)
            continue

        # Player BlackJack
        blackjack_hand = [['A', 10], [10, 'A']]
        if player_cards in blackjack_hand:
            print("BlackJack. Winner Winner Chicken Dinner")
            player_blackjack_tally.append(1)
            player_blackjack_tally_hand.append(1)
            continue

        move = basic_player_strategy(player_cards, dealer_cards[0])

        # If player splits
        if move == 'x' and player_cards[0] == player_cards[1]:
            var = False
            split(player_cards, dealer_cards)

        # If player hits
        if var is True:

            if move == 'd':

                player_cards.append(shoe.pop(0))

                # For when player hits and receives an Ace
                if player_cards.count('A') > 0:
                    player_ace_count = player_cards.count('A')
                    for b in range(player_ace_count):
                        player_cards[player_cards.index('A')] = 11
                    for r in range(player_cards.count(11)):
                        if sum(player_cards) > 21 and r != player_cards.count(11):
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
                    player_busts_tally_hand.append(1)
                    break

                move = 's'

            while move == 'h':
                player_cards.append(shoe.pop(0))

                # For when player hits and receives an Ace

                if player_cards.count('A') > 0:
                    player_ace_count = player_cards.count('A')
                    for p in range(player_ace_count):
                        player_cards[player_cards.index('A')] = 11
                    for g in range(player_cards.count(11)):
                        if sum(player_cards) > 21 and g != player_cards.count(11):
                            player_cards.remove(11)
                            player_cards.append(1)

                # To calculate player score
                player_total = sum(player_cards)
                print(player_cards, "Total:", player_total)
                if player_total > 21:
                    print('Player Bust. You Lose')
                    print()
                    player_busts_tally.append(1)
                    player_busts_tally_hand.append(1)
                    break
                move = basic_player_strategy(player_cards, dealer_cards[0])

        # If player stands
        if var is True:
            if move == 's':

                # If there are aces in players cards
                player_ace_count = player_cards.count('A')
                for h in range(player_ace_count):
                    player_cards[player_cards.index('A')] = 11
                for k in range(player_cards.count(11)):
                    if sum(player_cards) > 21 and k != (player_cards.count(11)):
                        player_cards.remove(11)
                        player_cards.append(1)

                if sum(player_cards) > 21:
                    print('Player Bust. You lose')
                    player_busts_tally.append(1)
                    player_busts_tally_hand.append(1)

                player_total = sum(player_cards)
                print("The Dealer Hand is:", dealer_cards)
                dealer_strategy(dealer_cards, dealer_busts_tally_hand)
                print()

                dealer_total = sum(dealer_cards)
                if 21 >= dealer_total > player_total:
                    print('Dealer Wins')
                    dealer_wins_tally.append(1)
                    dealer_wins_tally_hand.append(1)
                if 21 > dealer_total < player_total <= 21:
                    print('Player Wins')
                    player_wins_tally.append(1)
                    player_wins_tally_hand.append(1)
                if 21 >= dealer_total == player_total:
                    print("Push")
                    push_tally.append(1)
                    push_tally_hand.append(1)

    print(stats(dealer_blackjack_tally, player_blackjack_tally, player_wins_tally, dealer_wins_tally,
                player_busts_tally, dealer_busts_tally, push_tally, dealer_blackjack_tally_hand,
                player_blackjack_tally_hand,
                player_wins_tally_hand, dealer_wins_tally_hand, player_busts_tally_hand, dealer_busts_tally_hand,
                push_tally_hand))

    return ''


# ##############################END FUNCTIONS############################
if __name__ == '__main__':
    for i in range(1):
        print(blackjack())

