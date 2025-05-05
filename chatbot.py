import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client with error handling
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

def initialize_chatbot():
    """Initialize the chatbot with system message"""
    return {
        "messages": [
            {
                "role": "system",
                "content": """You are a helpful cooking assistant that can:
                1. Suggest recipes based on ingredients
                2. Explain cooking techniques
                3. Provide ingredient substitutions
                4. Answer general cooking questions
                5. Give cooking tips and advice
                
                Always provide detailed, accurate, and helpful responses."""
            }
        ]
    }

def get_chatbot_response(user_input, chatbot_state):
    """Get response from the chatbot using Groq model"""
    if client is None:
        st.error("Groq client not initialized. Please check your API key.")
        return "I apologize, but I'm having trouble connecting to the AI service."
        
    try:
        # Add user message to chat history
        chatbot_state["messages"].append({"role": "user", "content": user_input})
        
        # Get response from Groq model
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Updated model name
            messages=chatbot_state["messages"],
            temperature=0.7,
            max_tokens=1000,
            top_p=0.9,
            presence_penalty=0.1
        )
        
        # Extract and store the response
        response = completion.choices[0].message.content
        chatbot_state["messages"].append({"role": "assistant", "content": response})
        
        return response
        
    except Exception as e:
        if "model_decommissioned" in str(e) or "model_not_found" in str(e):
            st.error("The selected model is unavailable. Please update to a supported model.")
        else:
            st.error(f"Error getting chatbot response: {e}")
        return "I apologize, but I'm having trouble processing your request. Please try again."

def get_user_recommendations(user_details):
    """Get personalized recommendations for the user using Groq LLM."""
    if client is None:
        st.error("Groq client not initialized. Please check your API key.")
        return []

    try:
        # Create a prompt using user details
        prompt = f"""Based on the following user details, provide 3 personalized recipe recommendations:
        - Favorite cuisine: {user_details['favorite_cuisine']}
        - Dietary restrictions: {user_details['dietary_restrictions']}
        - Preferred ingredients: {user_details['preferred_ingredients']}
        - Ingredients to avoid: {user_details['ingredients_to_avoid']}
        - Cooking skill: {user_details['cooking_skill']}
        - Favorite meal: {user_details['favorite_meal']}
        - Spice level: {user_details['spice_level']}
        - Cooking time preference: {user_details['cooking_time_preference']}
        
        For each recipe, include:
        1. Recipe name
        2. List of ingredients
        3. Step-by-step instructions
        4. Estimated cooking time
        """

        # Send the prompt to the Groq LLM
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        # Parse the response
        response_text = completion.choices[0].message.content
        recommendations = parse_llama_response(response_text)
        return recommendations

    except Exception as e:
        st.error(f"Error getting recommendations: {e}")
        return []