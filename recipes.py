import requests
import json
import pandas as pd


def get_recipe(recipe, diet, ingredients):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    querystring = {"query": "{}".format(recipe), "diet": "{}".format(diet),
                   "excludeIngredients": "{}".format(ingredients), "number": "100"}

    headers = {
        "X-RapidAPI-Key": "84e3b5a6f6mshfa61e64adee66a3p1c8d48jsn7f6087e0f0cd",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    df = pd.DataFrame(response.json().get('results'))
    print(df.loc[:, ~df.columns.isin(['id', 'imageType'])].to_markdown(tablefmt="orgtbl"))

    id = input("\nEnter the index of the item you wish to make: ")

    return int(df['id'].values[int(id)])


def get_meal(meal):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/analyzedInstructions".format(meal)

    querystring = {"stepBreakdown": "true"}

    headers = {
        "X-RapidAPI-Key": "84e3b5a6f6mshfa61e64adee66a3p1c8d48jsn7f6087e0f0cd",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))


def main():
    inpt = input("Welcome to the recipe searcher! Type 'help' for a list of commands; otherwise, "
                 "press enter to continue . . . ")
    if inpt == 'help':
        print("Recipe - The recipe you would like to search.\n"
              "Diet - The diet to which the recipes must be compliant. Possible values are: pescetarian, "
              "lacto vegetarian, ovo vegetarian, vegan, paleo, primal, and vegetarian.\n"
              "Ingredient - An comma-separated list of ingredients that must not be contained in the recipes.")
    recipe = input("Enter a recipe: ")
    diet = input("Choose a diet: ")
    ingredients = input("Exclude ingredients: ")
    meal = get_recipe(recipe, diet, ingredients)
    get_meal(meal)


if __name__ == '__main__':
    main()
