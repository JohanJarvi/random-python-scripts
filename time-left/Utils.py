from pathlib import Path


def readFile():
    path = Path(__file__).parent
    file = open(str(path) + "/hours.txt", "r")
    return file.read()


def convertDecimalHourRepresentationToMinutes(decimalHourRepresentation):
    split = decimalHourRepresentation.split('.')
    hoursPortion = split[0]
    minutesPortion = split[1]
    return int(hoursPortion) * 60 + int(minutesPortion)


def convertMinutesIntoHoursMinutesRepresentation(minutes):
    floatTime = minutes / 60
    split = str(floatTime).split('.')
    hours = split[0]
    minutesInFloat = split[1][:2]  # "two decimal places"
    minutes = (int(minutesInFloat) / 100) * 60
    return str(hours) + 'h ' + str(int(minutes)) + 'm'
