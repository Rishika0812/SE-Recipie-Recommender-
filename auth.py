import streamlit as st
import pandas as pd
import os

# Constants for user data storage
USER_DATA_FILE = "user_data.csv"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        return pd.read_csv(USER_DATA_FILE)
    return pd.DataFrame(columns=[
        'username', 'password', 'favorite_cuisine', 'dietary_restrictions',
        'preferred_ingredients', 'ingredients_to_avoid', 'cooking_skill',
        'favorite_meal', 'spice_level', 'cooking_time_preference'
    ])

def save_user_data(df):
    df.to_csv(USER_DATA_FILE, index=False)

def login():
    st.subheader("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user_data = load_user_data()
        user = user_data[(user_data['username'] == username) & (user_data['password'] == password)]
        
        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

def signup():
    st.subheader("Sign Up")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    # Collect user preferences in a form to prevent premature resets
    with st.form("signup_form"):
        favorite_cuisine = st.selectbox(
            "Favorite cuisine",
            ["Italian", "Indian", "Mexican", "Chinese", "Japanese", "Mediterranean", "Other"]
        )
        
        dietary_restrictions = st.multiselect(
            "Dietary restrictions",
            ["None", "Vegetarian", "Vegan", "Gluten-free", "Dairy-free", "Nut-free"]
        )
        
        preferred_ingredients = st.text_input(
            "Preferred ingredients (comma-separated)",
            "e.g., chicken, rice, vegetables"
        )
        
        ingredients_to_avoid = st.text_input(
            "Ingredients to avoid (comma-separated)",
            "e.g., nuts, shellfish"
        )
        
        cooking_skill = st.selectbox(
            "Cooking skill level",
            ["Beginner", "Intermediate", "Expert"]
        )
        
        favorite_meal = st.selectbox(
            "Favorite type of meal",
            ["Breakfast", "Lunch", "Dinner", "Snacks"]
        )
        
        spice_level = st.selectbox(
            "Preferred spice level",
            ["Mild", "Medium", "Spicy"]
        )
        
        cooking_time = st.selectbox(
            "Preferred cooking time",
            ["Quick (<20 mins)", "Moderate (20-40 mins)", "Elaborate (>40 mins)"]
        )
        
        # Submit button for the form
        create_account = st.form_submit_button("Create Account")
    
    if create_account:
        if password != confirm_password:
            st.error("Passwords do not match!")
            return
        
        user_data = load_user_data()
        if username in user_data['username'].values:
            st.error("Username already exists!")
            return
        
        # Save user data
        new_user = pd.DataFrame([{
            'username': username,
            'password': password,
            'favorite_cuisine': favorite_cuisine,
            'dietary_restrictions': ','.join(dietary_restrictions),
            'preferred_ingredients': preferred_ingredients,
            'ingredients_to_avoid': ingredients_to_avoid,
            'cooking_skill': cooking_skill,
            'favorite_meal': favorite_meal,
            'spice_level': spice_level,
            'cooking_time_preference': cooking_time
        }])
        
        user_data = pd.concat([user_data, new_user], ignore_index=True)
        save_user_data(user_data)
        
        st.success("Account created successfully! Please login.")
        st.session_state.logged_in = False  # Ensure user is logged out
        st.experimental_rerun()  # Redirect to login page