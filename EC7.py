user_number = int(input("Which number would you like the times table for? "))
user_multiple = int(input("And how many multiples would like to see? "))
multiple = 0
while multiple < user_multiple :
    multiple = multiple + 1
    print(str(multiple) + " x " + str(user_number) + " = " + str(multiple * user_number))