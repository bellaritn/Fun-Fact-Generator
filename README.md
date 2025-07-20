# Fun-Fact-Generator
simple python program to practice python
## Overview
The Fun Fact Generator is a simple Python application that displays random fun facts from a predefined list. The program keeps track of which facts have been shown and can reset the used facts when needed.

## Features
Displays random fun facts from "FunFacts.txt"

Tracks used facts in "UsedFacts.txt"

Option to view all previously used facts

Reset function to make all facts available again

Simple and intuitive GUI interface

## Requirements
Python 3.x

Tkinter (usually comes with Python installation)

 Installation
Ensure you have Python 3 installed on your system

Download the following files:

FunFactGenerator.py

FunFacts.txt

Place both files in the same directory

## Usage
Run the program by executing: python FunFactGenerator.py

The main window will appear with three buttons:

Get Fun Fact: Displays a random unused fact

Reset Used Facts: Resets the tracking of used facts

Show Used Facts: Displays all previously shown facts

## File Descriptions
FunFactGenerator.py: The main Python script containing the application logic

FunFacts.txt: Text file containing all available fun facts (one per line)

UsedFacts.txt: Automatically created file to track which facts have been shown

## Customization
You can easily add more fun facts by editing the FunFacts.txt file:

Open FunFacts.txt in a text editor

Add new facts, one per line

Save the file

The new facts will be available the next time you run the program

## Notes
The program will automatically create UsedFacts.txt when needed

If all facts have been used, the program will prompt you to reset

The reset function combines all facts from both files and clears the used facts list
