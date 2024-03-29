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
    active_player = player1
    while True:
        menu = SingleMenu("Select an option", options)
        player1_selection = menu.show()
        player2_selection = menu.show()
        print(f"{player1.name} selected {player1_selection}")
        print(f"{player2.name} selected {player2_selection}")
        input("Press Enter to continue...")


def main():
    print("Welcom to the Rock, Paper, Scissors game!")
    try:
        player1 = Player(input("Player 1: "))
        player2 = Player(input("Player 2: "))
        play(player1, player2)
    except KeyboardInterrupt:
        print("\nGame ended.")

if __name__ == "__main__":
    main()
