#!/bin/python3
	 
from random import randint
    
MODES = ['TEST','DEV','PROD']
    
print(f"MODE={MODES[randint(0, len(MODES))-1]}")