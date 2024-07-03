
import random

WORDS = (
    "PYTHON", "ESTIMATE", "DIFFICULT", "ANSWER", "XYLOPHONE",
    "UNNECESSARY", "ADEQUATE", "FEASIBLE", "CHARACTER",
    "CONGRATULATIONS", "SEQUENCE", "POSITION", "PROGRAM"
)
MAX_WRONG = 6
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

def displayScaffold(wrong):
    """Display the scaffold based on the number of wrong guesses."""
    scaffold = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(scaffold[wrong])

print("\nWelcome to Hangman.")
print("\nYou have", MAX_WRONG, "wrong attempts to guess the word.")
while wrong < MAX_WRONG and so_far != word:
    displayScaffold(wrong)
    print("\n", so_far, "\n")
    guess = input("Enter a letter: ")
    guess = guess.upper()
    while guess in used:
        print("\nYou have already guessed this letter", guess)
        guess = input("Enter a letter: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYes,", guess, "is in the word.")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1
        left = MAX_WRONG - wrong
        print("\nYou have", left, "guesses left.")

displayScaffold(wrong)
if wrong == MAX_WRONG:
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")
print("\nThe word was", word)
