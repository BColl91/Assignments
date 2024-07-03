# Games module
class Player(object):
# Defines a player in a game
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score
	def __str__(self):
		rep = self.name + ":\t" + str(self.score)
		return rep
def askYesNo(question):
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response
def askForNumber(question, low, high):
	response = None
	while response not in range (low, high):
		response = int(input(question))
	return response
if __name__ == "__main__":
	print("You ran this module directly (not imported).")
	input("\nPress Enter to exit.")