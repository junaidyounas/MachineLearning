# Community Food Sharing System

This folder contains `index.py`, a simple menu-driven Python program for a community food sharing system.

## Program Description

The program offers a terminal menu with the following options:

1. Donate Food
2. View Food
3. Search Food
4. Exit

Users can enter their choice and then provide donation details such as food name, quantity, category, and location.

## How to Run

1. Open a terminal in this folder.
2. Run the program with:

```bash
python index.py
```

3. Follow the on-screen menu prompts.

## Notes

- The program stores donated food items in a list called `food_items`.
- Option 2 and option 3 are placeholders and currently only print a selection message.
- There is a typo in `index.py` where `quanitity` should be `quantity`.
- The donated food item is stored as a set rather than a dictionary; this may affect how duplicate or named fields are handled.

## File

- `index.py` - Main program file for the menu-based community food sharing system.
