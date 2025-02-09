print('Welcome to Treasure Island\nYour mission os to find the treasure.')
first_option = input('left or right?')
if first_option == 'right':
    print('Game Over')
else:
    second_option = input('swim or wait?')
    if second_option == 'swim':
        print('Game Over')

    else:
        third_choice = input('Red, Yellow or Blue')
        if third_choice == 'Red' or 'Blue':
            print('Game over')
        elif third_choice == 'Yellow':
            print('You Win')
        else:
            print('Game Over')