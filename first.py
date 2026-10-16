# print("Hello, Python!")
# print("I am learning machine learning.")
# print(10 + 5)


# course = "Data Analytics"
# study_hours = 9
# progress = 0.25

# print("I study {study_hours} hours per week.")
# print(f"My course is {course}.")
# print(f"My progress is {progress * 100}%.")


# weekday_hours = 1.5
# weekend_hours = 2

# total_hours = weekday_hours * 5 + weekend_hours * 2
# average_hours = total_hours / 7

# print(f"Total weekly hours: {total_hours}")
# print(f"Daily average: {average_hours:.2f}") # .2f means show 2 digits after the decimal point


# hours = input("Enter the number of hours you study per day: ")
# print(f"You study {hours} hours per day. and type of hours is {type(hours)}")


# # types shows number of hours is string, so we need to convert it into float or int to perform arithmetic operations
# hours = float(input("How many hours did you study? "))
# print(f"Next week, you could study {hours + 1} hours. type is {type(hours + 1)}")


mon = 2
tue=1.5
wed=3
thu=2.5

print("monday hours:", mon, "tuesday hours:", tue, "wednesday hours:", wed, "thursday hours:", thu)

sum = mon + tue + wed + thu
print(f"Total hours studied from Monday to Thursday: {sum} hours.")
avg = sum / 4
print(f"Average hours studied per day from Monday to Thursday: {avg:.2f} hours.")