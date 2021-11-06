import tkinter as tk
import random
import matplotlib.pyplot as plt
import json

global noofquestions
noofquestions = []

global accuracy_rates
accuracy_rates = []

global wrong
wrong = []

def Start():
    global n1
    global n2
    global ansbox
    global question
    global calculation
    global s
    
    n1 = random.choice(numbers)
    n1 = str(n1)
        
    n2 = random.choice(numbers)
    n2 = str(n2)

    global decider

    decider = random.randint(1, 2)

    if decider == 1:
        calculation = n1 + " X " + n2
    
    elif decider == 2:
        calculation = str(int(n1) * int(n2)) + " / " + n1

    question.config(text = calculation)

    noofquestions.append("thing")

    accuracy_rates.append((len(something) / len(noofquestions)) * 100)

def end():
    hmm = tk.Label(text = "Here are all of the calculations you got wrong. Close this window to see your accuracy rate graph!")
    hmm.pack()
    for i in range(len(wrong)):
        tag = tk.Label(text = wrong[i])
        tag.pack()

def Check():
    userinput = ansbox.get()
    userinput = int(userinput)
    if decider == 1:
        if userinput == int(n1) * int(n2):
            something.append("something")
            score.config(text = len(something))

        else:
            score.config(text = "WRONG. The correct answer was " + str(int(n1) * int(n2)))
            wrong.append(calculation)

    elif decider == 2:
        if userinput == int(n1) * int(n2) / int(n1):
            something.append("something")
            score.config(text = len(something))
        else:
            score.config(text = "WRONG. The correct answer was " + n1)
            wrong.append(calculation)

    ansbox.delete(0, 99)

    Start()


window = tk.Tk()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

something = []

running = True

question = tk.Label(text = "Question")
ansbox = tk.Entry()
checkbutton = tk.Button(text = "CHECK", command = Check)
score = tk.Label(text = "Score")
endbutton = tk.Button(text = "END", command = end)
timerlabel = tk.Label(text = "")

question.pack()
ansbox.pack()
checkbutton.pack()
score.pack()
endbutton.pack()
timerlabel.pack()

timerlabel.after(60000, end)

Start()

window.mainloop()

figure = plt.plot(accuracy_rates)
plt.xlabel("Questions")
plt.ylabel("Accuracy rate")
plt.show()

highscores = []
newscore = (len(something))
highscores.append(newscore)
highscoreFile = open('highscore.txt', 'w+')
json.dump(highscores, highscoreFile)
highscoreFile.close()

another_window = tk.Tk()

high_score_thing = tk.Label(text = "See your high scores in highscore.txt!")

high_score_thing.pack()

another_window.mainloop()
