import tkinter as tk
import tkinter.messagebox
import random
import sys

box_number = 0
num_guesses = 0

def hide_the_diamond():
    global box_number, num_guesses
    box_number = random.randint(1, 10)
    num_guesses = 0
    
    for button in box_buttons:
        button.config(state=tk.NORMAL)
    hide_button.config(state=tk.DISABLED) 

def check_guess(box):
    global num_guesses
    num_guesses += 1
    
    if box == box_number:
        show_congratulations()
    else:
        instructions_label.config(text="Sorry, that's not it. Guesses: " + str(num_guesses))
        
        if num_guesses == 3:
            tkinter.messagebox.showinfo("GAME OVER", "Sorry, you're out of guesses.\nThe diamond was in box " + str(box_number) + ".")
            play_again = tkinter.messagebox.askyesno("Play Again?", "Do you want to play again?")
            if play_again:
                hide_the_diamond()
            else:
                sys.exit()

def show_congratulations():
    congrats_window = tk.Toplevel(root)
    congrats_window.title("Congratulations!")
    congrats_window.configure(bg="white")

    congrats_label = tk.Label(congrats_window, text="Congratulations: You found the diamond!", bg="white")
    congrats_label.pack(pady=10)

    play_again_button = tk.Button(congrats_window, text="Play Again", command=lambda: [congrats_window.destroy(), hide_the_diamond()])
    play_again_button.pack(pady=10)
    play_again_button.config(bg="darkslategray", fg="linen")

    exit_button = tk.Button(congrats_window, text="Exit", command=sys.exit)
    exit_button.pack(pady=10)
    exit_button.config(bg="navy blue", fg="linen")

root = tk.Tk()
root.title("Find the Diamond Game")
root.configure(bg="mint cream")

root.resizable(False, False)

img = tk.PhotoImage(file="diamond.gif")
image_label = tk.Label(root, image=img)

instructions_label = tk.Label(root, text="Welcome: Click 'Hide The Diamond' to start.")
instructions_label.config(bg="mint cream", wraplength=300, anchor=tk.W, justify=tk.LEFT)
instructions_label.grid(row=1, column=5, rowspan=3, padx=10, pady=10)

box_buttons = []

def handle_box_1():
    check_guess(1)
BoxOne = tk.Button(root, text="Box 1", width=10, height=3, state=tk.DISABLED, bg="powder blue", fg="white", command=handle_box_1)
BoxOne.grid(row=1, column=0, padx=10, pady=10)
box_buttons.append(BoxOne)

def handle_box_2():
    check_guess(2)
BoxTwo = tk.Button(root, text="Box 2", width=10, height=3, state=tk.DISABLED, bg="cadet blue", fg="white", command=handle_box_2)
BoxTwo.grid(row=1, column=1, padx=10, pady=10)
box_buttons.append(BoxTwo)

def handle_box_3():
    check_guess(3)
BoxThree = tk.Button(root, text="Box 3", width=10, height=3, state=tk.DISABLED, bg="lightsteelblue", fg="white", command=handle_box_3)
BoxThree.grid(row=1, column=2, padx=10, pady=10)
box_buttons.append(BoxThree)

def handle_box_4():
    check_guess(4)
BoxFour = tk.Button(root, text="Box 4", width=10, height=3, state=tk.DISABLED, bg="lightcyan", fg="white", command=handle_box_4)
BoxFour.grid(row=1, column=3, padx=10, pady=10)
box_buttons.append(BoxFour)

def handle_box_5():
    check_guess(5)
BoxFive = tk.Button(root, text="Box 5", width=10, height=3, state=tk.DISABLED, bg="deepskyblue", fg="white", command=handle_box_5)
BoxFive.grid(row=1, column=4, padx=10, pady=10)
box_buttons.append(BoxFive)

def handle_box_6():
    check_guess(6)
BoxSix = tk.Button(root, text="Box 6", width=10, height=3, state=tk.DISABLED, bg="lightskyblue", fg="white", command=handle_box_6)
BoxSix.grid(row=2, column=0, padx=10, pady=10)
box_buttons.append(BoxSix)

def handle_box_7():
    check_guess(7)
BoxSeven = tk.Button(root, text="Box 7", width=10, height=3, state=tk.DISABLED, bg="paleturquoise", fg="white", command=handle_box_7)
BoxSeven.grid(row=2, column=1, padx=10, pady=10)
box_buttons.append(BoxSeven)

def handle_box_8():
    check_guess(8)
BoxEight = tk.Button(root, text="Box 8", width=10, height=3, state=tk.DISABLED, bg="darkturquoise", fg="white", command=handle_box_8)
BoxEight.grid(row=2, column=2, padx=10, pady=10)
box_buttons.append(BoxEight)

def handle_box_9():
    check_guess(9)
BoxNine = tk.Button(root, text="Box 9", width=10, height=3, state=tk.DISABLED, bg="lightskyblue", fg="white", command=handle_box_9)
BoxNine.grid(row=2, column=3, padx=10, pady=10)
box_buttons.append(BoxNine)

def handle_box_10():
    check_guess(10)
BoxTen = tk.Button(root, text="Box 10", width=10, height=3, state=tk.DISABLED, bg="lightcyan", fg="white", command=handle_box_10)
BoxTen.grid(row=2, column=4, padx=10, pady=10)
box_buttons.append(BoxTen)

hide_button = tk.Button(root, text="Hide The Diamond", width=20, height=2, command=hide_the_diamond)
hide_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
hide_button.configure(bg="dodger blue")

image_label = tk.Label(root, image=img, bg="ghost white")
image_label.grid(row=0, column=5, rowspan=2, padx=10, pady=10)

def show_instructions():
    tkinter.messagebox.showinfo("Instructions", "Click the Hide The Diamond button to start the game. Then, click on the box where you think the diamond is hidden. You have three guesses to find it.")

instructions_button = tk.Button(root, text="Instructions", width=15, height=2, command=show_instructions)
instructions_button.grid(row=3, column=2, columnspan=3, padx=10, pady=10)
instructions_button.configure(bg="cyan")

# Start the event loop
root.mainloop()