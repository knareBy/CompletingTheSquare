import time
import math
def answerer():
    answer = str(input('\nWould you like to solve another equation?(yes/no)'))
    if answer == 'yes':
        square()
    elif answer == 'no':
        print('OK, goodbye.')
        time.sleep(1.5)
    else :
        answerer()

def square():
    a = float(input('\nWhat is the co-efficient of x\xb2 in your equation?'))
    b = float(input('\nWhat is the co-efficient of x in your equation?'))
    c = float(input('\nWhat is the constant in your equation?'))
    print("\nThis is your equation: ",a,"x\xb2 + " ,b,"x + " ,c, sep='')

    d = b/(2*a)
    g = (-(d**2))*a
    e = g+c

    if d>=0 and e>=0:
        print('\nThis is your completed square: ',a,'(x + ',d,')\xb2 + ',e, sep='')
    elif d>=0 and e<0:
        print('\nThis is your completed square: ',a,'(x + ',d,')\xb2 ',e, sep='')
    elif d<0 and e<0:
        print('\nThis is your completed square: ',a,'(x ',d,')\xb2 ',e, sep='')
    elif d<0 and e>=0:
        print('\nThis is your completed square: ',a,'(x ',d,')\xb2 + ',e, sep='')

    f = -e/a
    g = math.sqrt(f)
    plus = -d+g
    minus = -d-g
    print('\nYour two roots are:',plus,'and',minus)
    answerer()


square()

