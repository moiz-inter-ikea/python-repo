x=-1
if x > 0:
    print ("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
print("finish")


######################################################

guess_day = input("guess day of week ")
today = "friday"

if(guess_day.lower() == today):
    print("you won")
else:
    print("you lost")


###########################################
l = [1,2,3,4,5,6,7]
guess_no = input("guess no. from list ")
if int(guess_no) in l:
    print("your guess is correct!!")
else:
    print("try again")