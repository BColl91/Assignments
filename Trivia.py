#THE TRIVIA PROGRAM
print("The Trivia Program")
name = input("what is your name?")
print("")
age = input("How old are you?")
print("")
weight = input("And for the sake of this program, how much do you weigh?")
print("")
print("Thank you", name, "! did you know:")

#calculate users age from years to seconds
age = float(age)
sage = age * 31557600
print("\n\tYou are", sage, "seconds old!\n\t")
print("")
print("")

#calculate users moon weight as
weight = float(weight)
weightm = (weight / 9.1) * 1.622
print("On the moon you would weigh", weightm, "kilos!")
print("")

#calculate your mars weight as
weightma = (weight / 9.1) * 3.711
print("But on Mars, you would weighh", weightma, "kilos!")
print("")

#calculate your venus weight as
weightv = (weight / 9.1) * 8.87
print("On Venus you would weigh", weightv, "kilos!")
print("")

#Calculate the difference in weight between the earth and moon
diff = weight - weightm
print("So", name, ", here is some great advice...")
print("fly to the moon and lose", diff, "kilos!")