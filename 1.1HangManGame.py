import random
print("Hello , You are welcome to hangman game to guess city name of nepal")
print("\n")
words = ['nepalgunj', 'pokhara', 'bhojpur', 'birtamode', 'dhading']


word = random.choice(words)

print("Guess the characters:")

guessed_word = ''

chances = 5

while chances > 0:
    failed = 0

    for char in word:
        if char in guessed_word:
            print(char, end='')

        else:
            print("_", end='')
            failed += 1

    if failed == 0:
        print('\n')
        print("You Win.")
        print("The word is: ", word + '.')
        break

    print('\n')
    guess = input("guess a character:")
    guess=guess.lower()
    guessed_word += guess

    if guess not in word:
        chances -= 1
        print("Wrong")
        print("You have", chances, 'more guesses.')

        if chances == 0:
            print("You Lose.")