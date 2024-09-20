#blackjack game
import random

# regles la somme des cartes d'un joueur ne doit pas depasser les 21 points
# si la somme est dépassée le joueur a perdu
# si les la somme est en dessous de 16 le joueurs a perdu

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# demande a l'utilisateur s'il veut joueur

player_choice = [random.choice(cards), random.choice(cards)]
total_player = sum(player_choice)
computer_list = []
computer_first_card = random.choice(cards)
computer_list.append(computer_first_card)
sum_computer = sum(computer_list)


def start_the_game():
    print(f"your cards: {player_choice}, current score : {total_player}")
    print(f"computer first card:  {computer_first_card}")


def update_score_player(total_score_player, choose_card):
    total_score_player += choose_card
    return total_score_player


def add_new_card(list_card_player, choose_card):
    list_card_player.append(choose_card)
    return list_card_player


def random_card():
    return random.choice(cards)


def find_winner(gamer, comp):
    if gamer > 21 or gamer < 16:
        return "computer wins ... "
    elif comp > 21 or comp < 16:
        return "player wins ... "
    if gamer > comp:
        return "player wins..."
    elif comp > gamer:
        return "computer wins..."
    else:
        return "draw..."


start_game = input("do you want to play the blackjack ? : ")


if start_game == "y":
    choice = start_game
    while start_game == "y":
        start_the_game()
        while choice == 'y' and total_player <= 21:
            choice = input("type 'y' to get another card, 'n' to pass------------ : ")
            if choice == 'y':
                new_card = random_card()
                newList = add_new_card(player_choice, new_card)
                player_choice = newList
                total_player = update_score_player(total_player, new_card)

                # computer
                computer_card = random_card()
                computer_new_list = add_new_card(computer_list, computer_card)
                computer_list = computer_new_list
                sum_computer = sum(computer_new_list)

                start_the_game()

        if choice == "n" or start_game == "n" and (total_player < 21):
            while sum_computer < 21 and sum_computer < total_player:
                computer_card = random_card()
                computer_new_list = add_new_card(computer_list, computer_card)
                computer_list = computer_new_list
                sum_computer = sum(computer_new_list)

            print(f"your final choices :  {player_choice}, total : {total_player}")
            print(f"computer choices :  {computer_list}, total : {sum_computer}")
            print(find_winner(total_player,sum_computer))

        start_game = input("do you want to play the blackjack ? : ")
        if start_game == "y":
            print("__--------______---------_____new game______")
            choice = start_game
            player_choice = [random.choice(cards), random.choice(cards)]
            total_player = sum(player_choice)
            computer_list = []
            computer_first_card = random.choice(cards)
            computer_list.append(computer_first_card)
            sum_computer = sum(computer_list)

print("fin du jeu ... ")


