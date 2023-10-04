#!/usr/bin/env python3
from messgene import MessGene
from participant import Participant
from options import DecisionMaking
import random
import time

def simulate(participant:Participant, blocks, trails_per_block, f):
    participant.data["total_points"] = 0
    info = []
    for block in range(1, blocks + 1):
        difficulty = random.choice(DecisionMaking.difficultylevels)
        participant.data["difficulty"] = difficulty
        participant.data["block"] = block 
        for trail in range(1, trails_per_block + 1):
            participant.data["trail"] = trail
            messgene = MessGene(banner=difficulty, message="",input="option A or option B: ")
            messgene.generate_banner()
            option = messgene.generate_message()
            current_gain = participant.makeDecision(option,difficulty, random.choice(["Gains","Losses"]))
            participant.block_scores.append(current_gain)
            print(participant.data, file=f)   

              
        msg = "{} for block #{}:{:>3}"
        score = random.choice(participant.block_scores)
        participant.total_scores = participant.total_scores + score 
        participant.data["total_points"] = participant.total_scores 
        time.sleep(0.5)
        print("loading...")
        time.sleep(0.5)
        print("data being processed for end of block")
        time.sleep(0.5)
        print(msg.format(participant.reward_Domain,block ,score))    
        participant.block_scores.clear()
        time.sleep(0.5)
    print(participant.data, file=f)   
    return info
            
            
# - Participant ID
# - Block Number
# - Trial Number within Block
# - Difficulty Level
# - Reward Domain (Gains/Losses)
# - Option Chosen
# - Outcome (gain or loss)
# - Total Points after each Block            
            
            
            




if __name__ == "__main__":
   try:
        welcome = MessGene(
            banner="Welcome to the Decision-Making Under Uncertainty Game!\n",
            message = "[yellow]In this experiment, you will be presented with [bold red]two options[/bold red] per trial,\n"
            "[bold red]each with different probability distributions[/bold red] of rewards.\n"
            "Your task is to [bold red]select one of[/bold red] the options, and based on the distribution,\n"
            "you will either [bold red]gain or lose[/bold red] points. Let's get started!\n",
            input = "Please enter your ID to start"
            )
        
        welcome.generate_banner()
        id = welcome.generate_message()
        
        if not id.isdigit():
            raise ValueError("Participant id must be a number")
            
        Participant = Participant(id)
        
        blocks = MessGene(input="Enter number of blocks: ", message="").generate_message()
        if not blocks.isdigit():
            raise ValueError("Number of blocks must be a number")
        
      
        trails_per_block = MessGene(input="Enter number of trails per block: ", message="").generate_message()
        if not trails_per_block.isdigit():
            raise ValueError("Number of trails per block must be a number")
        
        blocks = int(blocks)
        trails_per_block = int(trails_per_block)
        
        with open("paricipants.log", "a") as f:
            simulate(Participant, blocks, trails_per_block, f)
            print("*"*100,file=f)
        f.close() 
        print("Your average score is: ", Participant.total_scores/blocks)

   except Exception as e:
       print(e)



