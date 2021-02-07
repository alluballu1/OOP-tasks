
import random
import cookie_demo as cookie
import CellPhoneClass as CellPhone

# Main function


def main():
    print("Hello")

    choices = ["rock", "paper", "scissors"]
    cookie_shape = random.choice(choices)
    cookie_flavor = input("choose a flavor: ")


    my_cookie = cookie.cookie(cookie_shape, cookie_flavor)

    new_flavor = input(cookie_flavor + " sucks, pick a new one: ")
    my_cookie.set_flavor(new_flavor)


    print(my_cookie, my_cookie.get_shape())




main()