class Dictionary:
    # Constructor: Initializes the dictionary
    def __init__(self):
        self.words = {}  # Instance-level dictionary to store words

    # Add a new word to the dictionary
    def new_Entry(self):
        word = input("Enter the word: ").strip()
        description = input("Enter the description: ").strip()
        self.words[word] = description
        print(f"'{word}' has been added to the dictionary.")

    # Look up a word in the dictionary
    def look(self):
        word = input("Enter the word to look up: ").strip()
        if word in self.words:
            print(f"The description for '{word}' is: {self.words[word]}")
        else:
            print(f"'{word}' not found in the dictionary.")

    # Main method to handle user interaction
    def run(self):
        actions = {
            "1": self.new_Entry,
            "2": self.look,
            "3": self.exit_program,
        }

        while True:
            print("\nOptions:")
            print("1. Add a new word")
            print("2. Look up a word")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            action = actions.get(choice)
            if action:
                action()  # Call the corresponding method
            else:
                print("Invalid choice. Please select a valid option.")

    # Exit the program
    def exit_program(self):
        print("Exiting the program. Goodbye!")
        exit()


if __name__ == "__main__":
    d = Dictionary()
    d.run()

# 1.in this kata your job its to create a class dictionary which you can add words to and their entries