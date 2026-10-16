study_hours = {
    "Monday": 2.0,
    "Tuesday": 1.5,
    "Wednesday": 3.0,
    "Thursday": 2.5,
    "Friday": 0.0,
}

def summarize_hours(hours_by_day: dict[str, float]) -> None:
    values = list(hours_by_day.values())
    # print(hours_by_day.values())

    if not values:
        print("No study data available.")
        return

    total = sum(values)
    average = total / len(values)
    # below list comprehension is used to create a list of days where the study hours are greater than or equal to 2. It iterates over the items in the `hours_by_day` dictionary, checking each day's hours and including the day in the new list if the condition is met.

    # explain all 3 inside the list
    # 1. `day`: This is the variable that will hold the key (day of the week) from each item in the dictionary.
    # 2. `hours`: This is the variable that will hold the value (study hours) from each item in the dictionary.
    # 3. `if hours >= 2`: This is the condition that filters the items. Only items where the study hours are greater than or equal to 2 will be included in the new list.
    print('Monday' in hours_by_day.items())
    # Monday shows false because we are checking if the string 'Monday' is in the items of the dictionary, but the items are key-value pairs.
    print('Monday' in hours_by_day, 2.0 in hours_by_day.values())
    productive_days = [
        day for (day, hours) in hours_by_day.items() #we don't need to put () in day,hours. i just put it for understanding purpose. we can also write it as day,hours in hours_by_day.items()
        if hours >= 2
    ]


    print(f"Total: {total:.1f} hours")
    print(f"Daily average: {average:.2f} hours")
    # we can also write above using traditional for loop
    # Keep only days with at least 2 study hours
    for day, hours in hours_by_day.items():
        if hours >= 2:
            print("using traditional for loop",day)
    print(f"Days with at least 2 hours: {productive_days}")

summarize_hours(study_hours)