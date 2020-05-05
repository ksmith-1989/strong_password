import re
import time

print("Time for a new password.")

# funtcion for entering strong password.


def pw():
    print("Password Requirements:\nMust have 8-14 characters.\nMust have one lowercase and one uppercase character\nMust contain one numerical character.\nMust contain one special character(e.g: .!  # %^&)")
    password = input("Please Enter a New Password:")
    if re.match(r'(?=.{8,14}$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\?@?.!#%^&]).*$', password) is None:
        print("Password does not meet requirment.")
        time.sleep(1)
        pw()
    else:
        print("Strong password")


# run function
pw()
