from datetime import date
import Utils

weekdayInteger = date.today().weekday()

hours = Utils.readFile().split(',')
try:
    hoursToday = hours[weekdayInteger]
except:
    hoursToday = input(
        "How many hours have you worked today? (In the format of H.mm): ")

minutesToday = Utils.convertDecimalHourRepresentationToMinutes(hoursToday)
workingDayInMinutes = 7.6 * 60
leftToday = workingDayInMinutes - minutesToday
print("")
print("You have " + Utils.convertMinutesIntoHoursMinutesRepresentation(leftToday) +
      " left to work today")
print("")
