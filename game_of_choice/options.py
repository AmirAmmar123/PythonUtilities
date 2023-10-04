
import random

class DecisionMaking:
    difficultylevels = ["Easy Level", "Medium Level", "Hard Level"]
    options = ["option A", "option B"]
    probability_threshold_easy = 0.8   
    probability_threshold_medium = 0.6
    probability_threshold_hard = 0.5  
    
    def __init__(self):
       pass
    
    """
        this function return points according to probability that has given in the instructions 
        - **Easy Level**: Option 1 yields 5 points with 80% probability and 0 points
        with 20% probability. Option 2 yields 2 points with 100% probability.
        - **Medium Level**: Option 1 yields 5 points with 60% probability and 0 points
        with 40% probability. Option 2 yields 3 points with 100% probability.
        - **Hard Level**: Option 1 yields 6 points with 50% probability and 0 points
        with 50% probability. Option 2 yields 3 points with 100% probability.

    """
    @staticmethod
    def optionPoint(option, level):
        while option not in DecisionMaking.options:
            print(f"Invalid option:\t{option}\ntry again.")
            option = input("option A or option B:\t")
        
        # Generate a random number between 0 and 1
        random_number = random.random()

        if level == DecisionMaking.difficultylevels[0]:
            if option == "Option A":
                if random_number <= DecisionMaking.probability_threshold_easy:
                    return 5
                else:
                    return 0
            else:
                return 2
                
        elif level == DecisionMaking.difficultylevels[1]:
            if option == "Option A":
                if random_number <= DecisionMaking.probability_threshold_medium:
                    return 5 
                else:
                    return 0
            else:
                return 2
        else:
            if option == "Option A":
                if random_number <= DecisionMaking.probability_threshold_hard:
                    return 5 
                else:
                    return 0
            else:
                return 3
    