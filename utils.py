import pandas as pd
import os

def ensure_data_directory():
    """Ensure the data directory exists"""
    if not os.path.exists('data'):
        os.makedirs('data')

def load_csv_file(filepath):
    """Load a CSV file and return as DataFrame"""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return pd.DataFrame()

def save_csv_file(df, filepath):
    """Save DataFrame to CSV file"""
    try:
        df.to_csv(filepath, index=False)
        return True
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return False

def validate_user_input(input_data):
    """Validate user input data"""
    required_fields = [
        'username', 'password', 'favorite_cuisine', 'dietary_restrictions',
        'preferred_ingredients', 'ingredients_to_avoid', 'cooking_skill',
        'favorite_meal', 'spice_level', 'cooking_time_preference'
    ]
    
    for field in required_fields:
        if field not in input_data or not input_data[field]:
            return False, f"Missing required field: {field}"
    
    return True, "Input validation successful"

def format_recipe_display(recipe):
    """Format recipe data for display"""
    return {
        'name': recipe.get('name', ''),
        'ingredients': recipe.get('ingredients', ''),
        'instructions': recipe.get('instructions', ''),
        'cooking_time': recipe.get('cooking_time', '')
    }

def initialize_user_data_file():
    """Initialize the user_data.csv file if it does not exist"""
    if not os.path.exists("user_data.csv"):
        df = pd.DataFrame(columns=[
            'username', 'password', 'favorite_cuisine', 'dietary_restrictions',
            'preferred_ingredients', 'ingredients_to_avoid', 'cooking_skill',
            'favorite_meal', 'spice_level', 'cooking_time_preference'
        ])
        df.to_csv("user_data.csv", index=False)