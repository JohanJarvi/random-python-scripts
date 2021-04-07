from pathlib import Path

def convertDecimalHourRepresentationToMinutes(decimalHourRepresentation):
    split = decimalHourRepresentation.split('.')
    hoursPortion = split[0]
    minutesPortion = split[1]
    return int(hoursPortion) * 60 + int(minutesPortion)

def convertMinutesIntoHoursMinutesRepresentation(minutes):
    floatTime = minutes / 60
    split = str(floatTime).split('.')
    hours = split[0]
    minutesInFloat = split[1][:2] # "two decimal places"
    minutes = (int(minutesInFloat) / 100) * 60
    return str(hours) + 'h ' + str(int(minutes)) + 'm'

def readFile():
    path = Path(__file__).parent
    # hours.txt should be a file of hour strings such as "7.32" or "7.56" representing 7 hours and 32 minutes
    # or 7 hours and 56 minutes respectively. 
    file = open(str(path) + "/hours.txt", "r")
    return file.read()

hoursStr = readFile()

time_worked = 0
thirtyEightHoursInMinutes = 38 * 60

if (hoursStr):
    hours = hoursStr.split(',')
    for hour in hours:
        time_worked += convertDecimalHourRepresentationToMinutes(hour)
        if time_worked > thirtyEightHoursInMinutes:
            print('STOP RIGHT THIS INSTANT! You have already worked enough! Party time!')
else:
    print('How many days have you worked this week: ')
    days_worked = int(input())

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(0, days_worked):
        print('Enter time worked on ' + days_of_week[i] + " (in format of 'h.mm' e.g. '7:40' representing 7 hours 40 minutes): ")
        time_worked += convertDecimalHourRepresentationToMinutes(input())
        if time_worked > thirtyEightHoursInMinutes:
            print('STOP RIGHT THIS INSTANT! You have already worked enough! Party time!')


print("")
print ('You have worked ' + convertMinutesIntoHoursMinutesRepresentation(time_worked) + ' this week.')
print ("")

time_left = thirtyEightHoursInMinutes - time_worked
if time_left < 0:
    print ('You have worked ' + convertMinutesIntoHoursMinutesRepresentation(abs(time_left)) + ' too much this week!')
else:
    print ('You have ' + convertMinutesIntoHoursMinutesRepresentation(time_left) + ' left to work this week.')

print("")


