# File name: tkinter Main Program.py
# Author: Alex Porri
# Description: The main GUI on which the functionalities will be built on.

import tkinter as tk

# SOME NOTES FOR MYSELF, PLEASE IGNORE
# root.tk.TK() for creating the main window
# Toplevel is for creating a new window (IMPORTANT!)
# Labels are for the texts
# Use grid instead of pack to arrange the "blocks" better
# Lambda functions to pass data on commands (button/onClick functionalities)


# Function for admitting the player info to the main screen (later the class creation)

def secondButtonPress(etunimi, sukunimi, window, list_of_players):
    list_of_players.insert("end", etunimi.get() + " " + sukunimi.get())
    window.destroy()


# Window for the player info input
# Will add age, experience with the game, etc. later

def add_player(root, list_of_players):
    new_window = tk.Toplevel(root)
    new_window.geometry("200x200")

    first_name = tk.Label(new_window, text="Etunimi")
    first_name_entry = tk.Entry(new_window)
    last_name = tk.Label(new_window, text="Sukunimi")
    last_name_entry = tk.Entry(new_window)
    new_button = tk.Button(new_window, text="Lisää pelaaja",
                           command=lambda: secondButtonPress(first_name_entry, last_name_entry, new_window, list_of_players))

    first_name.grid(row=0, column=0, pady=5, padx=10)
    first_name_entry.grid(row=0, column=1, pady=5)
    last_name.grid(row=1, column=0, pady=5, padx=10)
    last_name_entry.grid(row=1, column=1, pady=5)
    new_button.grid(row=2, column=0, columnspan=4, pady=30)

# Function for displaying the selected player's data (currently only the first and last name is shown)

def display_name(event, name):
    selected_name = event.widget.curselection()
    if selected_name:
        index = selected_name[0]
        name_of_player = event.widget.get(index)
        name.configure(text=name_of_player)
    else:
        name.configure(text="")

# Main function for the main window of the program

def main():
    root = tk.Tk()
    name = tk.Label(root)
    list_of_players = tk.Listbox(root)
    button = tk.Button(root, text="Uusi pelaaja", command=lambda: add_player(root, list_of_players))
    button.grid(row=0, column=0, pady=2)
    name.grid(row=0, column=1, pady=2, columnspan=2)
    list_of_players.grid(row=1, column=0, pady=2)
    list_of_players.bind("<<ListboxSelect>>", lambda event, arg=None: display_name(event, name))

    root.mainloop()


main()
