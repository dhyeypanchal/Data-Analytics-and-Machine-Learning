def calculate_average(values):
    return sum(values) / len(values)

hours = [2, 1.5, 3, 2.5]

average = calculate_average(hours)
print(average)  # 2.25


# define arguments so that we can pass any number of arguments to the function. *any_name is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of positional arguments to the function, which are then accessible as a tuple within the function.
def calculate_average(*args):
    return sum(args) / len(args)

print(calculate_average(2, 1.5, 3, 2.5))  # 2.25


def greet(name: str, greeting: str = "Hello") -> str: # also this is how we apply type hints to the function arguments and return type. It is not enforced at runtime, but it can help with code readability and can be used by static type checkers.
    return f"{greeting}, {name}!"
    # The function `greet` is defined with type hints, indicating that the `name` parameter should be of type `str` and the `greeting` parameter should also be of type `str`. However, Python's type hints are not enforced at runtime; they are primarily for documentation and static analysis purposes.

print(greet("Dhyey"))
print(greet("Dhyey", "Hi"))
print(greet(5, "Welcome"))

# why it is working with 5 then

# lamda function: it is a small anonymous function that can take any number of arguments, but can only have one expression. It is often used for short, simple functions that are not reused elsewhere in the code. The syntax for a lambda function is: `lambda arguments: expression`. The expression is evaluated and returned when the lambda function is called.
square = lambda x: x ** 2
print(square(5))  # 25

students = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 92},
]

# below syntax is used to sort the list of dictionaries based on the "score" key in descending order. The `sorted` function takes the list of students and a key function that extracts the "score" value from each student dictionary. The `reverse=True` argument specifies that the sorting should be done in descending order.
students_sorted = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True,
)

print(students_sorted)  # [{'name': 'B', 'score': 92}, {'name': 'A', 'score': 85}]