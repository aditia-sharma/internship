from notify_run import Notify
import random

Notif = Notify()

OTP = random.randint(000000, 999999)
print("A verification OTP has been sent to your phone")
notification = ("Your OTP is: " + str(OTP))
Notif.send(notification)
Entry = int(input("Enter OTP to access this file: "))
if Entry == OTP:

    print("Correct OTP")

else:
    print("Wrong OTP")