import random

random_integer = random.randint(1,10)

print(random_integer)

random_number_0_1 = random.random() * 10
print(random_number_0_1)

random_float = random.uniform(1,10)
print(random_float)

random_coin_flip = random.randint(0,1)
if random_coin_flip == 0:
    print("Heads")
else:
    print("Tails")
