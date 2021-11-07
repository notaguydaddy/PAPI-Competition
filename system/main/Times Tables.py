import random, json, os
import tkinter as tk

#Globals
n1, n2, questions, correct = [0 for _ in range(4)]
numbers = [x for x in range(1, 13)]
wrong = []

def Start():
    global n1, n2, question, calculation, ans, calculation
    n1, n2 = random.choice(numbers), random.choice(numbers) # Chose two random numbers
    calculation, ans = (str(n1) + " * " + str(n2), n1 * n2) if random.choice([True, False]) else (str(n1 * n2) + " / " + str(n1), n2) # Generate question and answer
    question.config(text = calculation) # Show question

def Check():
    global n1, n2, correct, questions
    try: inans = int(ansbox.get())
    except:
        (Start(), ansbox.delete(0, 99))
        return
    if inans == ans: (correct := correct + 1, score.config(text = correct))
    else: (score.config(text = "Incorrect, the correct answer was " + str(int(n1) * int(n2))), wrong.append(calculation))
    (questions := questions + 1, ansbox.delete(0, 99), Start())

# Game window
window = tk.Tk()
(question := tk.Label(text = "Question")).pack()
(ansbox := tk.Entry()).pack()
(checkbutton := tk.Button(text = "Check answer", command = Check)).pack()
(score := tk.Label(text = "Score")).pack()
(endbutton := tk.Button(text = "End game", command = lambda: window.destroy())).pack()
(timer := tk.Label()).pack()
timer.after(60000, lambda: window.destroy())
(Start(), window.mainloop())

# High score calculation
try: hs = json.load(open("highscore.json"))[0] if os.path.isfile("highscore.json") else 0
except Exception as e: hs = 0
if hs < correct: (hs := correct, json.dump([correct], open("highscore.json", "w")))

# Show details
another_window = tk.Tk()
[tk.Label(text=x).pack() for x in ["{}/{}".format(correct, questions), "High score: {}".format(hs)] + (["Here's what you got wrong:", *wrong] if len(wrong) > 0 else [])]
another_window.mainloop()