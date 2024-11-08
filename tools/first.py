import os
from modules.logger import logger as lg

def first():
    return "hey i'm the first tools"


if __name__ == "__main__":
    res = first()
    
else :
    res = f"first has been called"
    #tooler = "my tool result"


print(os.getcwd())







lg.output(res)


