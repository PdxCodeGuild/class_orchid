print(f"welcome to your recipe book")

recipe_book = []

#measurements = {}




while True:
    item_input= input(f"Please enter an item or 'done' to finish")
    amount_input = input("enter the amount of the item")
    if item_input != 'done':
        recipe_book.append(item_input)
        recipe_book.append(amount_input)
    if item_input == 'done':
        break
print(recipe_book)