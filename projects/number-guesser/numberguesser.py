import random
from colorama import Fore, Style, init

init(autoreset=True)

def colored_input(prompt, color):
    return input(color + prompt + Style.RESET_ALL)

def guess_the_number():
    print("Welcome to the Number Guessing Game!")

    # Get the user's name
    user_name = colored_input("Enter your username: ", Fore.BLUE)
    
    # Get the maximum limit for the random number
    max_limit = int(colored_input("Enter the maximum limit for the number (e.g., 100): ", Fore.GREEN))
    print(f"Hello, {Fore.BLUE}{user_name}{Style.RESET_ALL}! I'm thinking of a number between {Fore.GREEN}1{Style.RESET_ALL} and {Fore.GREEN}{max_limit}{Style.RESET_ALL}.")

    # Calculate the rate for reducing the final score
    rate = 100 / (max_limit / 1000)  # You can adjust the factor as needed

    print(f"The rate for your score will be: {Fore.YELLOW}{rate}{Style.RESET_ALL}.")

    # Generate a random number between 1 and the specified maximum limit
    secret_number = random.randint(1, max_limit)

    attempts = 0
    while True:
        user_guess = int(colored_input("Your guess: ", Fore.CYAN))
        attempts += 1

        if user_guess < secret_number:
            print(Fore.RED + "Too small! Try again." + Style.RESET_ALL)
        elif user_guess > secret_number:
            print(Fore.RED + "Too big! Try again." + Style.RESET_ALL)
        else:
            print(f"Congratulations, {Fore.BLUE}{user_name}{Style.RESET_ALL}! You guessed the number in {Fore.GREEN}{attempts}{Style.RESET_ALL} attempts.")
            break

    # The bigger the number the better the rate will be

    # percent = abs(1 - rate) / max(1, rate) * 100

    final_score = attempts * (rate / 100);

    print(f"With a multiplier of {Fore.GREEN if rate <= 100 else Fore.RED}{rate / 100}{Style.RESET_ALL}, ", end='')
    print(f"You're final score is: {Fore.YELLOW}{final_score}{Style.RESET_ALL}.")
    
    # Update and display the score
    update_score(user_name, final_score)

def update_score(user_name, final_score):
    # Read the existing scores from a file
    scores = {}
    try:
        with open("scores.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                scores[name] = float(score)
    except FileNotFoundError:
        pass

    # Update the score for the current user
    if user_name in scores:
        scores[user_name] = min(scores[user_name], final_score)
    else:
        scores[user_name] = final_score

    # Write the updated scores back to the file
    with open("scores.txt", "w") as file:
        for name, score in scores.items():
            file.write(f"{name},{score}\n")

    # Display the scores in ascending order
    print(Fore.YELLOW + "\nHigh Scores (Smaller is Better):" + Style.RESET_ALL)
    for name, score in sorted(scores.items(), key=lambda x: x[1]):
        print(f"{Fore.BLUE}{name}{Style.RESET_ALL}: {Fore.GREEN}{score:.2f} final score{Style.RESET_ALL}")

if __name__ == "__main__":
    guess_the_number()
