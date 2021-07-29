import time
import subprocess as s


while True:
    s.call(['notify-send', 'Water Reminder', 'Drink some water perhaps?'])
    time.sleep(60*60)
