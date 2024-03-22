
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
