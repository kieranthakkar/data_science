import statistics

print("Please input 3 numbers")

num1 = float(input("No. 1: "))
num2 = float(input("No. 2: "))
num3 = float(input("No. 3: "))

print("/nAverage:",statistics.mean([num1,num2,num3]))