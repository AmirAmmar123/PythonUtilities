#!/usr/bin/env python3

import random
from rich.console import Console
import subprocess
import time

console = Console()

levels=("**Easy Level**","**Medium Level**","**Hard Level**")
gainorlose=('Gains', 'Losses')
op=("Option A", "Option B")
participant_id = 1
num_blocks = 3
num_trials_per_block = 5


def generate_banner(text):
    try:
        # Use subprocess to run the figlet command and generate the banner
        banner = subprocess.check_output(["figlet", text]).decode("utf-8")
        return banner
    except FileNotFoundError:
        print("Figlet is not installed. Please install figlet on your system.")

def welcome_message():
    """.
    Display a welcome message to the participant explaining the task.
    """
    console.print(
          "[yellow]In this experiment, you will be presented with [bold red]two options[/bold red] per trial,\n"
          "[bold red]each with different probability distributions[/bold red] of rewards.\n"
          "Your task is to [bold red]select one of[/bold red] the options, and based on the distribution,\n"
    "you will either [bold red]gain or lose[/bold red] points. Let's get started!\n"
    )
    
    input = console.input("[bold white]press enter to start[/bold white] ")  





# Constants for reward distributions
REWARD_DISTRIBUTIONS = [
    
    {'**Easy Level**': 
        
            { "Option A":[(5, 0.8), (0, 0.2)],                                   
              "Option B":(2,1.0)                                    
            }
        
    },

    
    {'**Medium Level**': 
        
            { "Option A":[(5, 0.6), (0, 0.2)],                                   
              "Option B":(2,1.0)                                    
            }
        
    },
    
    {'**Hard Level**': 
        
            { "Option A":[(5, 0.8), (0, 0.2)],                                   
              "Option B":(2,1.0)                                    
            }
        
    }
]


# Function to simulate a single trial
def simulate_trial(difficulty_level, reward_domain):
    options = REWARD_DISTRIBUTIONS[difficulty_level]
    option_chosen = input('Option A or Option B:\t')
    while option_chosen not in op:
        option_chosen = input('\033[1;31mEnter a valid option.\nOption A or Option B:\t\033[0m')
         
    reward = random.choices([option[0] for option in options], [option[1] for option in options])[0]
    return option_chosen, reward


def simulate_block(participant_id, block_number, difficulty_level, reward_domain, num_trials_per_block):
    block_data = []
    total_points = 0
    for trial_number in range(1, num_trials_per_block + 1):
        option_chosen, reward = simulate_trial(difficulty_level, reward_domain)
        total_points += reward
        block_data.append([participant_id, block_number, trial_number, difficulty_level, reward_domain, option_chosen, reward, total_points])
    return block_data    

# Function to calculate the average reward for a participant
def calculate_average_reward(participant_data):
    block_rewards = [block[-1][-1] for block in participant_data]
    return sum(block_rewards) / len(block_rewards)

def run_experiment(participant_id, num_blocks, num_trials_per_block):
    participant_data = []
    reward_domain = random.choice(gainorlose)
    
    for block_number in range(1, num_blocks + 1):
        difficulty_level = random.choice(levels)
        print(f"Difficulty level: {difficulty_level}")
        block_data = simulate_block(participant_id, block_number, difficulty_level, reward_domain, num_trials_per_block)
        
        time.sleep(0.5)
        print("new block is beginning")
        time.sleep(0.5)
        participant_data.append(block_data)
    average_reward = calculate_average_reward(participant_data)
    return participant_data, average_reward

participant_id = 1
num_blocks = 3
num_trials_per_block = 2


if __name__ == "__main__":
    banner = generate_banner("Welcome to the Decision-Making Under Uncertainty Game!\n")
    console.print (f"[bold white]{banner}")
    welcome_message()
    participant_data, average_reward = run_experiment(participant_id, num_blocks, num_trials_per_block)

    # Print participant data
    for block_data in participant_data:
        for trial_data in block_data:
            print(dict(participant_id=trial_data[0], block_number=trial_data[1], trial_number=trial_data[2], difficulty_level=trial_data[3], reward_domain=trial_data[4], option_chosen=trial_data[5], reward=trial_data[6], total_points=trial_data[7]))

    # Print average reward
    print("Average Reward:", average_reward)



