costs = {"socks": 5, "shoes": 60, "sweater": 30}
items_bought = []


# Method to fill the items array
def newItem(item):
    items_bought.append(item)
    print(items_bought)


# Calculate the total of the items
def get_Total(tax):
    total = 0
    # first I need to get the list of items,
    for item in items_bought:
        # then check if the items are in the dictionary
        if item in costs:
            print(f"{item} exists in the dictionary")
            total += costs[item]
        else:
            print(f"{item} doesnt exist in the dictionary")
    total += total * tax
    print(f"The total is: {total}")
    return round(total, 2)


# add the items to the purcharse_array
def add_item():
    while True:
        print("\n Add the items to the array(type STOP to finish) \n")
        item_bougth = input("Enter the item: ").strip()
        if item_bougth.lower() == "stop":
            print("\n")
            break
        newItem(item_bougth)
    taxes = float(input("Please enter the amount of taxes: "))
    get_Total(taxes)


if __name__ == "__main__":
    add_item()

## 2.How much will you spend given a dictionary of items and their costs an array specifying the items bought,
## calculate the total cost of the items plus a given tax.
## If item doesnt exist in the given cost values,the item is ignored.Output should be rounded to two decimal places.
