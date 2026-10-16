import math
from statistics import mean
from newModule import calculate_average

print(math.sqrt(16))  # 4.0
a = [1, 2, 3, 4, 5]
print(sum(a))  # 15
print(mean(a))  # 3.0

# this is our custom module which we created in newModule.py file. we can also import it using from newModule import * but it is not recommended because it can lead to namespace pollution and make the code less readable. It is better to import only the specific functions or classes that you need.
print(calculate_average(2, 1.5, 3, 2.5))  # 2.25
