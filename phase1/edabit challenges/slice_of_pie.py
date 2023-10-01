"""
Create a function that determines if it's possible to split a pie fairly given these three parameters:
    1. Total number of slices.
    2. Number of recipients.
    3. How many slices each person gets.

The function will be in this form:
    equal_slices(total slices, no. recipients, slices each)
"""

def equal_slices(total, num_recipients, slices_each):
    return (num_recipients * slices_each) <= total
