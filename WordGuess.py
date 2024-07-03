# The Word Guess Game
import random
WORDS =("python", "moon", "difficult", "answer", \
		"cheese", "wensleydale", "wallace", \
		"gromit", "crackers", "congratulations", \
		"variable", "numbers", "program")
# Choose a random word from the Word list
word = random.choice(WORDS)
correct = word
hyphen = ""

# Show even letters only
for i in range(len(word)):
     remainder = i%2                  # check if i is odd or even
     if remainder != 0:
           hyphen += word[i]   # even letters
     else:
           hyphen += "-"       # odd letters
print("\n", hyphen)

print("\nWelcome to the Word Guess game.")
print("\nSome characters in the word will be hidden. You need to guess what the word is.")
answer = input("\nYour answer: ")
# Loop until the answer is correct or an empty string is input
while answer != correct and answer != "":
	print("\nSorry, that's not quite right. Try again.")
	answer = input("\nYour answer: ")
# The answer is correct
if answer == correct:
	print("\nCorrect!")