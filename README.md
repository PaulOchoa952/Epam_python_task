# Dictionary Project

Welcome to the **Dictionary Project**! This project is a compilation of exercises to work with dictionaries and explores concepts such as class creation, working with collections, and implementing logic to solve problems. The project includes command-line interaction, Python object-oriented programming, and the ability to execute tests with `pytest` integrated with GitHub Actions for continuous integration.

---

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Setup and Installation](#setup-and-installation)
4. [How to Run](#how-to-run)
5. [Usage](#usage)
6. [Testing](#testing)
7. [GitHub Actions](#github-actions)
8. [Example Workflow](#example-workflow)

---

## Project Description

This project consists of tasks that involve working with a dictionary-like structure. Three main exercises have been implemented:

1. **Creating and Managing a Dictionary**  
   This includes the ability to add new entries with names and descriptions and search for specific information in the dictionary.

2. **Shopping List Cost Calculator**  
   Given a dictionary of items and their costs, along with an array of items bought, this module calculates the total cost of the items, including a user-specified tax. If an item isn't found in the cost list, it is ignored.

3. **String Word Assembly**  
   Takes an array of words and concatenates the nth letter from each word, where `n` is the position of the word in the list.

The program is interactive, operating as a command-line menu-driven application.

---

## Features

- Add new entries to a dictionary.
- Search for entries by name.
- Track items bought, their costs, and calculate totals with taxes.
- Solve the nth letter word combination problem.
- Command-line interface for user interactivity.
- Integrated testing with `pytest`.
- GitHub Actions workflow for continuous integration.

---

## Setup and Installation

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
2. **Navigate to the Project directory**  
   Navigate:
   ```bash
   cd Epam_Python_task
3. **Install dependencies.Create and activate a virtual enviroment**
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
---
 ## How to Run

 Each task is implemented in its own file. You can run them individually as follows:

 1. **Run the Dictionary Task**  
    Add and search for words in the dictionary:
    ```bash
    python dictionary_task.py
    ```

 2. **Run the Spending/Tax Calculation Task**  
    Add items to a shopping list and calculate the total cost:
    ```bash
    python spend_task.py
    ```

 3. **Run the nth Letter Word Assembly Task**  
    Solve the kata problem of concatenating the nth letter from each word in a list:
    ```bash
    python array_task.py
    ```

 ---

 ## Usage

  Dictionary Task
 - Add a word with a name and description to the dictionary.
 - Search for a word by name and display its description.

  Spending/Tax Calculation Task
 - Add items to your shopping list.
 - Calculate the total cost of the items, including a user-specified tax.

  nth Letter Word Assembly Task
 - Concatenate the nth letter from each word in a list, where `n` is the position of the word in the list.

 ---

 ## Testing

 The project includes integration with `pytest` for unit testing. To run the test suite:

 1. Navigate to the `tests` folder:
    ```bash
    cd tests
    ```

 2. Run the tests:
    ```bash
    python -m unittest discover
    ```

  Example Tests Include:
 1. **Adding and searching for words in the dictionary.**  
 2. **Calculating total costs with and without ignoring items not in the cost dictionary.**  
 3. **Assembling the word from an array of words.**

 ---

 ## Makefile Commands

 This project includes a `Makefile` to simplify common tasks such as installing dependencies, running tests, linting, and executing specific examples.

  General Commands
 - **`make help`**: Display the list of available commands.
 - **`make install`**: Install all required dependencies from `requirements.txt`.
 - **`make lint`**: Run Ruff for code linting.
 - **`make test`**: Run Pytest for unit tests.
 - **`make clean`**: Clean up Python cache and temporary files.

  Example-Specific Commands
 - **`make dict`**: Run the dictionary task to add words and their descriptions.
 - **`make spend`**: Run the spending/tax calculation task.
 - **`make array`**: Run the nth letter concatenation task.