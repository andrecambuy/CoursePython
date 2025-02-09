print('Welcome to the tip calculator')
total = float(input('What was the total bill?'))
tip = int(input('How much would you like to give? 10, 12, 15?'))
people_split = float(input('How many people to split the bill?'))

total_per_person = round((total +(total * (tip/100))) / people_split, 2)
print(f'Each person should pay: ${total_per_person}')