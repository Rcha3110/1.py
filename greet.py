import time

# Get the current time in hours
currTime = int(time.strftime('%H'))

# Determine the appropriate greeting based on the current time
if 6 <= currTime < 12:
    print("Good morning ma'am")
elif 12 <= currTime < 18:
    if currTime == 12:
        print("Good noon!")
    else:
        print("Buenas tardes!")  # Note: "Buenos tardes" should be "Buenas tardes" in Spanish
elif 18 <= currTime < 21:
    print("Good evening ma'am")
else:
    print("Buenas noches!")

