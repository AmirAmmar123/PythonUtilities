from options import DecisionMaking

class Participant:
    """
        Class representing a participant with the fields
        id , block_score represented as a list, data represented as a dictionary, chosen option from [option A, option B]
        difficulty level as randomized, reward domain randomized, total scores as integer
        id is a string  
    """
    def __init__(self, id):
        self.id = id
        self.block_scores=[]
        self.data = dict()
        self.chosen_option = str()
        self.difficulty_level = str()
        self.reward_Domain = str()
        self.total_scores = 0
        self.data["id"] = id
        
        

    """
        this function is called when a participant has to make a decision
        also will update the data dictionary with the keys reward_domain, and chosen option 
        also a function from the options module will be called 
    """
    def makeDecision(self,option, level, reward_Domain):
        self.reward_Domain = reward_Domain
        self.data["reward_Domain"] = reward_Domain
        self.chosen_option = option
        self.data["chosen_option"] = option
        self.difficulty_level = level
        gain = DecisionMaking.optionPoint(option, level)
        if self.reward_Domain == "Losses":
            return -gain
        return gain
    
    def __str__(self):
        return self.id
    