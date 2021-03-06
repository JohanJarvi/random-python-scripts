import time
from datetime import date
from pathlib import Path
import subprocess as s
import sys

pomos = []
pomosCount = 0
pomodoroLaps = 0

# Debug:
multiplier = 60

shortBreakDurations = [5, 4, 3]
longBreakDurations = [30, 22, 15]

levelOfProductivity = int(
    input("How productive do you want to be from 1 to 3: "))

if levelOfProductivity > 3 or levelOfProductivity < 0:
    raise "Error! Cannot have an productivity level lower than 1 or higher than 3!"

path = Path(__file__).parent

try:
    readFile = open(str(path) + "/pomocounts.txt", "r")
    file = open(str(path) + "/pomocounts.txt", "a")
except:
    print("\nError! Failed to open file pomocounts.txt.\nPlease create this file in the root directory.\n")
    sys.exit()


lines = readFile.read().splitlines()
readFile.close()

if len(lines) == 0:
    file.write(str(date.today()) + "\n")
else:
    if str(date.today()) not in lines:
        file.write("\n\n" + str(date.today()) + "\n")

print("Starting pomodoro technique lets do this!")
print("    ")

def showProgressBar(minutesToProgress):
    progress = [" "] * minutesToProgress
    progressedMinutes = 0

    print("Progress: ")
    while progressedMinutes < minutesToProgress:
        progress[progressedMinutes] = "#"
        time.sleep(1 * multiplier)
        progressedMinutes += 1
        percentage = (progressedMinutes / minutesToProgress) * 100.0
        print("[" + "".join(progress) + "] - " +
              str(round(percentage)) + "% complete", end="\r")

    print("    ")


while True:
    if pomodoroLaps > 0:
        print("Here we go again! You have done " +
              str(pomodoroLaps) + " pomodoro laps so far!")
        print("    ")

    workString = "Work for " + str(25) + " minutes starting now!"
    print(workString)
    s.call(['notify-send', 'Pomodoro Counter', workString])
    showProgressBar(25)

    pomos.append("@")
    print("    ")
    print("Your total pomos are: ")
    print("".join(pomos))
    print("    ")

    file.write("@")

    pomosCount = len(pomos)

    if pomosCount == 1:
        print("Good job on your first pomo! Keep it up!")

    if pomosCount == 2:
        print("Good job on your second pomo! Stay focused!")

    if pomosCount == 3:
        print("Good job on your third pomo! You can do this!")

    if pomosCount == 4:
        print(
            "Good job on your fourth and final pomo! Go have your well deserved long break!")

    print("    ")

    if len(pomos) != 4:
        shortBreakDuration = shortBreakDurations[levelOfProductivity - 1]
        breakString = "Break for " + str(shortBreakDuration) + " minutes!"
        print(breakString)
        s.call(['notify-send', 'Pomodoro Counter', breakString])
        showProgressBar(shortBreakDuration)
        print("    ")
    else:
        longBreakDuration = longBreakDurations[levelOfProductivity - 1]
        breakString = "Break for " + str(longBreakDuration) + " minutes!"
        print(breakString)
        s.call(['notify-send', 'Pomodoro Counter', breakString])
        showProgressBar(longBreakDuration)
        pomos = []
        print("    ")
        pomodoroLaps += 1
