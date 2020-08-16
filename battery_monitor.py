import os
import sys
from tkinter import *

# Settings
BATTERY_PATH = '/sys/class/power_supply/BAT0/capacity'
DISPLAY = ':0'
EXIT_AFTER = 5000 # time in ms
TL = (-50, 25) # window top-left corner coordinates
LEVEL_WARN = 40 # below what % of power to display warning message

def popup(s):
    root = Tk()
    root.attributes('-type', 'splash') # hide bar/decorations
    root.after(EXIT_AFTER, sys.exit)

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    button = Button(root, text = s, font = ("Verdana", 15), bg = "yellow", command = sys.exit)
    button.pack()
    root.geometry('{}+{}'.format(*TL))
    root.mainloop()

def main():
    os.environ['DISPLAY'] = DISPLAY
    os.environ['XAUTHORITY'] = '{}/.Xauthority'.format(os.environ['HOME'])

    with open(BATTERY_PATH) as fh:
        battery_value = fh.read().strip()

    if int(battery_value) <= LEVEL_WARN:
        msg = '{}% remaining.'.format(battery_value)
        popup(msg)

if __name__ == "__main__":
    main()
