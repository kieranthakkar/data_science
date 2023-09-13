def save_to_file(first_name, surname, age):
    with open('notme.txt', 'w') as f:
        line = ','.join([first_name, surname,age])
        data = line.split(",")
        print(data)
        f.write(line + '\n')
        f.close

first_name = input('Please enter your first name: ')
surname = input('Please enter your surname: ')
age = input('How old are you? ')

save_to_file(first_name, surname, age)