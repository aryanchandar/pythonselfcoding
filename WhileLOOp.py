"""
i=1
while i<=5:
  print(i)
  i=i+1
print("Done")

"""



'''
i=1
while i<=5:
  print('*'*i)
  i=i+1
print("Done")
'''











"""
#Guessing game
guess:1
guess:2
guess:3
this is a guessing game in this game we got only 3 chance to guess the no if we guess correctly then it we pass or it will give this result:Sorry you failed!
below is the solution
"""
"""
secret_no=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess:'))
    guess_count+=1
    if guess==secret_no:
        print('you won')
        break
else:
    print('you failed!')   

"""






'''
#Car Game
from typing import ClassVar


>help 
start - to start the car
stop - to stop the car
quit - to exit

>asd
I don't understand that...
>start
Car started...Ready to go!
>stop
Car stopped.
>quit
end program'''
#solution

command=""
started=False
stopped=False
while True:

    command=input("> ").lower()
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
            print("Car started....")

    elif command=="stop":
        if stopped:
           print("car is already stopped")
        else:
            stopped=True  
            print("Car stopped")    
    elif command=="help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif command=="quit":
        break
else:
    print("Sorry, i don't understand that")