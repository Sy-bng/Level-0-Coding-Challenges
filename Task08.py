number = int(71)
def time_converter () :
    hour = number / 60/60
    minutes = number /60 % 60
    return hour, minutes
time = time_converter()
print(time)

