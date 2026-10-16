# tuples, sets and dictionaries are all collections in python.

coordinates = (43.01, -81.27) # This is a tuple, which is an immutable collection of items. so you cannot change the values of a tuple once it is created.

# set

courses = {"Python", "ML", "Python"}
print(courses)  # {'Python', 'ML'}; display order may vary (it is unordered and does not allow duplicates,(unique elements and no positional indexing what does it mean? It means that in a set, the elements are not stored in any particular order, and you cannot access them using an index like you would with a list or tuple. Additionally, sets do not allow duplicate values, so if you try to add the same element multiple times, it will only appear once in the set.))

# for sets important operations are union, intersection, difference, and symmetric difference.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))  # {1, 2, 3, 4, 5, 6}
print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a & b)  # {3, 4}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}
print(a ^ b)  # {1, 2, 5, 6}

# dictionary (key-value pairs)
student = {"name": "Alice", "age": 20, "grade": "A"}

student["new key"] = "new value"  # adding a new key-value pair to the dictionary
student["age"] = 21  # updating the value of an existing key in the dictionary
print(student)  # {'name': 'Alice', 'age': 21, 'grade': 'A'}

# comprehension (it is short way to create a new collection from an existing one using some expression or condition)
hours = [2, 1.5, 3, 2.5]
minutes = [h * 60 for h in hours] #this is loop comprehension, it is a concise way to create a new list by applying an expression to each item in an existing iterable (like a list). In this case, it multiplies each hour value by 60 to convert it to minutes.
print(minutes)  # [120.0, 90.0, 180.0, 150.0]
