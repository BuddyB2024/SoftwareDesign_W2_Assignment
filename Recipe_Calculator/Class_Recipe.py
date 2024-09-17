# This file contains the Recipe class, which represents a recipe containing multiple ingredients.





from Class_Ingredient import Ingredient


class Recipe:
    """
    A class to represent a recipe containing multiple ingredients.

    Attributes:
        name (str): The name of the recipe (e.g., 'Chocolate Chip Cookies').
        servings (int): The number of servings the recipe is intended to make.
        ingredients (list): A list of Ingredient objects that make up the recipe.
    """

    def __init__(self, name, servings):
        self.name = name
        self.servings = servings
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def calculate_cost(self):
        # Calculate the total cost by summing the costs of each ingredient
        total_cost = sum(ingredient.calculate_cost() for ingredient in self.ingredients)
        return round(total_cost, 2)  # Rounding to 2 decimal places for display

    def calculate_amount(self):
        # Calculate the total amount based on servings
        total_amount = sum(ingredient.calculate_amount(self.servings) for ingredient in self.ingredients)
        return total_amount

    def print_recipe(self):
        print(f"--------------------------")
        print(f"Recipe: {self.name}")
        print(f"Servings: {self.servings}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            ingredient.print_ingredient()
        print(f"Total Cost: ${self.calculate_cost()}")
        print(f"--------------------------")

        # Add the set_servings method
    def set_servings(self, new_servings):
        # Adjust the amount of each ingredient based on the new number of servings
        scale_factor = new_servings / self.servings
        for ingredient in self.ingredients:
            new_amount = ingredient.get_amount() * scale_factor
            ingredient.set_amount(new_amount)
        self.servings = new_servings
        new_cost = self.calculate_cost()

    def convert_units(self, to_metric=True, index=0):
        # Base case: If index is equal to the length of the ingredients list, stop recursion
        if index >= len(self.ingredients):
            return

        # Convert the current ingredient
        self.ingredients[index].convert_unit(to_metric)

        # Print statement for debugging to ensure each ingredient is being processed
        print(f"Converted {self.ingredients[index].name} to {'metric' if to_metric else 'standard'}: {self.ingredients[index].amount} {self.ingredients[index].unit}")

        # Recursive call to process the next ingredient
        self.convert_units(to_metric, index + 1)
