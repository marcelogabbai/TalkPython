import random
mm_count = random.randint(1, 100)
guess = 0
tries = 0
guess = int(input("How many m&m in the jar"))
while guess != mm_count:

    tries += 1
    if guess > mm_count:
        print("guess is greater")
    elif guess < mm_count:
        print("guess is lower")
    elif guess == mm_count:
        print("you win")
