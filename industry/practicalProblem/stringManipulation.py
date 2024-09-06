def get_grocery_list(bros_recipe: str, ingredients_at_home:dict):
    strList=bros_recipe.split()
    valueList=[]
    keyList=[]
    groceryDict={}
    recipeDict={}

    for ingredient in strList:
        if ingredient.isdigit():
            valueList.append(int(ingredient))
        else:
            keyList.append(ingredient.lower())
    for ingredient, needed_quantity in recipeDict.items():
        ingredient_lower = ingredient.lower()  # For case-insensitive matching
        if ingredient_lower in ingredients_at_home:
            available_quantity = ingredients_at_home.get(ingredient_lower)
            if needed_quantity > available_quantity:
                groceryDict[ingredient_lower] = needed_quantity - available_quantity
        else:
            # If the ingredient is not at home, add the full required amount to the grocery list
            groceryDict[ingredient_lower] = needed_quantity

    return groceryDict


# Test Case 2: No ingredients at home

recipe_3 = "4 8 1 10 2 bUtTeR hIcKoRyWoOdChIpS pApRiKa BeEfBrIsKeT bRoWnSuGaR"
home_3 = {"sAlT": 1, "pEPper": 1, "paPRika": 1, "bUTteR": 2}
grocery_list_3 = {"beefbrisket": 10, "brownsugar": 2, "hickorywoodchips": 8, "butter": 2}
print(get_grocery_list(recipe_3, home_3) == grocery_list_3)

# Test Case 4: All ingredients at home
recipe_4 = "2 4 1 2 2 BuTtEr SaLmOnFiLlEtS lEmOn OrEgAnO pArSlEy"
home_4 = {"butTer": 2, "saLmoNfiLLets": 4, "leMOn": 1, "oREGano": 2, "pARsLey": 2}
grocery_list_4 = {}
print(get_grocery_list(recipe_4, home_4) == grocery_list_4)        
recipe_3 = "4 8 1 10 2 bUtTeR hIcKoRyWoOdChIpS pApRiKa BeEfBrIsKeT bRoWnSuGaR"
home_3 = {"sAlT": 1, "pEPper": 1, "paPRika": 1, "bUTteR": 2}
grocery_list_3 = {"beefbrisket": 10, "brownsugar": 2, "hickorywoodchips": 8, "butter": 2}



