from datetime import datetime
from time import sleep

date = datetime.today()

print("one")

pausecount = 0
while pausecount < 5:
    print(pausecount)
    pausecount += 1
    sleep(1)

print(date)