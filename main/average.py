print("This here will calculate your average trip time \n"
      "and your average trip speed")

# feed me some info please :)

trip_distance = int(input("enter trip distance>>"))

while True:

    start_hour = int(input("enter starting hour>>"))

    if start_hour > 23:
        print("please input hour between 0 and 23")
        start_hour = int(input("enter starting hour>>"))
    else:
        pass

    start_minutes = int(input("enter starting minutes>>"))

    if start_minutes > 59:
        print("please input minutes between 0 and 59")
        start_minutes = int(input("enter starting minutes>>"))
    else:
        pass


    stop_hour = int(input("enter ending hour>>"))

    if stop_hour > 23:
        print("please input hour between 0 and 23")
        stop_hour = int(input("enter ending hour>>"))
    else:
        pass

    stop_minutes = int(input("enter ending minutes>>"))

    if stop_minutes <= 59:
        break
    elif stop_minutes > 59:
        print("please input minutes between 0 and 59")
        stop_minutes = int(input("enter ending minutes>>"))




# calculate time in hours
diff_h = stop_hour - start_hour
diff_m = stop_minutes - start_minutes

time_in_minutes = 60 * diff_h + diff_m
time_in_hours = time_in_minutes / 60


# calculate average speed in km/h
avg_speed = trip_distance / time_in_hours

# print time and speed
print("You spend", round(time_in_hours, 2), "hours for the trip")
print("Your avg speed was", round(avg_speed, 2), "km/h")

# it's not perfect, yet, maybe.. in future
