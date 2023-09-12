"""
The 50-30-20 strategy is a simple way to budget, which involves spending 50% of after-tax income on needs, 30% after tax income on wants, and 20% after-tax income on savings or paying off debt.

Given the after-tax income as ati, make a function that will return a dictionary that shows how much a person needs to spend on needs, wants, and savings.
"""
def fifty_thirty_twenty(ati):
    d = dict()
    d["Needs"] = 0.5*ati
    d["Wants"] = 0.3*ati
    d["Savings"] = 0.2*ati
    return d

print(fifty_thirty_twenty(10000))