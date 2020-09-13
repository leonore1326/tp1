from numpy import random
import time

MIN_NUMBER = 1
MAX_NUMBER = 50

def game():
    ''' The game in itself    
    '''
    
    # The random number to guess
    r = random.randint(MIN_NUMBER,MAX_NUMBER)
    found = False
    k=0
    
    # (Eternal) loop
    while not found:
        
        if k==7:
            found=True
            print("you too slow... you lost !")
        else :
            entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")
            while not entry.isdigit():
                print("please input a number")
                entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")
    
            entry = int(entry)
            # Condition on what to do
            if entry<MIN_NUMBER or entry>MAX_NUMBER :
                print("You should pay attention to the rules...")
                time.sleep(10)
            if entry == r:
                print("\n\nGood job, it was "+str(r)+"!!!")
                found=True
            elif abs(r-entry)<=10 :
                print("you're getting close, but...")
            if entry>r:
                print("You're too high!")
            if entry<r:
                print("A bit more?")
            k=k+1
    	
 
# Start the game only if you wish
#playerwish = input("Hello, want to play a game? ")
#if playerwish in ["yes", "y"] :
boul=True
while boul :
    print("\n\nLet's start a game...")
    game()

	

