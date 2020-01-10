#! python3
# stopwatch.py - A simple stopwatch program.

import time, pyperclip

# Display the program's instructions.
print("Press ENTER to begin. Afterwards, press ENTER to \"click\" the "
      "stopwatch. Press CTRL-C to quit.")
input()     # press ENTER to begin
print("Started")
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1
ourText = []

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        var = "Lap # " + str(lapNum).rjust(2) + ": " + str(totalTime).rjust(6) + " (" + str(lapTime).rjust(6) + ")"
        print(var, end="")
        ourText.append(var)
        lapNum += 1
        lastTime = time.time()  # reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy("\n".join(ourText))
    print('\nDone.')