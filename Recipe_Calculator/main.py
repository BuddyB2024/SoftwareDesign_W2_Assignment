# this program is a recipe calculator that takes in a recipe and the number of servings and calculates 
# the amount of ingredients needed. It also allows the user to convert the units of measurement between
# standard and metric systems. The program uses two classes, Ingredient and Recipe, to represent the
# ingredients and the recipe, respectively. The Ingredient class contains attributes for the name, amount,
# unit, and price of an ingredient, as well as methods for converting units and printing the ingredient details.
# The Recipe class contains attributes for the name, servings, and list of ingredients in a recipe, as well as
# methods for adding and removing ingredients, calculating the total cost and amount of the recipe, and printing
# the recipe details. The program also includes a main function that creates a list of ingredients, adds them to
# a recipe, prints the recipe details, converts the units of measurement, adjusts the servings, and prints the updated recipe details.

# Recipe Calculator






from Class_Ingredient import Ingredient
from Class_Recipe import Recipe

def main():
    ingredients = [
        Ingredient("flour", 2, "cups", 1.99),
        Ingredient("sugar", 1, "cup", 2.99),
        Ingredient("butter", 1, "cup", 3.99),
        Ingredient("eggs", 2, "large", 0.99),
        Ingredient("vanilla extract", 1, "tsp", 0.50),
        Ingredient("baking powder", 1, "tsp", 0.25),
        Ingredient("salt", 1, "tsp", 0.10),
        Ingredient("milk", 1, "cup", 1.99),
        Ingredient("chocolate chips", 1, "cup", 2.99),
    ]

    recipe = Recipe("Chocolate Chip Cookies", 24)

    for ingredient in ingredients:
        recipe.add_ingredient(ingredient)

    recipe.print_recipe()

    # Remove the salt ingredient by finding it in the list
    salt_to_remove = next((ing for ing in recipe.ingredients if ing.name == "salt"), None)
    if salt_to_remove:
        recipe.remove_ingredient(salt_to_remove)
        print("\nRemoved salt from the recipe:")
        recipe.print_recipe()
    else:
        print("Salt was not found in the recipe.")

    # Add garlic to the recipe
    garlic = Ingredient("garlic", 2, "cloves", 0.25)
    recipe.add_ingredient(garlic)
    print("\nAdded garlic to the recipe:")
    recipe.print_recipe()

    servings = int(input("Enter the number of servings: "))
    recipe.set_servings(servings)

    recipe.print_recipe()

    measurement_system = input("Do you want to convert to metric (m) or standard (s)? ").lower()
    if measurement_system == 'm':
        recipe.convert_units(to_metric=True)
        print("Converted to metric:")
    elif measurement_system == 's':
        recipe.convert_units(to_metric=False)
        print("Converted to standard:")

    recipe.print_recipe()


if __name__ == "__main__":
    main()
