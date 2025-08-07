enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
potion_strength = 10
def drint_potion():
    print(potion_strength)

drint_potion()
print(potion_strength)