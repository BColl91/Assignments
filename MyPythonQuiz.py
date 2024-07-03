import sys

def open_file(file_name, mode):
	try:
		file = open(file_name, mode)
	except IOError:
		print("Unable to open the file", file_name, "\n")
		print("closing Program..")
		sys.exit()
	else:
		return file

def next_line(file):
	line = file.readline()
	return line

def next_block(file):
	category = next_line(file) 
	question = next_line(file) 
	answers = [] 
	for i in range(4):
		answers.append(next_line(file))
	correct = next_line(file)
	if correct:
		correct = correct[0]
	explanation = next_line(file)
	return category, question, answers, correct, explanation

def main():
	games = [ "Y", "y", "Yes", "yes" ]
	print("\n***Welcome To The Gaming Knowledge Quiz~!***")
	name = input("\nWhat is your name? ")
	name = name.title()
	print("\nHiya,", name, "\b!")
	subject = input("\nDo you enjoy Computer Games? ")
	subject = subject.title()
	if subject in games:
		print("\nGood. I hope you enjoy this quiz!\n")
	else:
		print("\nThat's ok. I'm sure you'll enjoy this quiz anyway.\n")
	quiz_file = open_file("QuizQuestions.txt", "r")
	score = 0
	category, question, answers, correct, explanation = next_block(quiz_file)
	numQuestions = 0
	while category:
		numQuestions += 1
		print(category)
		print(question)
		for i in range(4):
			print(i + 1, "-", answers[i])
		answer = input("Choose your answer: ")
		if answer == correct:
			print("\nCorrect!", end=" ")
			score += 1
		else:
			print("\nSorry, that's not right.", end=" ")
		print(explanation)
		print("Score:", score, "from", numQuestions, "\b.\n")
		category, question, answers, correct, explanation = next_block(quiz_file)

	quiz_file.close()
	print("You have completed the quiz~!")
	print("\nYou're final score is", score, "Out of", numQuestions, "\b.")
 
main()

