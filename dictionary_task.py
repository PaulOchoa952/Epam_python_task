class Dictionary:
    # Constructor: Initializes the dictionary
    def __init__(self):
        self.words = {}  # instace-level dictionary to store words

    # add a new word to the dictionary
    def newEntry(self, name, description):
        self.words[name] = description

    # Method to display name
    def look(self, name):
        if name in self.words:
            print(f"The description for {name} is: {self.words[name]}")
        else:
            print(f"{name} not found in the dictionary")

if __name__ == "__main__":
    d=Dictionary()
    d.newEntry("grape","purple")
    d.look("grape")

# 1.in this kata your job its to create a class dictionary wich you can add words to and their entries
