# Smart Recipe Recommender

This project is a Python-based smart recipe recommender system.  
It suggests recipes based on ingredients the user has at home,  
helping to reduce food waste and improve meal planning.

## Features

- User inputs a list of ingredients (via command line)
- System searches for recipes that match those ingredients
- Recipes are ranked by number of matching ingredients
- Visualization of most common ingredients (bar chart)
- Visualization of top recipe categories (pie chart)
- Kaggle data is automatically downloaded using `download_data.py`

## Data

- Dataset: [Food.com Recipes and Reviews](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews)

## Setup

1. Install dependencies:

    ```bash
    pip install pandas matplotlib kaggle
    ```

2. Set up your Kaggle API token:

    - Download your `kaggle.json` token from Kaggle account > API  
    - Place it in:  
      `~/.kaggle/kaggle.json` (Linux/Mac)  
      `%USERPROFILE%\.kaggle\kaggle.json` (Windows)

3. Download data:

    ```bash
    python download_data.py
    ```

4. Run the recommender:

    ```bash
    python main.py
    ```

5. Enter ingredients when prompted:

    ```text
    Enter ingredients (comma separated): chicken, garlic, onion
    ```

6. View top matching recipes and charts.
