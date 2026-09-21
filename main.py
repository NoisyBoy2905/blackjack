from colorama import Fore, init
from hand import Deck, Hand

init(autoreset=True)

def divider():
    print("-" * 40)

def clear_screen():
    print("\033[H\033[J", end="")

def show_hand(name, hand, total):
    print(f"{name}: {hand} | Total: {total}")

def blackjack(deck):

    double = False
    first_turn = True

    player_hand = Hand([deck.deal_card(), deck.deal_card()])
    dealer_hand = Hand([deck.deal_card(), deck.deal_card()])

    player_total = player_hand.hand_total()
    dealer_total = dealer_hand.hand_total()

    divider()
    show_hand("Player", player_hand, player_total)
    print(f"Dealer: {dealer_hand[0]} and one HIDDEN")
    divider()

    if player_total == 21:
        if dealer_total == 21:
            print(Fore.LIGHTMAGENTA_EX + "Tie! Both have blackjack.")
            return "tie", double
        print(Fore.GREEN + "Player Blackjack!")
        return "blackjack", double

    while player_total < 21:
        action = input(Fore.CYAN + "\n[H]it, [S]tand or [D]ouble? ").strip().upper()

        if action == "H":
            first_turn = False
            card = deck.deal_card()
            player_hand.add_card(card)
            player_total = player_hand.hand_total()
            print(Fore.CYAN + f"\nYou drew {card}")
            show_hand("Player", player_hand, player_total)

            if player_total > 21:
                print(Fore.RED + "\nPlayer bust! Dealer wins.")
                return "loss", double
            elif player_total == 21:
                print(Fore.GREEN + "\nPlayer hits 21!")
                break

        elif action == "S":
            first_turn = False
            break

        elif action == "D":
            if not first_turn:
                print(Fore.RED + "\nCan only double down on your first turn!")
                continue
            double = True
            card = deck.deal_card()
            player_hand.add_card(card)
            player_total = player_hand.hand_total()
            print(Fore.CYAN + f"\nYou drew {card}")
            show_hand("Player", player_hand, player_total)

            if player_total > 21:
                print(Fore.RED + "\nPlayer bust! Dealer wins.")
                return "loss", double
            break

        else:
            print(Fore.RED + "\nInvalid choice! Enter H, S or D.")

    # ---- Dealer's turn ----
    divider()
    show_hand("Dealer", dealer_hand, dealer_total)

    if dealer_total == 21:
        print(Fore.RED + "\nDealer Blackjack! Dealer wins.")
        return "loss", double

    while dealer_total < 17:
        card = deck.deal_card()
        dealer_hand.add_card(card)
        dealer_total = dealer_hand.hand_total()
        print(Fore.CYAN + f"\nDealer drew {card}")
        show_hand("Dealer", dealer_hand, dealer_total)

    # ---- Result ----
    divider()
    if dealer_total > 21 or player_total > dealer_total:
        print(Fore.GREEN + f"Player wins! {player_total} vs {dealer_total}")
        return "win", double
    elif dealer_total > player_total:
        print(Fore.RED + f"Dealer wins! {dealer_total} vs {player_total}")
        return "loss", double
    else:
        print(Fore.LIGHTMAGENTA_EX + f"Tie! Both have {player_total}")
        return "tie", double

def main():

    wins = 0
    losses = 0
    tie = 0

    keep_playing = True
    deck = Deck()
    deck.shuffle()

    chips = 100

    while keep_playing:
        clear_screen()

        if len(deck) < 15:
            deck = Deck()
            deck.shuffle()

        divider()
        print(Fore.LIGHTMAGENTA_EX + f"Chips: {chips}  |  Wins: {wins}  Losses: {losses}  Draws: {tie}")
        divider()

        bet = 0
        while bet <= 0 or bet > chips:
            try:
                bet = int(input(Fore.CYAN + "How much would you like to bet? ").strip())
            except ValueError:
                print(Fore.RED + "Enter a number!")
                continue

            if bet > chips:
                print(Fore.RED + "You do not have enough!")
            elif bet <= 0:
                print(Fore.RED + "Bet must be more than 0!")

        result, doubled = blackjack(deck)

        payout = bet * 2 if doubled else bet

        if result == "win":
            wins += 1
            chips += payout
        elif result == "loss":
            losses += 1
            chips -= payout
        elif result == "tie":
            tie += 1
        elif result == "blackjack":
            wins += 1
            chips += round(bet * 1.5)

        if chips == 0:
            print(Fore.RED + "\nYou are broke! Game over.")
            break

        choice = input(Fore.CYAN + "\nPlay again? [Y/N] ").strip().upper()
        if choice != "Y":
            keep_playing = False

    divider()
    print(Fore.LIGHTMAGENTA_EX + f"Final: Wins: {wins} | Losses: {losses} | Draws: {tie}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()