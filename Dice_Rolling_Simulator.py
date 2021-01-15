import random
print('This is dice rolling program')
print()
min = int(input('Enter start num: '))
max = int(input('Enter end num: '))

roll_again = 'yes'

while roll_again == 'yes':
    print('....Dice is rolling.....')
    print('........................')
    print('........................')
    
    p = random.randint(min,max)
    s = '.......... {} ...........'
    print(s.format(p))
    print('........................')
    print('........................')

    roll_again = input('Do you want to roll dice again? ')
    
    
