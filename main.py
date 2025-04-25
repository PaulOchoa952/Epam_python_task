"""dictionaries first excersice
fruit={'name':'pear','color':'green','price':23,'dishes':['pear pie','pear soup']}

for key,value in fruit.items():
    #print(key,":",value)
"""

# 1.in this kata your job its to create a class dictionary wich you can add words to and their entries

"""2.How much will you spend given a dictionary of items and their costs an array specifying the items bought,
calculate the total cost of the items plus a given tax.
If item doesnt exist in the given cost values,the item is ignored.Output should be rounded to two decimal places.
"""

"""
3.Complete the function that takes an array of words.You must concatenate the n th letter from each word 
wich should be returned as a string,where n is the position of the word in the list
"""


class Dictionary:
    # Constructor: Initializes the dictionary
    def __init__(self):
        self.fruit = {}  # instace-level dictionary to store fruits
        self.costs = {"socks": 5, "shoes": 60, "sweater": 30}
        self.items_bought = []

    # add a new fruit to the dictionary
    def newEntry(self, name, description):
        self.fruit[name] = description

    # Method to display name
    def look(self, name):
        if name in self.fruit:
            print(f"The description for {name} is: {self.fruit[name]}")
        else:
            print(f"{name} not found in the dictionary")

    # Method to fill the items array
    def newItem(self, item):
        self.items_bought.append(item)
        print(self.items_bought)

    # Calculate the total of the items
    def get_Total(self, tax):
        total = 0

        # first I need to get the list of items,
        for item in self.items_bought:
            # then check if the items are in the dictionary
            if item in self.costs:
                print(f"{item} exists in the dictionary")
                total += self.costs[item]
            else:
                print(f"{item} doesnt exist in the dictionary")
        total += total * tax
        print(f"The total is: {total}")
        return round(total, 2)


# menu method
def menu():
    while True:
        print(
            "Select the task you want to try\n "
            "1. Add a new word \n "
            "2. Look up a word's description \n "
            "3. Add an item to the bought items list \n "
            "4. Get the concatenated word from the array \n "
            "5. Exit"
        )

        choice = input("Enter the number of task you want to try: ").strip()

        if choice == "1":
            add_to_dictionary()
        elif choice == "2":
            lookup_for_word()
        elif choice == "3":
            add_item()
        elif choice == "4":
            get_the_word()
        elif choice == "5":
            print("Exiting the program. GoodBye!")
            break
        else:
            print("Invalid choice.Please select valid option from the menu!")


# add a new word to the dictinary with a while loop
def add_to_dictionary():
    while True:
        print("\nEnter a word(type STOP to finish): ")
        name = input("Enter the name of the word:").strip()
        if name.lower() == "stop":
            print("\n")
            break
        description = input(f"Enter the description of {name}: ").strip()
        d.newEntry(name, description)


# display specific word description
def lookup_for_word():
    while True:
        print("\n Look for a specific word(type STOP to finish)")
        search_name = input("Enter the search_name of the word:").strip()
        if search_name.lower() == "stop":
            print("\n")
            break
        d.look(search_name)


# add the items to the purcharse_array
def add_item():
    while True:
        print("\n Add the items to the array(type STOP to finish)")
        item_bougth = input("Enter the item: ").strip()
        if item_bougth.lower() == "stop":
            print("\n")
            break
        d.newItem(item_bougth)
    taxes = float(input("Please enter the amount of taxes: "))
    d.get_Total(taxes)


def get_the_word(value=""):
    word = ["yoda", "best", "has"]  # -->yes
    for i in range(len(word)):
        if len(word[i]) > i:
            value += word[i][i]
    print(value)


# Initialize the instace of you class
d = Dictionary()

if __name__ == "__main__":
    menu()
