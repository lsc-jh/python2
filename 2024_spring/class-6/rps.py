from advanced_selector import SingleMenu


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Option:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name


options = [
    Option("Rock", "rock"),
    Option("Paper", "paper"),
    Option("Scissors", "scissors")
]


def option_hits(option1, option2):
    if option1 == option2:
        return None

    if option1 == "rock" and option2 == "scissors":
        return True

    if option1 == "scissors" and option2 == "paper":
        return True
    
    if option1 == "paper" and option2 == "rock":
        return True

    return False


def play(player1, player2):
    while True:
        menu = SingleMenu(f"{player1.name}, select an option", options)
        player1_selection = menu.show()
        if player1_selection is None:
            print("Player 1 not selected an option.")
            break

        menu = SingleMenu(f"{player2.name}, select an option", options)
        player2_selection = menu.show()
        if player2_selection is None:
            print("Player 2 not selected an option.")
            break

        p1_hit_p2 = option_hits(player1_selection.value, player2_selection.value)
        print(f"{player1.name}: {player1_selection.value} - {player2.name}: {player2_selection.value}")
        if p1_hit_p2 is None:
            print("Draw")
        if p1_hit_p2:
            player1.score += 1
            print(f"{player1.name} wins!")
        else:
            player2.score += 1
            print(f"{player2.name} wins!")
        input("Press Enter to continue...")
    print(f"{player1.name}: {player1.score} - {player2.name}: {player2.score}")


def who_won(player1, player2):
    if player1.score > player2.score:
        print(f"{player1.name} wins!")
    elif player1.score < player2.score:
        print(f"{player2.name} wins!")
    else:
        print("Draw!")


def main():
    print("Welcom to the Rock, Paper, Scissors game!")
    player1 = Player(input("Player 1: "))
    player2 = Player(input("Player 2: "))
    try:
        play(player1, player2)
        who_won(player1, player2)
    except KeyboardInterrupt:
        who_won(player1, player2)
        print("\nGame ended.")


if __name__ == "__main__":
    main()
