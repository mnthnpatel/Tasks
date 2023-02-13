userlist = []
def userpage():
     print("user page accessed")
     opt = int(input("Enter '0' to log out"))
     if opt == 0:
          mainpage()

def signin():
     username = input("Please enter username: ")
     for user in userlist:
          if username in user:
               password = input("Please enter password: ")
               if password in user:
                    userpage()
               else:
                    print("Incorrect password")
                    mainpage()
          else:
               print("Unregister username")
               mainpage()

def signup():
     username = input("Please enter username: ")
     password = input("Please enter password: ")
     userlist.append([username,password])
     print(userlist)
     userpage()

def mainpage():
     opt = int(input("Enter '0' to sign up, '1' to sign in: "))
     if opt == 0:
          signup()
     elif opt == 1:
          signin()
mainpage()