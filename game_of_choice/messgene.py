
from rich.console import Console
import subprocess
console = Console()


class MessGene:
   
    
    def __init__(self, **args):
        self.args = args
        
    def generate_banner(self):
        try:
            # Use subprocess to run the figlet command and generate the banner
            banner = subprocess.check_output(["figlet", self.args["banner"]]).decode("utf-8")
            console.print (f"[bold white]{banner}") 
        except FileNotFoundError:
            print("Figlet is not installed. Please install figlet on your system.")

    def generate_message(self):
        console.print( self.args["message"])
        iput= self.args["input"]
        return console.input(f"[bold white]{iput}[/bold white] ")
