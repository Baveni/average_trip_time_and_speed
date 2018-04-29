print("This here will calculate your average trip time \n"
      "and your average trip speed")

# feed me some info please :)

trip_distance = int(input("enter trip distance>>"))
start_hour = int(input("enter starting hour>>"))
start_minutes = int(input("enter starting minutes>>"))
stop_hour = int(input("enter ending hour>>"))
stop_minutes = int(input("enter ending minutes>>"))


# calculate time in hours
diff_h = stop_hour - start_hour
diff_m = stop_minutes - start_minutes

time_in_minutes = 60 * diff_h + diff_m
time_in_hours = time_in_minutes / 60


# calculate average speed in km/h
avg_speed = trip_distance / time_in_hours

# print time and speed
print("You spend ", time_in_hours, " hours for the trip")
print("Youre avg speed was ", avg_speed, "km/h")
