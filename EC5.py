addition_num = 0
total = 0
user_number = int(input("Enter any number here: "))
while addition_num <= user_number :
    if addition_num % 3 == 0 :
        total = total + addition_num
        addition_num = addition_num + 1
    elif addition_num % 5 == 0 :
        total = total + addition_num
        addition_num = addition_num + 1
    else :
        addition_num = addition_num + 1
print(total)
