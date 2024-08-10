"""
This game is a pep8 style.
Players make choices to navigate through.
the ruins and find the legendary lost treasure.
"""

import time
import random


def print_pause(message):
    """To keep 2 seconds between every message."""
    print(message)
    time.sleep(2)


def invalid_input():
    """Ensure that the user choosse the correct choice."""
    choice = input("Enter your choice (1/2): ")
    while choice not in ["1", "2"]:
        print_pause("Invalid input. Please try again.")
        choice = input("Enter your choice (1/2): ")
    return choice


def play_again():
    """Ask the player if he want to play again."""
    print_pause("Would you like to play again?")
    print_pause("1. Yes")
    print_pause("2. No")
    choice = invalid_input()
    if choice == "1":
        start_game()
    elif choice == "2":
        print_pause("Thanks for playing DECI ancient ruins adventure game!")


def start_game():
    """Start the game."""
    score = 0
    intro(score)


def intro(score):
    """Introduction and first choice."""
    print_pause("Welcome to the DECI ancient ruins adventure game!")
    print_pause(
        "A long time ago, a rich man buried a treasure within the depths "
        "of a ruin. Many have tried to find it, but they have failed. Now, "
        "brave adventurer, it is your turn to find the legendary lost "
        "treasure. Will you succeed where others have failed?"
    )
    print_pause("1. Not sure")
    print_pause("2. I will nail it")
    choice = invalid_input()
    if choice == "1":
        print_pause("Give it a try")
        score += 5
    elif choice == "2":
        print_pause("What a brave adventurer!")
        score += 10
    print_pause(f"Current score: {score}")
    print_pause(
        "Now, you stand before the entrance of the ruins. The air is thick "
        "with the scent of dust."
    )
    first_choice(score)


def first_choice(score):
    """Take the first choice in the game."""
    print_pause("1. Enter the ruins")
    print_pause("2. Examine the entrance")
    choice = invalid_input()
    if choice == "1":
        scenarios = [
            "The first room is vast, with huge statues of warriors. At the "
            "center, a stone holds a dilapidated map.",
            "You enter a dimly lit hallway,"
            "the walls covered in ancient runes and moss."
        ]
        print_pause(random.choice(scenarios))
    elif choice == "2":
        score += 10
        warnings = [
            "The symbols are warnings left by the rich man. They speak of "
            "traps and witches that protect the treasure.",
            "You find ancient carvings that hint at dangerous guardians and "
            "deadly traps within the ruins."
        ]
        print_pause(random.choice(warnings))
        print_pause("You must proceed with caution. Now you enter the room.")
        print_pause(
            "The first room is vast, with huge statues of warriors. At the "
            "center, a stone holds a dilapidated map."
        )
    print_pause(f"Current score: {score}")
    second_choice(score)


def second_choice(score):
    """Take the second choice in the game."""
    print_pause("1. Take the map")
    print_pause("2. Inspect the statues")
    choice = invalid_input()
    if choice == "1":
        print_pause(
            "The map shows the layout of the ruins,"
            "with several rooms marked."
            "This will help us get through a lot."
        )
    elif choice == "2":
        score += 10
        observations = [
            "The statues are carved with intricate detail, each depicting a "
            "different witch of the treasure. Their eyes seem to follow your "
            "every move.",
            "The statues seem almost lifelike, their expressions frozen in a "
            "mix of anger and sorrow."
        ]
        print_pause(random.choice(observations))
        print_pause("Now you take the map from the stone.")
        print_pause(
            "The map shows the layout of the ruins,"
            "with several rooms marked."
            "This will help us get through a lot."
        )
    print_pause(f"Current score: {score}")
    third_choice(score)


def third_choice(score):
    """Take the third choice in the game."""
    print_pause(
        "Whenever you walk a little, the floor is shaking a little, and darts "
        "shoot out from the walls. The path ahead is littered with traps "
        "designed to stop the thieves."
    )
    print_pause("1. Use the map to navigate the traps.")
    print_pause("2. Attempt to dodge the traps.")
    choice = invalid_input()
    if choice == "1":
        print_pause(
            "By using the map, you successfully navigate the trap, avoiding "
            "the deadly darts."
        )
        print_pause(
            "A huge stone witch awakens as you enter the room. Its eyes glow "
            "with a menacing light, and it moves to attack."
        )
        print_pause(f"Current score: {score}")
        fourth_choice(score)
    elif choice == "2":
        if random.choice([True, False]):
            print_pause(
                "You successfully dodge the traps "
                "and overcome the difficulties."
            )
            score += 10
            print_pause(f"Current score: {score}")
            fourth_choice(score)
        else:
            print_pause(
                "You try to dodge the traps, "
                "but a dart cuts your arm. You try "
                "to survive, but you are wounded."
            )
            score -= 10
            print_pause(f"Current score: {score}")
            print_pause("Game over")
            print_pause(f"Score: {score}")
            play_again()


def fourth_choice(score):
    """Take the fourth choice in the game."""
    print_pause("1. Fight the witch")
    print_pause("2. Use the environment to outsmart the witch")
    choice = invalid_input()
    if choice == "1":
        score -= 10
        print_pause("You fought bravely, "
                    "but the witch is powerful. She defeated you.")
        print_pause(f"Current score: {score}")
        print_pause("Game over")
        print_pause(f"Score: {score}")
        play_again()
    elif choice == "2":
        print_pause(
            "You notice a series of levers on the walls."
            "Using them, you operate "
            "a trap that immobilizes the witch, allowing you to pass safely."
        )
        print_pause(
            "You've made it to the treasure room. The room is filled with "
            "untold wealth, the legendary lost treasure of the rich man."
        )
        print_pause(f"Current score: {score}")
        fifth_choice(score)


def fifth_choice(score):
    """Take the fifth choice in the game."""
    print_pause("1. Take the treasure and leave")
    print_pause("2. Explore the room for more secrets.")
    choice = invalid_input()
    if choice == "1":
        print_pause("Carry as much of this treasure as you can.")
        print_pause(
            "Your journey through the ruins has been successful. You emerge "
            "into the sunlight, the treasure safe in your hands."
            "Your adventure has made you an unforgettable legend."
        )
        print_pause("Congratulations! You win")
        print_pause(f"Score: {score}")
        play_again()
    elif choice == "2":
        score += 10
        discoveries = [
            "You discover an ancient journal detailing the rich man's history "
            "and the true purpose of the treasure."
            "This knowledge is invaluable.",
            "Hidden behind a false wall, you find a secret room filled with "
            "ancient artifacts and scrolls."
        ]
        print_pause(random.choice(discoveries))
        print_pause("Carry as much of this treasure as you can.")
        print_pause(
            "Your journey through the ruins has been successful. You emerge "
            "into the sunlight, the treasure safe in your hands."
            "Your adventure has made you an unforgettable legend."
        )
        print_pause("Congratulations! You win")
        print_pause(f"Score: {score}")
        play_again()


start_game()
