class chatbook:
    __user_id = 1

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val


    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
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
            self.my_post()

        elif uinput == "2":
            self.send_mesg()

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
    
    def my_post(self):
        txt = input("Enter your message here --> ")
        print(f"following content has been posted -> {txt}")

        print('\n')
        self.post()

    def send_mesg(self):
        txt = input("Enter your message here --> ")
        frd = input("enter your friend name --> ")
        print(f"messege sent succesfully to -> {frd}")
        print('\n')
        self.post()

