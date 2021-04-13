import Utils

hoursStr = Utils.readFile()

time_worked = 0
thirtyEightHoursInMinutes = 38 * 60

if (hoursStr):
    hours = hoursStr.split(',')
    for hour in hours:
        time_worked += Utils.convertDecimalHourRepresentationToMinutes(hour)
        if time_worked > thirtyEightHoursInMinutes:
            print('STOP RIGHT THIS INSTANT! You have already worked enough! Party time!')
else:
    print('How many days have you worked this week: ')
    days_worked = int(input())

    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(0, days_worked):
        print('Enter time worked on ' +
              days_of_week[i] + " (in format of 'h.mm' e.g. '7:40' representing 7 hours 40 minutes): ")
        time_worked += Utils.convertDecimalHourRepresentationToMinutes(input())
        if time_worked > thirtyEightHoursInMinutes:
            print('STOP RIGHT THIS INSTANT! You have already worked enough! Party time!')


print("")
print('You have worked ' +
      Utils.convertMinutesIntoHoursMinutesRepresentation(time_worked) + ' this week.')
print("")

time_left = thirtyEightHoursInMinutes - time_worked
if time_left < 0:
    print('You have worked ' + Utils.convertMinutesIntoHoursMinutesRepresentation(
        abs(time_left)) + ' too much this week!')
else:
    print('You have ' + Utils.convertMinutesIntoHoursMinutesRepresentation(time_left) +
          ' left to work this week.')

print("")
