# Exercise 1

user_funds = 10.31
item_price = int(input(f"Item cost is: "))

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
else:
    print("Sorry you don't have enough money")


# Exercise 2

def product(n):
    total = 1
    for i in n:
        total *= i
    return total


print(product([4, 4, 5]))


# Exercise 3

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                return False
        return True


# Exercise 4

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n += 1

print(item_list[4])
