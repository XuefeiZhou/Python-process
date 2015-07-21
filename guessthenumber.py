#from MIT CS lecture,week 2
print("Please think of a number between 0 and 100!")
answer = 'h'
low = 0
high = 100
while answer != 'c':
    ans = (low + high) / 2
    print ('Is your secret number %s?' % ans)
    answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'h':
        high = ans
    elif answer == 'l':
        low = ans
    elif answer == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: %s' % ans) 
