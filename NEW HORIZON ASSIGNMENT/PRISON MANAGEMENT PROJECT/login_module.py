import os
import random


# ======================================================================================================================================================================================

# generate an admin key if a new admin is registered
def random_admin_id():
    name = "AD"
    number_list = []
    k = 1
    while k <= 6:
        number = random.randint(0, 9)
        number_list.append(number)
        k += 1
    s = [str(i) for i in number_list]
    res = (''.join(s))
    val = name + res
    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYour admin key is", val)
    return val


# generate a user key if a new user is registered
def random_user_id():
    name = "US"
    number_list = []
    k = 1
    while k <= 6:
        number = random.randint(0, 9)
        number_list.append(number)
        k += 1
    s = [str(i) for i in number_list]
    res = (''.join(s))
    val = name + res
    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYour user key is", val)
    return val
# ======================================================================================================================================================================================


# ======================================================================================================================================================================================


# check if username login exists or not and create a new user if username does not exist
def new_admin_reg():
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ----------------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t\t\t\t\tNEW ACCOUNT\t\t\t\t   |\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ----------------------------------------------")
    username = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Username: ").upper()
    password = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Password: ").lower()
    # save each new login as a dictionary key and value pair
    if os.path.isfile("username_password.txt") is False:
        print("\n---Can't write to username_password.txt, file not found---")
    else:
        file_handle = open("username_password.txt", "r")
        for i in file_handle:
            if i.startswith(username):
                print("---Username already in use, try another username---")
                return new_admin_reg
            else:
                handle = open("username_password.txt", "a")
                if len(password) > 8:
                    print("Password too long, your password must not be more than 8 characters long")
                    return new_admin_reg
                else:
                    admin_id = random_admin_id()
                    handle.write("\n")
                    handle.write(username)
                    handle.write("\t\t\t\t\t\t")
                    handle.write(password)
                    handle.write("\t\t\t\t\t\t")
                    handle.write(admin_id)
                    handle.close()
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRegistration successful")


def new_user_reg():
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ----------------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t\t\t\t\tNEW ACCOUNT\t\t\t\t   |\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ----------------------------------------------")
    username = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Username: ").upper()
    password = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Password: ").lower()

    # save each new login as a dictionary key and value pair
    if os.path.isfile("username_password.txt") is False:
        print("\n---Can't write to username_password.txt, file not found---")
    else:
        file_handle = open("username_password.txt", "r")
        for i in file_handle:
            if i.startswith(username):
                print("---Username already in use, try another username---")
                return new_user_reg()
            else:
                handle = open("username_password.txt", "a")
                if len(password) > 8:
                    print("Password too long, your password must not be more than 8 characters long")
                    return new_user_reg()
                else:
                    user_id = random_user_id()
                    handle.write("\n")
                    handle.write(username)
                    handle.write("\t\t\t\t\t\t")
                    handle.write(password)
                    handle.write("\t\t\t\t\t\t")
                    handle.write(user_id)
                    handle.close()
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRegistration successful")

# ======================================================================================================================================================================================

# ======================================================================================================================================================================================

# this will get general login details


def general_login():
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ----------------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t\t\t\t\tLOGIN\t\t\t\t\t   |\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ----------------------------------------------")
    username = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tUSERNAME: ").upper()
    password = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPASSWORD: ").lower()
    wrong_username = ""
    wrong_password = ""
    if username == wrong_username or password == wrong_password:
        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInvalid username or password...")
        return general_login()

    if os.path.isfile("username_password.txt") is True:
        file_handle = open("username_password.txt", "r")
        for i in file_handle:
            if i.startswith(username) is True:
                z = i.split()
                x = z[1]
                if x != password:
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogin unsuccessful, Invalid username or password...")
                    return general_login()
                if x == password:
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t---Login successful---\nLoading...")
    return None

# ======================================================================================================================================================================================

# ======================================================================================================================================================================================

# this will get admin login details
def admin_login():
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t -----------------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t\t\t\t\tADMIN LOGIN\t\t\t\t\t|\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t -----------------------------------------------")
    wrong_username = ""
    wrong_admin_key = ""
    username = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tENTER USERNAME: ").upper()
    admin_key = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tENTER ADMIN KEY: ").upper()
    if username == wrong_username or admin_key == wrong_admin_key:
        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogin unsuccessful, Invalid Username or Admin key...")
        return admin_login()
    if os.path.isfile("username_password.txt") is True:
        file_handle = open("username_password.txt", "r")
        for i in file_handle:
            if i.startswith(username):
                z = i.split()
                x = z[2]
                if x != admin_key:
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogin unsuccessful, Invalid Admin key...")
                    return admin_login()
                if x == admin_key:
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t---Login successful---\nLoading...")

# ======================================================================================================================================================================================

# ======================================================================================================================================================================================


def user_login():
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t -----------------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\t\t\t\t\tUSER LOGIN\t\t\t\t\t|\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t -----------------------------------------------")
    wrong_username = ""
    wrong_user_key = ""
    username = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tENTER USERNAME: ").upper()
    user_key = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tENTER USER KEY: ").upper()
    if username == wrong_username or user_key == wrong_user_key:
        print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogin unsuccessful, Invalid Username or User key...")
    if os.path.isfile("username_password.txt") is True:
        file_handle = open("username_password.txt", "r")
        for i in file_handle:
            if i.startswith(username):
                z = i.split()
                x = z[2]
                if x != user_key:
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLogin unsuccessful, Invalid User key...")
                    return user_login()
                if x == user_key:
                    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t---Login successful---\nLoading...")
# ======================================================================================================================================================================================
