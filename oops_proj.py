class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    
    def menu(self):
        user_input = input("""Welcomre to the chatbook!! How would you like to proceed?
                            1. Press 1 to signup
                            2. press 2 to signin 
                            3. press anyother key to exit
                            ENTER THE NUMBER => """)
        if user_input == "1":
            self.signup()

        elif user_input == "2":
            self.signin()

        else:
            exit()

    def post(self):
        uinput = input("""Welcome to Chatbook
                       
                       1. Press 1 to write a post
                       2. Press 2 to message a friend
                        """)
        if uinput == "1":
            pass

        elif uinput == "2":
            pass

        else:
            exit

    def signup(self):
        email = input('Enter your email here => ')
        password = input('Setup your neww password => ')
        self.username = email
        self.password = password
        print("You Signedup Succesfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print('Please signup first by pressing 1')
            self.menu()
        else:
            email1 = input("Enter your registered email => ")
            passw = input("Enter your password => ")

            if self.username == email1 and self.password == passw:
                print("You logged in succesfully")
                self.loggedin = True
                print("\n")
                self.post()
            else:
                print("Enter Correct email and password")
        print("\n")        
        self.menu()

obj = chatbook()