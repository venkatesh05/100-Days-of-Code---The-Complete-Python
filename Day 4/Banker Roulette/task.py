import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1
random_friends = random.randint(0,len(friends)-1)
print(friends[random_friends])

# option 2
random_friends = random.choice(friends)
print(random_friends)


