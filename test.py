#!/usr/bin/env python3
import random

def simulate_game(difficulty):
    if difficulty == "Easy":
        option1_prob = 0.8
        option2_prob = 0.2
        option1_points = 5
        option2_points = 2
    elif difficulty == "Medium":
        option1_prob = 0.6
        option2_prob = 0.4
        option1_points = 5
        option2_points = 3
    elif difficulty == "Hard":
        option1_prob = 0.5
        option2_prob = 0.5
        option1_points = 6
        option2_points = 3
    else:
        raise ValueError("Invalid difficulty level")

    # Randomly choose between option 1 and option 2 based on probabilities
    choice = random.choices(["Option1", "Option2"], [option1_prob, option2_prob])[0]

    if choice == "Option1":
        points = option1_points
    else:
        points = option2_points

    return points

# Simulate a game on Easy difficulty
easy_points = simulate_game("Easy")
print(f"Easy Level: You earned {easy_points} points")

# Simulate a game on Medium difficulty
medium_points = simulate_game("Medium")
print(f"Medium Level: You earned {medium_points} points")

# Simulate a game on Hard difficulty
hard_points = simulate_game("Hard")
print(f"Hard Level: You earned {hard_points} points")