"""
Create a Python file named lab_3-5.py

Import the time and math modules.

Calculate 22 using math.pow and again using the ** operator.

Record the time using time.process_time before and after each calculation (Hint: you may need to store the result of time.process_time in a variable)

Add a statement that prints the elapsed time after each statement is processed. Run the program. What do you notice? Write it as a comment.

Change each statement that records the time to use time.perf_counter instead of time.process_time.

Run the program again. What do you notice? Write it as a comment.
"""
import time
import math

x = time.perf_counter()
math.pow(2,2)
print(x)

2 ** 2
print(x)

# The time is the same after running both statements.
# with perf_counter the time output is in fractional seconds
