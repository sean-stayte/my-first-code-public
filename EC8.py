
# Write a program that prints all prime numbers.

number = 1
# while number > 0: 
for number in range(100) :
    factors = []
    for i in range(1, number+1) :
      if number%i == 0 :
         factors.append(i)
    if len(factors) == 2 :
         print(number)
    number = number + 1