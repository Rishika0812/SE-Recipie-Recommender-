import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Recipe Collection",
    page_icon="🍳",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Check for API key
if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY not found in environment variables. Please check your .env file.")
    st.stop()

# Initialize Groq client (if needed in this file)
try:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    client = Groq()  # Ensure no unsupported arguments are passed
    client.api_key = api_key  # Set the API key separately
except ImportError:
    st.error("Groq module not found. Please ensure it is installed.")
    client = None
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")
    client = None

# Import other modules after environment setup
from auth import login, signup
from chatbot import initialize_chatbot, get_chatbot_response
from docs import show_documentation
from utils import initialize_user_data_file

# Initialize user data file
initialize_user_data_file()

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Login"
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = initialize_chatbot()
if 'favorite_recipes' not in st.session_state:
    st.session_state.favorite_recipes = set()
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []
if 'meal_plan' not in st.session_state:
    st.session_state.meal_plan = pd.DataFrame(columns=['date', 'meal'])
if 'category' not in st.session_state:
    st.session_state.category = None

def switch_tab(tab_name):
    st.session_state.current_tab = tab_name

def main():
    st.title("🍳 Recipe Collection")
    
    # Sidebar for navigation
    with st.sidebar:
        st.header("Navigation")
        if not st.session_state.logged_in:
            st.session_state.current_tab = st.radio(
                "Choose an option:",
                ["Login", "Sign Up"],
                key="nav_radio_logged_out",
                index=0 if st.session_state.current_tab == "Login" else 1
            )
        else:
            st.session_state.current_tab = st.radio(
                "Choose an option:",
                ["Home", "My Favorites", "Shopping List", "Meal Planner", "Chatbot", "Documentation"],
                key="nav_radio_logged_in"
            )
            if st.button("Logout", key="logout_button"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.session_state.current_tab = "Login"
                st.rerun()
    
    # Main content area
    if not st.session_state.logged_in:
        if st.session_state.current_tab == "Login":
            login()
        else:
            signup()
    else:
        if st.session_state.current_tab == "Home":
            show_home()
        elif st.session_state.current_tab == "My Favorites":
            show_favorites()
        elif st.session_state.current_tab == "Shopping List":
            show_shopping_list()
        elif st.session_state.current_tab == "Meal Planner":
            show_meal_planner()
        elif st.session_state.current_tab == "Chatbot":
            show_chatbot()
        else:
            show_documentation()

def show_home():
    st.header(f"Welcome, {st.session_state.username}!")
    
    # Search and filter section
    st.subheader("🔍 Search & Filter")
    col1, col2, col3 = st.columns(3)
    with col1:
        search_query = st.text_input("Search recipes", "")
    with col2:
        cuisine_filter = st.selectbox(
            "Filter by cuisine",
            ["All", "Italian", "Indian", "Japanese", "French", "Mexican", "Chinese"]
        )
    with col3:
        time_filter = st.selectbox(
            "Filter by cooking time",
            ["All", "Quick (< 30 mins)", "Medium (30-60 mins)", "Long (> 60 mins)"]
        )
    
    st.divider()
    
    # Recipe Categories
    st.subheader("📑 Recipe Categories")
    category_cols = st.columns(4)
    with category_cols[0]:
        if st.button("🥗 Vegetarian"):
            st.session_state.category = "vegetarian"
    with category_cols[1]:
        if st.button("🍖 Non-Vegetarian"):
            st.session_state.category = "non-vegetarian"
    with category_cols[2]:
        if st.button("🍰 Desserts"):
            st.session_state.category = "desserts"
    with category_cols[3]:
        if st.button("🥪 Quick Meals"):
            st.session_state.category = "quick-meals"
            
    st.divider()
    
    # Featured Recipes
    st.subheader("⭐ Featured Recipes")
    st.write("Here are some of the most popular recipes from around the world:")
    
    # Famous recipes data
    famous_recipes = [
        {
            "name": "Classic Margherita Pizza",
            "cuisine": "Italian",
            "category": "vegetarian",
            "rating": 4.8,
            "difficulty": "Medium",
            "ingredients": """
            - 2 1/4 cups all-purpose flour
            - 1 tsp active dry yeast
            - 1 cup warm water
            - 1 tsp salt
            - 1 tbsp olive oil
            - 1 cup tomato sauce
            - 8 oz fresh mozzarella
            - Fresh basil leaves
            - Extra virgin olive oil
            """,
            "instructions": """
            1. Mix flour, yeast, and salt in a bowl
            2. Add warm water and olive oil, knead for 10 minutes
            3. Let dough rise for 2 hours
            4. Roll out dough and add toppings
            5. Bake at 450°F for 15-20 minutes
            """,
            "cooking_time": "2 hours 30 minutes",
            "nutrition": {
                "calories": 250,
                "protein": 10,
                "carbs": 30,
                "fat": 8
            }
        },
        {
            "name": "Butter Chicken",
            "cuisine": "Indian",
            "category": "non-vegetarian",
            "rating": 4.9,
            "difficulty": "Medium",
            "ingredients": """
            - 2 lbs chicken thighs
            - 1 cup yogurt
            - 2 tbsp ginger-garlic paste
            - 2 tsp garam masala
            - 1 tsp turmeric
            - 2 cups tomato sauce
            - 1 cup heavy cream
            - 4 tbsp butter
            - Fresh cilantro
            """,
            "instructions": """
            1. Marinate chicken in yogurt and spices
            2. Cook chicken until golden
            3. Prepare sauce with tomatoes and cream
            4. Combine chicken and sauce
            5. Garnish with cilantro
            """,
            "cooking_time": "1 hour",
            "nutrition": {
                "calories": 450,
                "protein": 35,
                "carbs": 12,
                "fat": 28
            }
        },
        {
            "name": "Sushi Roll",
            "cuisine": "Japanese",
            "category": "non-vegetarian",
            "rating": 4.7,
            "difficulty": "Hard",
            "ingredients": """
            - 2 cups sushi rice
            - 4 sheets nori
            - 1 avocado
            - 1 cucumber
            - 8 oz fresh tuna
            - Soy sauce
            - Wasabi
            - Pickled ginger
            """,
            "instructions": """
            1. Cook sushi rice with vinegar
            2. Lay nori sheet on bamboo mat
            3. Spread rice and add fillings
            4. Roll tightly using the mat
            5. Slice into pieces
            """,
            "cooking_time": "1 hour",
            "nutrition": {
                "calories": 320,
                "protein": 18,
                "carbs": 45,
                "fat": 9
            }
        },
        {
            "name": "Chocolate Lava Cake",
            "cuisine": "French",
            "category": "desserts",
            "rating": 4.9,
            "difficulty": "Medium",
            "ingredients": """
            - 6 oz dark chocolate
            - 6 oz butter
            - 3 eggs
            - 3 egg yolks
            - 1/2 cup sugar
            - 1/4 cup flour
            - Vanilla extract
            - Powdered sugar
            """,
            "instructions": """
            1. Melt chocolate and butter
            2. Mix eggs, sugar, and flour
            3. Combine all ingredients
            4. Pour into ramekins
            5. Bake at 400°F for 12 minutes
            """,
            "cooking_time": "30 minutes",
            "nutrition": {
                "calories": 380,
                "protein": 6,
                "carbs": 35,
                "fat": 24
            }
        }
    ]
    
    # Filter recipes based on user input
    filtered_recipes = famous_recipes
    if search_query:
        filtered_recipes = [r for r in filtered_recipes if search_query.lower() in r['name'].lower()]
    if cuisine_filter != "All":
        filtered_recipes = [r for r in filtered_recipes if r['cuisine'] == cuisine_filter]
    if time_filter != "All":
        if time_filter == "Quick (< 30 mins)":
            filtered_recipes = [r for r in filtered_recipes if "minutes" in r['cooking_time'] and int(r['cooking_time'].split()[0]) <= 30]
        elif time_filter == "Medium (30-60 mins)":
            filtered_recipes = [r for r in filtered_recipes if ("hour" in r['cooking_time'] and int(r['cooking_time'].split()[0]) == 1) or 
                              ("minutes" in r['cooking_time'] and 30 < int(r['cooking_time'].split()[0]) <= 60)]
        else:
            filtered_recipes = [r for r in filtered_recipes if "hour" in r['cooking_time'] and int(r['cooking_time'].split()[0]) > 1]
    
    # Display recipes in a grid
    if not filtered_recipes:
        st.info("No recipes found matching your criteria.")
    else:
        col1, col2 = st.columns(2)
        for i, recipe in enumerate(filtered_recipes):
            with col1 if i % 2 == 0 else col2:
                with st.expander(f"{recipe['name']} ({recipe['cuisine']})", expanded=i==0):
                    # Recipe header
                    col_a, col_b, col_c = st.columns([2,2,1])
                    with col_a:
                        st.write(f"⭐ Rating: {recipe['rating']}/5.0")
                    with col_b:
                        st.write(f"🔨 Difficulty: {recipe['difficulty']}")
                    with col_c:
                        if recipe['name'] in st.session_state.favorite_recipes:
                            if st.button("❤️", key=f"fav_{recipe['name']}"):
                                st.session_state.favorite_recipes.remove(recipe['name'])
                        else:
                            if st.button("🤍", key=f"fav_{recipe['name']}"):
                                st.session_state.favorite_recipes.add(recipe['name'])
                    
                    # Recipe content
                    st.write("**Ingredients:**")
                    st.write(recipe['ingredients'])
                    st.write("**Instructions:**")
                    st.write(recipe['instructions'])
                    st.write(f"**Cooking Time:** {recipe['cooking_time']}")
                    
                    # Nutrition information
                    st.write("**Nutrition Information:**")
                    nutrition_cols = st.columns(4)
                    with nutrition_cols[0]:
                        st.metric("Calories", f"{recipe['nutrition']['calories']} kcal")
                    with nutrition_cols[1]:
                        st.metric("Protein", f"{recipe['nutrition']['protein']}g")
                    with nutrition_cols[2]:
                        st.metric("Carbs", f"{recipe['nutrition']['carbs']}g")
                    with nutrition_cols[3]:
                        st.metric("Fat", f"{recipe['nutrition']['fat']}g")
                    
                    # Action buttons
                    col_x, col_y = st.columns(2)
                    with col_x:
                        if st.button("🛒 Add to Shopping List", key=f"shop_{recipe['name']}"):
                            ingredients = [ing.strip() for ing in recipe['ingredients'].split('\n') if ing.strip() and ing.strip().startswith('-')]
                            st.session_state.shopping_list.extend(ingredients)
                            st.success("Added to shopping list!")
                    with col_y:
                        if st.button("📅 Add to Meal Planner", key=f"plan_{recipe['name']}"):
                            new_meal = pd.DataFrame([{
                                'date': datetime.today().strftime('%Y-%m-%d'),
                                'meal': recipe['name']
                            }])
                            st.session_state.meal_plan = pd.concat([st.session_state.meal_plan, new_meal], ignore_index=True)
                            st.success("Added to meal planner!")

def show_favorites():
    st.header("❤️ My Favorite Recipes")
    if not st.session_state.favorite_recipes:
        st.info("You haven't added any recipes to your favorites yet.")
    else:
        for recipe_name in st.session_state.favorite_recipes:
            st.write(f"- {recipe_name}")

def show_shopping_list():
    st.header("🛒 Shopping List")
    if not st.session_state.shopping_list:
        st.info("Your shopping list is empty.")
    else:
        for item in st.session_state.shopping_list:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(item)
            with col2:
                if st.button("✅", key=f"remove_{item}"):
                    st.session_state.shopping_list.remove(item)
                    st.rerun()

def show_meal_planner():
    st.header("📅 Meal Planner")
    
    # Add new meal
    with st.form("add_meal"):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("Date")
        with col2:
            meal = st.text_input("Meal")
        if st.form_submit_button("Add to Plan"):
            new_meal = pd.DataFrame([{
                'date': date.strftime('%Y-%m-%d'),
                'meal': meal
            }])
            st.session_state.meal_plan = pd.concat([st.session_state.meal_plan, new_meal], ignore_index=True)
    
    # Display meal plan
    if st.session_state.meal_plan.empty:
        st.info("No meals planned yet.")
    else:
        st.dataframe(st.session_state.meal_plan.sort_values('date'))

def show_chatbot():
    st.header("👩‍🍳 Recipe Chatbot")
    st.write("Ask me anything about recipes, cooking techniques, or ingredients!")
    
    try:
        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask a question about recipes...", key="chat_input"):
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)
            
            # Get and display assistant response
            response = get_chatbot_response(prompt, st.session_state.chatbot)
            if response:
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.write(response)
    except Exception as e:
        st.error(f"Error in chatbot: {e}")

if __name__ == "__main__":
    main()