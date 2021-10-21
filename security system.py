import random
x=int(input("enter your username as a phone number\n"))
y=(input("enter your passward\n"))
if x != 77:
    print("check your username\n","username is incorrect")
elif y != "Pass@123":
    print("passward is incorrect")
else:
    otp=random.randint(1000,9999)
    print(otp)
    for a in range(0,4):
        a=int(input("enter your OTP\n"))
        if a != otp:
            print("try again your OTP is incorrect\n")
            print("please check you number and retry")
        else:
            print("you are good to go\n  welcome")
            break