
"""
Class_Ingredient.py

Attributes: name, amount, unit, price, precision
Methods: __init__, get_name, set_name, get_amount, 
        set_amount, get_unit, set_unit, get_price, 
        set_price, calculate_cost, calculate_amount,
        convert_unit, print_ingredient

The Ingredient class represents an ingredient with a name, amount, unit, and price. It has methods to calculate the cost
and amount per serving, convert units, and print the ingredient details.
The precision attribute is used to round the calculated values to a specific number of decimal places.
The convert_unit method converts the ingredient amount to metric or standard units based on the unit type.
The print_ingredient method displays the ingredient details.
The Recipe class uses the Ingredient class to create a list of ingredients for a recipe. 
It has methods to add and remove ingredients, calculate the total cost and amount of the recipe, and print the recipe details.
The set_servings method adjusts the amount of each ingredient based on the new number of servings.

"""

from conversions import (
    cups_to_grams, grams_to_cups, cups_to_milliliters, milliliters_to_cups,
    ounces_to_grams, grams_to_ounces, pounds_to_grams, grams_to_pounds,
    teaspoons_to_grams, grams_to_teaspoons, tablespoons_to_grams, grams_to_tablespoons,
    tablespoons_to_milliliters, milliliters_to_tablespoons, teaspoons_to_milliliters, milliliters_to_teaspoons,
    CONVERSION_FACTORS
)

class Ingredient:
    """ 
    A class to represent an ingredient with its name, amount, unit, and price.

    Attributes:
        precision (int): The precision used for rounding numerical values, defaulting to 2 decimal places.
        name (str): The name of the ingredient (e.g., 'flour', 'sugar').
        amount (float): The quantity of the ingredient.
        unit (str): The unit of measurement for the ingredient (e.g., 'cups', 'grams').
        price (float): The price per unit of the ingredient.
        original_amount (float): The original amount of the ingredient, used for cost calculations.
        original_unit (str): The original unit of measurement of the ingredient, used for cost calculations.
    """

    precision = 2  # Define precision as a class-level attribute


    def __init__(self, name, amount, unit, price, precision=None):
        self.name = name
        self.amount = amount
        self.unit = unit.lower()
        self.price = price
        # Use specific precision if provided, otherwise use the class default
        self.precision = precision if precision is not None else Ingredient.precision
        # Store original amount and unit to use for cost calculation
        self.original_amount = amount
        self.original_unit = unit.lower()
        self.price_per_original_unit = price / amount  # Calculate price per original unit

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_unit(self):
        return self.unit

    def set_unit(self, unit):
        self.unit = unit.lower()

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def calculate_cost(self):
        """
        Calculates the cost based on the adjusted amount and the original unit price.
        Ensures that the cost calculation reflects any changes in measurement units.
        """
        # Calculate the adjusted cost using the original price per unit
        adjusted_cost = self.price_per_original_unit * self.amount
        return round(adjusted_cost, self.precision)

    def calculate_amount(self, servings):
        # Divide the original amount by servings for the amount per serving
        return round(self.original_amount / servings, self.precision)

    def convert_unit(self, to_metric=True):
        print(f"Converting {self.name}: {self.amount} {self.unit} {'to metric' if to_metric else 'to standard'}")

        if to_metric:
            if self.unit in ['cups', 'cup']:
                if self.name in CONVERSION_FACTORS:
                    self.amount = round(cups_to_grams(self.amount, self.name), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / cups_to_grams(1, self.name)
                else:
                    self.amount = round(cups_to_milliliters(self.amount), self.precision)
                    self.unit = 'milliliters'
                    self.price_per_original_unit = self.price / cups_to_milliliters(1)
            elif self.unit in ['tablespoons', 'tbsp', 'tablespoon']:
                if self.name in CONVERSION_FACTORS:
                    self.amount = round(tablespoons_to_grams(self.amount, self.name), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / tablespoons_to_grams(1, self.name)
                else:
                    self.amount = round(tablespoons_to_milliliters(self.amount), self.precision)
                    self.unit = 'milliliters'
                    self.price_per_original_unit = self.price / tablespoons_to_milliliters(1)
            elif self.unit in ['teaspoons', 'teaspoon', 'tsp']:
                if self.name in CONVERSION_FACTORS:
                    self.amount = round(teaspoons_to_grams(self.amount, self.name), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / teaspoons_to_grams(1, self.name)

                else:
                    self.amount = round(teaspoons_to_milliliters(self.amount), self.precision)
                    self.unit = 'milliliters'
                    self.price_per_original_unit = self.price / teaspoons_to_milliliters(1)
            elif self.unit in ['ounces', 'oz']:
                if self.name in CONVERSION_FACTORS:
                    self.amount = round(ounces_to_grams(self.amount), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / ounces_to_grams(1)
                else:
                    self.amount = round(ounces_to_grams(self.amount), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / ounces_to_grams(1)

            elif self.unit in ['pounds', 'lb']:
                if self.name in CONVERSION_FACTORS:
                    self.amount = round(pounds_to_grams(self.amount), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / pounds_to_grams(1)
                else:
                    self.amount = round(pounds_to_grams(self.amount), self.precision)
                    self.unit = 'grams'
                    self.price_per_original_unit = self.price / pounds_to_grams(1)
            elif self.unit == 'milliliters':
                pass  # Already metric
            elif self.unit == 'grams':
                pass  # Already metric
            else:
                print(f"Unhandled unit '{self.unit}' for '{self.name}'. Assuming no conversion needed.")
        else:
            if self.unit in ['grams', 'gram']:
                if self.name in CONVERSION_FACTORS:
                    self.amount = round(grams_to_cups(self.amount, self.name), self.precision)
                    self.unit = 'cups'
                else:
                    self.amount = round(grams_to_ounces(self.amount), self.precision)
                    self.unit = 'ounces'
            elif self.unit in ['milliliters', 'milliliter', 'ml']:
                self.amount = round(milliliters_to_cups(self.amount), self.precision)
                self.unit = 'cups'
                print(f"Unhandled unit '{self.unit}' for '{self.name}' in standard conversion.")
    
    def print_ingredient(self):
        # Display the name, adjusted amount, unit, and adjusted cost
        adjusted_cost = self.calculate_cost()
        print(f'{self.name}: {round(self.amount, self.precision)} {self.unit} - ${adjusted_cost}')
