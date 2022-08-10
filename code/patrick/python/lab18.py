from lab18ver2 import test
from lab18ver2_2 import test_2
import os
import csv
print(f"welcome to your recipe book")

recipe_book = []



def read():
    for filename in os.listdir('data/recipes'):
        with open(os.path.join("data/recipes", filename), 'r') as f:
            text = f.read()
            print(text)



options = '''
    1. Read the cookbook
    2. Add a new recipe to the cookbook
    3. Delete a recipe
    5. Search for a recipe from the library of 30,000 recipes
    6. Exit cookbook
     



'''


while True:
    user_choice = input(options)

    if user_choice == "1":
        read()

    elif user_choice == "2":
        recipe_name = input(f"Please enter the Recipe name: ")
        title = "recipe"
        

        new_recipe = []
        new_recipe_dict = {}
        new_recipe_dict.update({title: recipe_name})

        while True:
            
            item_input= input(f"Please enter an item to add to the recipe: ")
            
            recipe_book.append(new_recipe_dict)
            
            amount_input = input("Enter the amount & measurement of the item. ie; 1-9, - cups, teaspoons, tablespoons, ect: ")
             
            ingredient = {"ingredient": item_input, "amount": amount_input}
            new_recipe.append(ingredient)
            new_recipe_dict[item_input] = amount_input
            another_item = input(f"would you like to enter another item, 'y', 'n' ?")
            if another_item == 'y':
                True
            if another_item == 'n':
                recipe_book.append(new_recipe_dict)
                with open(f'data/recipes/{recipe_name}.csv', 'w') as f:
                    fieldnames = ["ingredient", "amount"]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for l in new_recipe:
                        writer.writerow(l)
                        break
            
    elif user_choice == "3":
        recipe_to_remove = input(f"What recipe would you like to remove: ")
        
        if os.path.exists(f"data/recipes/{recipe_to_remove}.csv"):
            os.remove(f"data/recipes/{recipe_to_remove}.csv")
            #recipe_book.remove(recipe_to_remove)
        else:
            print("The file does not exist")

    


    elif user_choice == "4":
        search_choice  = input(f"Would you like 1 recipe or mulitple? ")
        if search_choice == "1":
            test()
        if search_choice == "multiple":
            test_2()

        
    elif user_choice == "5":
   
        print(F'Thanks for cooking with us!')    
        break
    
                
    
    

