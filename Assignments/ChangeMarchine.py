import math

total_money = float(input("How much money you have? "))

num_20s = int(math.floor(total_money // 20))
total_money -= (num_20s * 20)

num_10s = int(math.floor(total_money // 10))
total_money -= (num_10s * 10)

num_1s = int(math.floor(total_money // 1))
total_money -= (num_1s * 1)

num_dimes = int(math.floor(total_money // 0.1))
total_money -= (num_dimes * 0.1)

num_nickels  = int(math.floor(total_money // 0.05))
total_money -= (num_nickels * 0.05)

num_cents = int(math.ceil(total_money*100))

print(f'the number of $20 bills is: {num_20s}')
print(f'the number of $10 bills is: {num_10s}')
print(f'the number of $1 bills is: {num_1s}')
print(f'the number of dimes is: {num_dimes}')
print(f'the number of nickels is: {num_nickels}')
print(f'the number of pennies is: {num_cents}')

# Test
# print((num_20s * 20) + (num_10s * 10)+ (num_1s * 1)+ (num_dimes * 0.1)+ (num_nickels * 0.05)+ (num_cents * 0.01))