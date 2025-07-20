# Fun-Fact-Generator
simple python program to practice python
![Python Version](https://img.shields.io/badge/python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
## Overview
The Fun Fact Generator is a simple Python application that displays random fun facts from a predefined list. The program keeps track of which facts have been shown and can reset the used facts when needed.

## Features
- 🎲 Displays random fun facts from 'FunFacts.txt'

- 📝 Tracks used facts in 'UsedFacts.txt'

- 🔄 Option to view all previously used facts

- 📋 Reset function to make all facts available again

- 🖥️ Simple and intuitive GUI interface

## Requirements
- Python 3.x

- Tkinter (usually comes with Python installation)

## Installation
1. Ensure you have Python 3 installed on your system

2. Download the following files:

    - 'FunFactGenerator.py'

    - 'FunFacts.txt'

3. Place both files in the same directory

> [!NOTE]
> The program will automatically create UsedFacts.txt when needed

## Usage
Run the program by executing: python FunFactGenerator.py

The main window will appear with three buttons:
|Button     | Action    |
|-----------|-----------|
|Get Fun Fact|Displays a random unused fact|
|Reset Used Facts|Resets the tracking of used facts|
|Show Used Facts|Displays all previously shown facts|



## File Structure
Fun-Fact-Generator/

├── FunFactGenerator.py    # Main application script

├── FunFacts.txt          # Database of available fun facts

└── UsedFacts.txt         # Automatically generated tracking file


## Notes

> [!NOTE]
> If all facts have been used, the program will prompt you to reset

> [!NOTE]
> The reset function combines all facts from both files and clears the used facts list

> [!NOTE]
> You can easily add more fun facts by editing the FunFacts.txt file
Open FunFacts.txt in a text editor

