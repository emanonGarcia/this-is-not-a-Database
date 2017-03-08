from user import User
import csv
import getpass


fieldnames = ['user_name', 'password', 'name', 'email']
curr_users = {}


def add_new_user(first_entry=None):
    first_entry = first_entry
    new_user = User()
    save_data(new_user.user_name.lower(), new_user.password, new_user.full_name, new_user.email, first_entry)
    curr_users[new_user.user_name.lower()] = new_user.password
    print("Saving new user data for '{}'...".format(new_user.user_name))
    thing()


def load_data():
    try:
        with open('user_info.csv', 'r') as f:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            next(reader, None)
            for row in reader:
                if row['user_name'] not in curr_users:
                    curr_users.setdefault(row['user_name'], row['password'])
                else:
                    continue
    except:
        print("No users in database. Please create the first account")
        add_new_user(True)


def save_data(u_name, p_word, name, e_mail, first_user=None):
    with open('user_info.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if first_user:
            writer.writeheader()
        writer.writerow({'user_name': u_name, 'password': p_word, 'name': name, 'email': e_mail})


def thing():
    user_input = input('\n[N]ew user or [Q]uit: ')
    if len(user_input) > 0 and (user_input.lower() == 'q' or user_input[0].lower() == 'q'):
        exit()
    elif user_input.lower() == 'n' or user_input[0].lower() == 'n':
        add_new_user()


def main():
    count = 0

    print("** Login **")
    load_data()
    while count < 3:
        user_input_name = input("Username: ")
        user_info_pword = getpass.getpass(prompt='Password: ', stream=None)
        if user_input_name.lower() in curr_users and user_info_pword == curr_users[user_input_name.lower()]:
            thing()
            break
        else:
            count += 1
            print("\nNo Match Found")
        print('\n...Please try again later')


if __name__ == '__main__':
    main()
