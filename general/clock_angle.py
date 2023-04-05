import datetime

def clock_angel():
    time = datetime.datetime.now()
    hour, minute = int(time.hour), int(time.minute)
    if hour > 12:
        hour -= 12
    clock_angel = abs(hour*30 + minute*0.5 - minute*6)
    return min(clock_angel, 360 - clock_angel)


print(clock_angel())