import math

def make_readable(seconds):
    minutes = 0
    hours = 0

    if seconds > 59:
        minutes = math.floor(seconds / 60)
    else:
        minutes = 0

    if minutes > 59:
        hours = math.floor(minutes / 60)
    else:
        hours = 0

    seconds %= 60
    minutes %= 60

    seconds = "%02d"%seconds
    minutes = "%02d"%minutes
    hours = "%02d"%hours

    return (f"{hours}:{minutes}:{seconds}")

print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
