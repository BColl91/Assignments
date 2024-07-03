import random

WORDS =("python", "estimate", "difficult", "answer", \
 "unnecessary", "adequate", "feasible", "character", "congratulations", \
 "sequence", "position", "program")

CLUES ={"python":"A programming language", "estimate":"To assess or calculate", \
           "difficult":"Not easy to do or understand", "answer":"A response to a question", \
            "unnecessary":"Not needed", \
           "adequate":"Sufficient, enough", "feasible":"Possible to do", \
           "character":"Someone in a story", "congratulations":"Well done", \
           "sequence":"A particular order in which related events occur", "position":"a Place"}

word = random.choice(WORDS)
clue = CLUES[word]
correct = word
anagram = ""

for n in range(0, len(word)):
     position = random.randrange(len(word))
     anagram += word[position]
     word = word[:position] + word[(position+1):]

print("\nWelcome to the anagram game.")
print("\nUnscramble the letters to make a word.")
print("\nThe anagram is:", anagram, "clue:", clue)
answer = input("\nYour answer: ")

while answer != correct and answer != "":
     print("\nSorry, that's not quite right.")
     answer = input("\nYour answer: ")

if answer == correct:
     print("\nWell done, you got it!")