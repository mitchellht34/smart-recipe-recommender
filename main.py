import pandas as pd
import ast  # To parse the ingredient strings

df = pd.read_csv('data/recipes.csv')

# print(df.columns)
# print(df.head())

# Clean and parse ingredients column
def safe_parse_ingredients(x):
    try:
        # Ignore "character(0)" or empty
        if 'character(0' in x or x.strip() == '':
            return []
        # Replace c(...) with [...] and parse
        return ast.literal_eval(x.replace('c(', '[').replace(')', ']'))
    except Exception as e:
        print(f"Error parsing row: {e}, value: {x}")
        return []

df['ParsedIngredients'] = df['RecipeIngredientParts'].apply(safe_parse_ingredients)


print(df[['Name', 'ParsedIngredients']].head())

