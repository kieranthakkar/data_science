import csv
# Read text from .csv file
def view():
    with open("students.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            print("Username:", line[0], "\tPassword:", line[1])

#view()


# Writing to .csv file
def add():
    pwd = input("Password: ")
    with open("students.csv", "a") as csv_file:
        char_writer = csv.writer(csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        char_writer.writerow(["Mango", "Papaya"])

add()