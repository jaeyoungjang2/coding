import datetime
import math


def calculateFee(timeDuration, fees):
    baseTime = fees[0]
    baseRate = fees[1]
    additionalTime = fees[2]
    additionalRate = fees[3]

    hour = str(timeDuration).split(":")[0]
    minute = str(timeDuration).split(":")[1]
    duration = int(hour) * 60 + int(minute)

    if duration < int(baseTime):
        return baseRate
    else:
        return baseRate + (math.ceil(((duration - baseTime) / additionalTime)) * additionalRate)


time_1 = datetime.timedelta(hours=10, minutes=22)
time_2 = datetime.timedelta(hours=20, minutes=30)


recordInfo = {}
feeInfo = {}
timeInfo = {}

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


for record in records:
    lst = record.split()
    time = lst[0]
    car = lst[1]
    type = lst[2]

    if type == "IN":
        recordInfo[car] = time
    if type == "OUT":
        targetInTime = recordInfo[car].split(":")
        targetOutTime = time.split(":")
        timeIn = datetime.timedelta(
            hours=int(targetInTime[0]), minutes=int(targetInTime[1]))
        timeOut = datetime.timedelta(
            hours=int(targetOutTime[0]), minutes=int(targetOutTime[1]))
        timeDuration = timeOut - timeIn

        try:
            timeInfo[car] += timeDuration
        except:
            timeInfo[car] = timeDuration
        del recordInfo[car]

for car in recordInfo:
    targetInTime = recordInfo[car].split(":")
    timeIn = datetime.timedelta(
        hours=int(targetInTime[0]), minutes=int(targetInTime[1]))
    timeOut = datetime.timedelta(hours=23, minutes=59)
    timeDuration = timeOut - timeIn

    try:
        timeInfo[car] += timeDuration
    except:
        timeInfo[car] = timeDuration


for car in timeInfo:
    # targetInTime = recordInfo[car].split(":")
    # timeIn = datetime.timedelta(
    #     hours=int(targetInTime[0]), minutes=int(targetInTime[1]))
    # timeOut = datetime.timedelta(hours=23, minutes=59)
    # timeDuration = timeOut - timeIn
    timeDuration = timeInfo[car]

    carsFee = calculateFee(timeDuration, fees)
    try:
        feeInfo[car] += int(carsFee)
    except:
        feeInfo[car] = int(carsFee)
print(recordInfo)
print(feeInfo)

cars = list(feeInfo.keys())
cars.sort()
answer = []
for car in cars:
    answer.append(feeInfo[car])
print(answer)
