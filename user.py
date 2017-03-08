import getpass


class User:

    curr_users = []

    def __init__(self):
        self.user_name = self.set_username()
        self.password = self.get_password()
        self.first_name = self.get_fname()
        self.last_name = self.get_lname()
        self.email = self.get_email()
        self.full_name = "{} {}".format(self.first_name, self.last_name)

    def set_username(self, user_name=None):
        valid = False
        while not valid:
            if user_name and user_name not in User.curr_users:
                valid = True
                User.curr_users.append(user_name)
                return user_name
            else:
                print("\nUsername must be unique")
                user_name = input("Enter username: ")

    def get_password(self):
        valid = False
        while not valid:
            password = getpass.getpass(prompt='Password: ', stream=None)
            if len(password) > 8:
                valid = True
                return password
            else:
                print("\nMust be longer than 8 characters")

    def get_fname(self):
        first_name = input("First name: ")
        return first_name

    def get_lname(self):
        last_name = input("Last name: ")
        return last_name

    def get_email(self):
        valid = False
        while not valid:
            email = input("Email: ")
            if '@' in email and '.' in email:
                valid = True
                return email
            else:
                print("\nPlease enter a valid email")
