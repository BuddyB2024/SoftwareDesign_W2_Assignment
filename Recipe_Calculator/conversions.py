# conversions.py
""" 
This module contains functions for unit conversions used in the Recipe Calculator program.
available conversions:
- Volume conversions: cups to milliliters, milliliters to cups, teaspoons to milliliters, milliliters to teaspoons,
  tablespoons to milliliters, milliliters to tablespoons
- Weight conversions: ounces to grams, grams to ounces, pounds to grams, grams to pounds
- Ingredient-specific conversions: cups to grams and grams to cups for common ingredients
- Teaspoons and tablespoons to grams conversions
"""
# Volume conversions
def cups_to_milliliters(cups):
    return cups * 240

def milliliters_to_cups(ml):
    return ml / 240

def teaspoons_to_milliliters(teaspoons):
    return teaspoons * 5

def milliliters_to_teaspoons(ml):
    return ml / 5

def tablespoons_to_milliliters(tablespoons):
    return tablespoons * 15

def milliliters_to_tablespoons(ml):
    return ml / 15  


# Weight conversions
def ounces_to_grams(ounces):
    return ounces * 28.35

def grams_to_ounces(grams):
    return grams / 28.35

def pounds_to_grams(pounds):
    return pounds * 454

def grams_to_pounds(grams):
    return grams / 454

# Ingredient-specific conversions: cups to grams and grams to cups
# Conversion factors for common ingredients (e.g., flour, sugar) from cups to grams

CONVERSION_FACTORS = {
    'flour': 125,          # 1 cup of flour ≈ 125 grams
    'sugar': 200,          # 1 cup of granulated sugar ≈ 200 grams
    'brown sugar': 220,    # 1 cup of packed brown sugar ≈ 220 grams
    'powdered sugar': 120, # 1 cup of powdered sugar ≈ 120 grams
    'butter': 227,         # 1 cup of butter ≈ 227 grams
    'milk': 240,           # 1 cup of milk ≈ 240 grams
    'water': 240,          # 1 cup of water ≈ 240 grams
    'oil': 218,            # 1 cup of oil ≈ 218 grams
    'honey': 340,          # 1 cup of honey ≈ 340 grams
    'cocoa powder': 100,   # 1 cup of cocoa powder ≈ 100 grams
    'oats': 90,            # 1 cup of oats ≈ 90 grams
    'rice': 190,           # 1 cup of uncooked rice ≈ 190 grams
    'chocolate chips': 175,# 1 cup of chocolate chips ≈ 175 grams
    'peanut butter': 270,  # 1 cup of peanut butter ≈ 270 grams
    'baking powder': 4,    # 1 teaspoon of baking powder ≈ 4 grams
    'baking soda': 4,      # 1 teaspoon of baking soda ≈ 4 grams
    'salt': 6,             # 1 teaspoon of salt ≈ 6 grams
    'vanilla extract': 4,  # 1 teaspoon of vanilla extract ≈ 4 grams
    'yeast': 3,            # 1 teaspoon of yeast ≈ 3 grams
    # Add more ingredients as needed
}

# Cups to grams and grams to cups conversions
def cups_to_grams(cups, ingredient_name):
    if ingredient_name in CONVERSION_FACTORS:
        return cups * CONVERSION_FACTORS[ingredient_name]
    else:
        raise ValueError(f"No conversion factor available for {ingredient_name} from cups to grams.")

def grams_to_cups(grams, ingredient_name):
    if ingredient_name in CONVERSION_FACTORS:
        return grams / CONVERSION_FACTORS[ingredient_name]
    else:
        raise ValueError(f"No conversion factor available for {ingredient_name} from grams to cups.")

# Teaspoons and tablespoons to grams conversions
TEASPOON_TO_MILLILITER = 5
TABLESPOON_TO_MILLILITER = 15

def teaspoons_to_grams(teaspoons, ingredient_name):
    if ingredient_name in CONVERSION_FACTORS:
        grams_per_ml = CONVERSION_FACTORS[ingredient_name] / 240  # Approximate conversion: 1 cup = 240 ml
        return teaspoons * TEASPOON_TO_MILLILITER * grams_per_ml
    else:
        return teaspoons * TEASPOON_TO_MILLILITER * 1  # Default assumption: 1 gram per ml

def grams_to_teaspoons(grams, ingredient_name):
    if ingredient_name in CONVERSION_FACTORS:
        grams_per_ml = CONVERSION_FACTORS[ingredient_name] / 240
        return grams / (TEASPOON_TO_MILLILITER * grams_per_ml)
    else:
        return grams / (TEASPOON_TO_MILLILITER * 1)

def tablespoons_to_grams(tablespoons, ingredient_name):
    if ingredient_name in CONVERSION_FACTORS:
        grams_per_ml = CONVERSION_FACTORS[ingredient_name] / 240
        return tablespoons * TABLESPOON_TO_MILLILITER * grams_per_ml
    else:
        return tablespoons * TABLESPOON_TO_MILLILITER * 1

def grams_to_tablespoons(grams, ingredient_name):
    if ingredient_name in CONVERSION_FACTORS:
        grams_per_ml = CONVERSION_FACTORS[ingredient_name] / 240
        return grams / (TABLESPOON_TO_MILLILITER * grams_per_ml)
    else:
        return grams / (TABLESPOON_TO_MILLILITER * 1)
