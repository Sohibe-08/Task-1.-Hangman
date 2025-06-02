import random
Words = ["apple", "dream", "school", "python", "ocean"]
random_word = random.choice(Words)
guessed = ["_"] * len(random_word)
guesses = 0
tries = 6
while tries > guesses and "_" in guessed:
    x = input("Enter a letter: ").lower()
    if x in random_word:
        for i in range(len(random_word)):
            if x == random_word[i]:
                guessed[i] = x
    else:
        guesses += 1
        print(f"Wrong answer, guesses left {tries- guesses}")
    print("".join(guessed))
if "_" not in guessed:
    print(f"Congratulations, You've guessed the right answer")
else:
    print("You've lost, the correct answer is:", random_word)