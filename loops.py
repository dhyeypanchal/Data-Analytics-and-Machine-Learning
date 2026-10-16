study_hours = [2, 1.5, 3, 2.5]

# for loop

for hours in study_hours:
    print(hours)

for i in range(5):
    print(i)

days = ["Monday", "Tuesday", "Wednesday"]

for index, day in enumerate(days, start=1): # start is optional, default is 0.
    print(index, day)


# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Other useful control-flow keywords:
# - break exits the nearest loop.
# - continue skips to the next iteration.
# - pass is a placeholder that does nothing.
count = 0
# pass working
while count < 5:
    count += 1
    pass  # This loop will run indefinitely, but the pass statement does nothing, so it won't cause an error.   
    print("using pass",count)

    # so what is the purpose of pass? The pass statement is used as a placeholder in situations where a statement is syntactically required but you don't want to execute any code. It allows you to create empty blocks of code, such as in loops, functions, or classes, without causing a syntax error. This can be useful during development when you want to outline the structure of your code without implementing the functionality yet.


# new_list = [expression for item in iterable]
hours = [2, 1.5, 3, 2.5]
minutes = [h * 60 for h in hours] #this is loop comprehension, it is a concise way to create a new list by applying an expression to each item in an existing iterable (like a list). In this case, it multiplies each hour value by 60 to convert it to minutes.
print(minutes)  # [120.0, 90.0, 180.0, 150.0]

total_minutes = sum(h * 60 for h in hours)
print(total_minutes)  # 540.0

