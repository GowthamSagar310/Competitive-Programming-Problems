for _ in range(int(input())):
    hours, minutes = map(int, input().split(":"))


    # if hours == 00 or hours >= 12 - convert - PM
    # minutes stays the same 
    # else hours remains same and AM
    zone = "AM"
    if hours == 0:
        hours = 12
        zone = "AM"
    elif hours == 12:
        hours = 12
        zone = "PM"
    elif hours > 12:
        hours = hours-12
        zone = "PM"
    
    # format 
    ms = "0" + str(minutes) if minutes < 10 else str(minutes)
    hs = "0" + str(hours) if hours < 10 else str(hours)

    print(hs + ":" + ms + " " + zone)
