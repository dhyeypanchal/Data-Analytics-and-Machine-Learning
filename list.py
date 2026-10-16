li = [1,2.5,3,4,5]
print("List of hours studied:", li)
print(f"Total hours studied from the list: {sum(li)} hours.")
print(f'list at index 2 is: {li[2]}')

study_hours = [2, 1.5, 3, 2.5]

print(study_hours[0])   # 2
print(study_hours[-1])  # 2.5
print(len(study_hours)) # 4
print(sum(study_hours)) # 9.0

# list is ordered and mutable.


# Slicing extracts part of a list using list[start:stop:step]. The stop index is excluded.

print(study_hours[1:3])  # [1.5, 3]
print(study_hours[:2])   # [2, 1.5]
print(study_hours[2:-1:1])   # [3, 2.5] (here -1 means the last element)
print(study_hours[2:4:1])   # [3, 2.5] (same as above)

values = [10, 20, 30, 40, 50]

print(values[1:4])  # [20, 30, 40]
print(values[:3])   # [10, 20, 30]
print(values[2:])   # [30, 40, 50]
print(values[::-1]) # [50, 40, 30, 20, 10]