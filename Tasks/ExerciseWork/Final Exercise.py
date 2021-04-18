# File name: Final Exercise.py
# Author: Alex Porri
# Description: The main GUI on which the functionalities will be built on.

import tkinter as tk
from tkinter import ttk
import random

from CharacterClass import Character

# SOME NOTES FOR MYSELF, PLEASE IGNORE
# root.tk.TK() for creating the main window
# Toplevel is for creating a new window (IMPORTANT!)
# Labels are for the texts
# Use grid instead of pack to arrange the "blocks" better
# Lambda functions to pass data on commands (button/onClick functionalities)


# Function for admitting the player info to the main screen (later the class creation)

def secondButtonPress(first_name, last_name, window, list_of_players, experience, age, player_list):
    player_name = first_name.get() + " " + last_name.get()
    new_player = Character(player_name, age.get(), experience.get())
    list_of_players.insert("end", new_player)
    player_list.append(new_player)
    print(player_list)
    window.destroy()


# Window for the player info input
# Will add age, experience with the game, etc. later -- DONE

def add_player(root, list_of_players, player_list):
    new_window = tk.Toplevel(root)

    new_window.title("Add a new player")

    first_name = tk.Label(new_window, text="First name")
    first_name_entry = tk.Entry(new_window)
    last_name = tk.Label(new_window, text="Last name")
    last_name_entry = tk.Entry(new_window)
    age = tk.Label(new_window, text="Age")
    age_entry = tk.Entry(new_window)
    experience = tk.Label(new_window, text="Experience")

    # Using ttk instead of basic tkinter widgets due to better visuals (ttk.Combobox vs. tk.Optionsmenu)

    set_experience = ttk.Combobox(new_window)
    set_experience["values"] = ("Inexperienced", "Novice", "Intermediate", "Experienced")
    set_experience.insert(0, "Select")
    new_button = tk.Button(new_window, text="Add player", width=35,
                           command=lambda: secondButtonPress(first_name_entry, last_name_entry, new_window,
                                                             list_of_players, set_experience, age_entry, player_list))

    first_name.grid(row=0, column=0, pady=5, padx=10)
    first_name_entry.grid(row=0, column=1, pady=5)
    last_name.grid(row=1, column=0, pady=5, padx=10)

    last_name_entry.grid(row=1, column=1, pady=5)
    age.grid(row=2, column=0, pady=5, padx=10)
    age_entry.grid(row=2, column=1, pady=5, padx=10)
    experience.grid(row=3, column=0, pady=5, padx=10)
    set_experience.grid(row=3, column=1, pady=5, padx=10)
    new_button.grid(row=4, column=0, columnspan=2)

# The main window where the character data can be viewed and modified

def character_window(root, event, player_list):
    new_window = tk.Toplevel(root)
    new_window.title("Customize player character")
    new_window.attributes("-topmost", True)

    name = tk.Label(new_window)
    age = tk.Label(new_window)

    experience = tk.Label(new_window)
    list_number = get_class_num(event, player_list)

    # creating the tkinter widgets

    save_button = tk.Button(new_window, text="Save", width=20,
                            command=lambda: save_function(race_entry, charname_entry, charclass_entry,
                                                          intellect_entry, strength_entry, dexterity_entry,
                                                          constitution_entry, player_list, list_number))
    print_button = tk.Button(new_window, text="Print data", width=20,
                             command=lambda: print_function(player_list, list_number))

    name_label = tk.Label(new_window)
    name_label.configure(text="Player name:")
    age_label = tk.Label(new_window)
    age_label.configure(text="Player age:")
    experience_label = tk.Label(new_window)
    experience_label.configure(text="Player experience:")

    name_label.grid(row=0, column=0)
    name.grid(row=0, column=1, pady=2)
    age_label.grid(row=1, column=0)
    age.grid(row=1, column=1, pady=2)
    experience_label.grid(row=2, column=0)
    experience.grid(row=2, column=1, pady=2)

    race_description = tk.Label(new_window)
    race_description.configure(text="Character race: ")
    character_name = tk.Label(new_window)
    character_name.configure(text="Character name: ")
    character_class = tk.Label(new_window)
    character_class.configure(text="Character class: ")
    intellect_description = tk.Label(new_window)
    intellect_description.configure(text="Intellect (INT): ")
    strength_description = tk.Label(new_window)
    strength_description.configure(text="Strength (STR): ")
    dexterity_description = tk.Label(new_window)
    dexterity_description.configure(text="Dexterity (DEX): ")
    constitution_description = tk.Label(new_window)
    constitution_description.configure(text="Constitution (CST): ")

    race_entry = ttk.Combobox(new_window, width=18)
    race_entry["values"] = ("Dwarf", "Elf", "Human")
    charname_entry = tk.Entry(new_window, width=22)
    charclass_entry = ttk.Combobox(new_window, width=18)
    charclass_entry["values"] = ("Mage", "Priest", "Fighter")
    intellect_entry = tk.Spinbox(new_window, from_=0, to=18)
    strength_entry = tk.Spinbox(new_window, from_=0, to=18)
    dexterity_entry = tk.Spinbox(new_window, from_=0, to=18)
    constitution_entry = tk.Spinbox(new_window, from_=0, to=18)

    display_name(event, name, age, experience, player_list, charname_entry, charclass_entry,
                 intellect_entry, strength_entry, dexterity_entry, constitution_entry, race_entry)

    # Using grid instead of pack due to better layout planning

    character_name.grid(row=4, column=0)
    charname_entry.grid(row=4, column=1, padx=10)
    race_description.grid(row=5, column=0)
    race_entry.grid(row=5, column=1)
    character_class.grid(row=6, column=0)
    charclass_entry.grid(row=6, column=1)
    intellect_description.grid(row=7, column=0)
    intellect_entry.grid(row=7, column=1)
    strength_description.grid(row=8, column=0)
    strength_entry.grid(row=8, column=1)
    dexterity_description.grid(row=9, column=0)
    dexterity_entry.grid(row=9, column=1)
    constitution_description.grid(row=10, column=0)
    constitution_entry.grid(row=10, column=1)
    save_button.grid(row=12, column=0)
    print_button.grid(row=12, column=1)


# Function for displaying the selected player's data (currently only the first and last name is shown)

def get_class_num(event, player_list):
    selected_name = event.widget.curselection()
    if selected_name:
        index = selected_name[0]
        name_of_player = event.widget.get(index)
        for x in range(len(player_list)):
            if player_list[x].get_name() == name_of_player:
                return x

# Function for saving the changed character data

def save_function(race_entry, charname_entry, charclass_entry,
                  intellect_entry, strength_entry, dexterity_entry,
                  constitution_entry, player_list, list_number):
    player_list[list_number].set_character_class(charclass_entry.get())
    player_list[list_number].set_race(race_entry.get())
    player_list[list_number].set_character_name(charname_entry.get())
    player_list[list_number].set_intellect(intellect_entry.get())
    player_list[list_number].set_strength(strength_entry.get())
    player_list[list_number].set_dexterity(dexterity_entry.get())
    player_list[list_number].set_constitution(constitution_entry.get())
    print("Saved!")

# Simple function for calling the "get all" function from the Character class

def print_function(player_list, list_number):
    print(player_list[list_number].get_all())

# Function for displaying the character data based on the player name. Flawed but works for demonstration purposes.

def display_name(event, name, age, experience, player_list, charname_entry, charclass_entry,
                 intellect_entry, strength_entry, dexterity_entry, constitution_entry, race_entry):
    selected_name = event.widget.curselection()

    charname_entry.delete(0, "end")
    intellect_entry.delete(0, "end")
    strength_entry.delete(0, "end")
    dexterity_entry.delete(0, "end")
    constitution_entry.delete(0, "end")

    name.configure(text="")
    age.configure(text="")
    experience.configure(text="")

    if selected_name:
        index = selected_name[0]
        name_of_player = event.widget.get(index)

        # IMPORTANT!!!!: get the callable class/object functions with dir(object)

        for x in range(len(player_list)):
            print(player_list[x].get_name(), player_list[x].get_race(), player_list[x]._Player__age)
            if player_list[x].get_name() == name_of_player:
                name.configure(text=name_of_player)
                age.configure(text=player_list[x]._Player__age)
                experience.configure(text=player_list[x]._Player__experience)
                charname_entry.insert(0, player_list[x].get_character_name())
                charclass_entry.insert(0, player_list[x].get_character_class())
                race_entry.insert(0, player_list[x].get_race())
                intellect_entry.insert(0, player_list[x].get_intellect())
                strength_entry.insert(0, player_list[x].get_strength())
                dexterity_entry.insert(0, player_list[x].get_dexterity())
                constitution_entry.insert(0, player_list[x].get_constitution())

    else:
        name.configure(text="")
        age.configure(text="")
        experience.configure(text="")


# Main function for the main window of the program

def main():
    player_list = []
    root = tk.Tk()
    root.title("Character creation tool")

    list_of_players = tk.Listbox(root)

    button = tk.Button(root, text="New player", command=lambda: add_player(root, list_of_players, player_list))
    button.grid(row=0, column=0, pady=5)

    list_of_players.grid(row=1, column=0, pady=10, padx=10)
    list_of_players.bind('<Double-Button>', lambda event, arg=None: character_window(root, event, player_list))

    root.mainloop()


main()
