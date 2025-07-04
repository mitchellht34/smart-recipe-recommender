import pandas as pd
import ast  # To parse the ingredient strings
import matplotlib.pyplot as plt
from collections import Counter

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

# Check first few rows
print(df[['Name', 'ParsedIngredients']].head())

def find_recipes(user_ingredients, df):
    matches = []

    for i, row in df.iterrows():
        recipe_ingredients = row['ParsedIngredients']
        
        # Count how many user ingredients appear in recipe ingredients
        match_count = sum(
            any(user_ing.lower() in ing.lower() for ing in recipe_ingredients)
            for user_ing in user_ingredients
        )
        
        matches.append((row['Name'], match_count))

    # Sort recipes by match count (highest first)
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:10]  # Top 10 matches

# Example user input
# user_ingredients = ['chicken', 'garlic', 'onion']

# Ask user for ingredients
input_str = input("\nEnter ingredients (comma separated): ")
user_ingredients = [x.strip() for x in input_str.split(",")]

# Find top matching recipes
top_recipes = find_recipes(user_ingredients, df)

# Print results
print("\nTop matching recipes:")
for recipe, score in top_recipes:
    print(f"{recipe} — {score} matching ingredients")

# --- Bar Chart of Common Ingredients ---

# Flatten all ingredients into one big list
all_ingredients = [ing.lower() for sublist in df['ParsedIngredients'] for ing in sublist]

# Count frequency of each ingredient
ingredient_counts = Counter(all_ingredients)

# Get top 20 ingredients
top_ingredients = ingredient_counts.most_common(20)

# Separate into lists for plotting
ingredients, counts = zip(*top_ingredients)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(ingredients, counts)
plt.xticks(rotation=90)
plt.title("Top 20 Most Common Ingredients")
plt.ylabel("Frequency")
plt.xlabel("Ingredient")
plt.tight_layout()
plt.show()

# --- Pie Chart of Recipe Categories ---

# Count category frequencies
category_counts = df['RecipeCategory'].value_counts().head(10)  # Top 10 categories

# Plot
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 10 Recipe Categories")
plt.axis('equal')
plt.show()