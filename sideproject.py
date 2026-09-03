print('''This story starts on a grass meadow, with wildflowers and grasses sprouting as far 
as the eyes can see. But that is irrelevant because the ground caves in and you find 
yourself in a cave. A cold one with water a few centimetres deep. A tree falls over and 
blocks the way you got in the cave. You must get out. Otherwise aldi will close. You need 
toilet paper though. Must. Get. Out.''')
answer1 = int(input('''You see a tunnel ahead. To start things off, what do you do? 
type 1 to drop your wallet. 2 to walk on. 3 to give up.'''))
if answer1 == 1:
    print('you lose. You needed that for when you got back to aldi.')
elif answer1 == 2:
    print('''the tunnel wasn't too long, and it led to aldi. You win.''' )
    while True:
        print("YOU WIN", end='')
elif answer1 == 3:
    print('''Eh fair enough. Yer still lose though. Naughty taughty''')
else:
    print('''if you're not gonna try nor will I. You lose.''')
