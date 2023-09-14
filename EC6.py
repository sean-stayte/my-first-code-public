import math as math
addition_num = 0
total = 0
user_number = int(input("Type any number: "))
user_choice = (input("What would you like to do? Type SUM to compute the sum of all the numbers up to yours, or type PRODUCT to compute the product: "))

if user_choice == "SUM" :
    while addition_num <= user_number :
        total = total + addition_num
        addition_num = addition_num + 1
    print(total)
    
elif user_choice == "PRODUCT" :
    print(math.factorial(user_number))

else :
    print("Sorry, that choice is not recognised. Please try again")