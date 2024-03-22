from advanced_selector import SingleMenu


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Option:
    def __init__(self, name, value):
        self.name = name
        self.value = value


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
    pass

def main():
    print("Welcom to the Rock, Paper, Scissors game!")
    player1 = Player(input("Player 1: "))
    player2 = Player(input("Player 2: "))
