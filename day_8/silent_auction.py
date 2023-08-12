from my_art.auction_logo import logo

my_dict = {}
auction_going = 1
print(logo)
print("Welcome to the secret auction game")

while auction_going:

    user_info = input('What is your name?: ')
    user_price = int(input("How much do you want ot bid?: "))
    my_dict[user_info] = user_price

    question = input('Any other bidders? y/n: ')
    if question == 'y':
        auction_going = True
        print("\n" * 100)
    else:
        my_name = 'Name'
        my_max = 0
        for k,v in my_dict.items():
            if v > my_max:
                my_max = v
                my_name = k
        print(f"The winner is {my_name} with bid$: {my_max}")
        auction_going = False

