import random, json, os
import tkinter as tk

#Globals
n1, n2, questions, correct = [0 for _ in range(4)] # Initializing variables
numbers = [x for x in range(1, 13)] # Question range 
wrong = [] # Wrong questions

def Start(): # Generate questions
    global n1, n2, question, calculation, ans, calculation # Load mutable variables
    n1, n2 = random.choice(numbers), random.choice(numbers) # Chose two random numbers
    calculation, ans = (str(n1) + " * " + str(n2), n1 * n2) if random.choice([True, False]) else (str(n1 * n2) + " / " + str(n1), n2) # Generate question and answer
    question.config(text = calculation) # Show question

def Check():
    global n1, n2, correct, questions # Load mutable variables
    try: inans = int(ansbox.get()) # Try and convert input to int
    except:
        (Start(), ansbox.delete(0, 99)) # Back to Start()
        return
    if inans == ans: (correct := correct + 1, score.config(text = correct)) # If correct answer, increment correct counter and score label
    else: (score.config(text = "Incorrect, the correct answer was " + str(int(n1) * int(n2))), wrong.append(calculation)) # Else, show correct answer and add to wrong list
    (questions := questions + 1, ansbox.delete(0, 99), Start()) # Increment total questions counter and return to Start()

# Game window
window = tk.Tk()

# Window items
(question := tk.Label(text = "Question")).pack()
(ansbox := tk.Entry()).pack()
(checkbutton := tk.Button(text = "Check answer", command = Check)).pack()
(score := tk.Label(text = "Score")).pack()
(endbutton := tk.Button(text = "End game", command = lambda: window.destroy())).pack()
(timer := tk.Label()).pack()

timer.after(60000, lambda: window.destroy()) # Timeout timer
(Start(), window.mainloop()) # Generate question and start game

# High score calculation
try: hs = json.load(open("highscore.json"))[0] if os.path.isfile("highscore.json") else 0 # Check if highscore exist
except Exception as e: hs = 0 # Default to 0
if hs < correct: (hs := correct, json.dump([correct], open("highscore.json", "w"))) # Write current highscore to json file

# Show stats
another_window = tk.Tk()
[tk.Label(text=x).pack() for x in ["{}/{}".format(correct, questions), "High score: {}".format(hs)] + (["Here's what you got wrong:", *wrong] if len(wrong) > 0 else [])] #Load labels
another_window.mainloop()