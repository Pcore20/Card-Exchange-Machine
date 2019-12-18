print('press 1 = 50')
print('press 2 = 100')
print('press 3 = 200')
a = 0
while (a > -1):
    a = int(input('Please choose the amount that you want to top up :'))
    if(a == 1):
        print('You top up 50 bath')
        b = 50
        break
    elif(a == 2):
        print('You top up 100 bath')
        b = 100
        break
    elif(a == 3):
        print('You top up 200 bath')
        b = 200
        break
    else:
        print('Wrong enter the new')
while (b > 0):
    print('Please top up another', b, 'bath')
    c = int(input('Please put money  '))
    b = b-c
    if(b == 0):
        print('Enter the fully Plase wait for card...')
