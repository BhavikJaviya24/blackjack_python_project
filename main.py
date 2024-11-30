import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose. Opponent has blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Opponent went over, You win."
    else:
        return "You lose!!"


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_game = input("Type 'y' to get another card or 'n' to pass:")
            if continue_game == 'y':
                user_cards.append(random.choice(cards))
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play game of BlackJack? Type 'y' or 'n'.") == 'y':
    play_game()
