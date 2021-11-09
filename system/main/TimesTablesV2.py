from utils import *
import random as rand

while True:
    print("Question:")
    n1, n2 = [rand.randint(1, 12) for _ in range(2)]
    decider = rand.choice([True, False])
    calc, ans = (str(n1) + " * " + str(n2), n1*n2) if decider else (str(n1*n2) + " / " + str(n1), n2)
    print(calc)
    
    usrAns = input()
    # EXTRA CLEAR SOMEWHERE
    
    try: usrAns = int(usrAns)
    except:
        clear()
        continue
    
    if usrAns == ans:
        print("Correct!")
        clear(4)
        continue
    print("Incorrect, {} = {}".format(calc, ans))
    clear(4)
    
