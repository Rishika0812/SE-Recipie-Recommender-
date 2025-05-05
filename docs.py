import streamlit as st
import plotly.graph_objects as go

def show_documentation():
    st.title("Project Documentation")
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Requirements",
        "Use Case Diagram",
        "System Diagram",
        "Activity Diagram",
        "Class Diagram"
    ])
    
    with tab1:
        show_requirements()
    
    with tab2:
        show_use_case_diagram()
    
    with tab3:
        show_system_diagram()
    
    with tab4:
        show_activity_diagram()
    
    with tab5:
        show_class_diagram()

def show_requirements():
    st.header("Software Requirements Specification (SRS)")
    
    # Introduction
    st.subheader("1. Introduction")
    st.markdown("""
    ### 1.1 Purpose
    The purpose of this project is to develop an **AI-Based Recipe Recommendation System** using **Streamlit** for the frontend and **LLaMA 3.3-70B-Versatile** for personalized recipe suggestions and chatbot interactions. The system will provide users with personalized recipe recommendations based on their preferences and an AI-powered chatbot for recipe-related queries.

    ### 1.2 Document Conventions
    This document follows a structured approach to specifying software requirements, including:
    - **Numbered sections** for easy reference
    - **Bold headers** to highlight major components
    - **Bullet points** for clarity in listing requirements and features

    ### 1.3 Intended Audience and Reading Suggestions
    This document is intended for:
    - **Developers** building and maintaining the system
    - **Project managers** overseeing development
    - **End-users** interested in how the system functions
    - **Instructors and evaluators** assessing the project's implementation

    ### 1.4 Scope
    The project will allow users to **sign up, log in, receive personalized recipe recommendations**, and **interact with an AI chatbot**. The system will store user data in a CSV file and integrate **LLaMA 3.3-70B-Versatile** to refine recipe suggestions.
    """)
    
    # Overall Description
    st.subheader("2. Overall Description")
    st.markdown("""
    ### 2.1 Product Perspective
    This project is a standalone web-based application built using **Streamlit**. It does not depend on an existing system but integrates an external AI model (**LLaMA 3.3-70B-Versatile**) for intelligent recommendations and a **Recipe NLG dataset** for structured data retrieval.

    ### 2.2 Product Functions
    - **User Authentication:** Users can sign up and log in using a CSV-based storage system
    - **Personalized Recipe Recommendations:** AI-based filtering and enhancement of recipes
    - **Chatbot Assistance:** Users can query the chatbot for cooking-related guidance
    - **Software Engineering Documentation Page:** Displays system diagrams and project details

    ### 2.3 User Characteristics
    - **Home Cooks:** Users who want personalized recipes
    - **Food Enthusiasts:** Users interested in discovering new dishes
    - **Students & Professionals:** People looking for quick and easy cooking solutions

    ### 2.4 Constraints
    - **No password hashing:** The CSV file will store plain text passwords
    - **Dependency on LLaMA 3.3-70B-Versatile:** The AI-based suggestions rely on external API availability
    - **Dataset Limitations:** The Recipe NLG dataset may not cover all cuisines

    ### 2.5 Assumptions and Dependencies
    - Users have an internet connection to interact with the AI model
    - The dataset contains sufficient recipe diversity
    - Streamlit is properly configured to support real-time chatbot responses
    """)
    
    # Specific Requirements
    st.subheader("3. Specific Requirements")
    st.markdown("""
    ### 3.1 Functional Requirements

    #### 3.1.1 User Authentication
    - **3.1.1.1 Sign-Up**
      - **3.1.1.1.1** Users provide a username, password, and answers to 8 predefined preference questions
      - **3.1.1.1.2** User data is stored in a CSV file
    - **3.1.1.2 Login**
      - **3.1.1.2.1** Users log in using their credentials
      - **3.1.1.2.2** The system verifies username and password

    #### 3.1.2 Personalized Recipe Recommendations
    - **3.1.2.1 AI-Based Suggestions**
      - **3.1.2.1.1** The system retrieves user data from the CSV
      - **3.1.2.1.2** AI model (**LLaMA 3.3-70B-Versatile**) processes user preferences and refines recommendations
      - **3.1.2.1.3** The **Recipe NLG dataset** provides structured recipe data
    - **3.1.2.2 Recipe Details**
      - **3.1.2.2.1** Recipes include **name, ingredients, instructions, and estimated cooking time**

    #### 3.1.3 AI Chatbot for Recipe Assistance
    - **3.1.3.1 Chatbot Functionality**
      - **3.1.3.1.1** Users can ask recipe-related questions
      - **3.1.3.1.2** AI chatbot provides ingredient-based suggestions
      - **3.1.3.1.3** Users can inquire about **cooking techniques, dietary substitutions, and food pairings**

    #### 3.1.4 Software Engineering Documentation Page
    - **3.1.4.1 System Documentation**
      - **3.1.4.1.1** Displays **Use Case Diagram, System Diagram, Activity Diagram, and Class Diagram**

    ### 3.2 Non-Functional Requirements

    #### 3.2.1 Performance Requirements
    - **3.2.1.1** AI-based recommendations should be **generated within 5 seconds**
    - **3.2.1.2** Chatbot responses should be **real-time or under 3 seconds**

    #### 3.2.2 Security Requirements
    - **3.2.2.1** User passwords are stored as **plain text** in CSV (not encrypted, per requirement)
    - **3.2.2.2** User input validation must be implemented to prevent SQL injection-like issues

    #### 3.2.3 Usability Requirements
    - **3.2.3.1** The application should have a **minimalist UI** for easy navigation
    - **3.2.3.2** Streamlit interface should be **responsive and accessible on mobile and desktop**

    #### 3.2.4 Reliability & Availability
    - **3.2.4.1** The system should be **available 24/7**, barring AI model API downtimes
    - **3.2.4.2** In case of API failure, the system should display **basic fallback recipes from the dataset**

    #### 3.2.5 Scalability
    - **3.2.5.1** The application should be able to handle **100 concurrent users** with minimal lag
    - **3.2.5.2** AI model requests should be optimized to **minimize token consumption**
    """)
    
    # Appendices
    st.subheader("4. Appendices")
    st.markdown("""
    - **Recipe NLG Dataset** reference
    - **LLaMA 3.3-70B-Versatile API Documentation**
    - **Streamlit framework documentation**
    """)

def show_use_case_diagram():
    st.header("Use Case Diagram")
    
    # Display the use case diagram image
    st.image("static/images/usecase_diagram.png", caption="AI-Based Recipe Recommendation System - Use Case Diagram", use_column_width=True)
    
    # Add description of the use case diagram
    st.markdown("""
    The Use Case Diagram illustrates the main interactions between different actors and the system:

    **Actors:**
    1. User - Primary actor who interacts with the system
    2. AI Model (LLaMA 3.3-70B) - System actor that handles AI-based operations
    3. System Admin - Administrator who manages the system

    **Main Use Cases:**
    1. User Operations:
        - View System Documentation
        - Sign Up
        - Login
        - Provide Preferences
        - Receive Recipe Recommendations
        - View Recipe Details
        - Search for Recipes
        - Save Favorite Recipes
        - View Saved Recipes
        - Update Profile
        - Ask AI Chatbot for Help
        - Respond to Chatbot Queries

    2. AI Model Operations:
        - Generate Recipe Recommendations
        - Respond to Chatbot Queries

    3. Admin Operations:
        - Manage Users
        - Update Recipe Dataset

    **Relationships:**
    - «include» relationships show mandatory inclusions
    - «extend» relationships show optional extensions
    - «generalization» shows relationships between general and specific use cases
    """)

def show_system_diagram():
    st.header("System Architecture Diagram")
    
    # Display the system architecture diagram
    st.image("static/images/system_diagram.png", use_column_width=True)
    
    # Add description of the system architecture
    st.markdown("""
    The system architecture diagram illustrates the key components and their interactions:

    **1. Frontend Layer:**
    - **Streamlit UI**: Web-based user interface
        - User Authentication Interface
        - Recipe Search & Display
        - Chatbot Interface
        - User Preference Management
        - Documentation View

    **2. Application Layer:**
    - **Authentication Module**
        - User Registration
        - Login Management
        - Session Handling
    - **Recipe Management**
        - Recipe Search
        - Recommendation Engine
        - Favorite Recipe Management
    - **Chatbot Module**
        - Query Processing
        - Response Generation
        - Context Management

    **3. Data Layer:**
    - **CSV Database**
        - User Profiles
        - User Preferences
        - Favorite Recipes
    - **Recipe NLG Dataset**
        - Recipe Information
        - Ingredients
        - Instructions
        - Cooking Times

    **4. AI Services Layer:**
    - **LLaMA 3.3-70B-Versatile Model**
        - Recipe Recommendation Processing
        - Natural Language Understanding
        - Response Generation
        - Context Analysis

    **Data Flow:**
    1. User interactions are handled through the Streamlit UI
    2. Authentication requests are processed via the Auth Module
    3. Recipe requests trigger the Recipe Management system
    4. AI queries are processed by LLaMA 3.3-70B-Versatile
    5. Data is persisted in CSV format
    6. Recipe information is retrieved from the Recipe NLG Dataset

    **Security & Performance:**
    - RESTful API communication between components
    - Asynchronous processing for AI operations
    - Session-based user authentication
    - Data validation at each layer
    """)

def show_activity_diagram():
    st.header("Activity Diagram")
    # Display the activity diagram image
    st.image("static/images/activity_diagram.png", caption="AI-Based Recipe Recommendation System - Activity Diagram", use_column_width=True)
    
    # Add description of the activity diagram
    st.markdown("""
    The Activity Diagram illustrates the system's workflow and interactions:

    **1. User Authentication Flow:**
    - Application Access
    - Authentication Check
    - Login/Signup Process
    - Credential Validation

    **2. Recipe Recommendation Flow:**
    - User Preference Collection
    - Recipe Search & Filtering
    - AI-Based Recommendation Generation
    - Recipe Display

    **3. Chatbot Interaction Flow:**
    - User Query Input
    - Query Processing
    - AI Response Generation
    - Answer Display

    **4. Decision Points:**
    - Authentication Status Check
    - User Preference Validation
    - Recipe Availability Check
    - Query Understanding Check

    **5. Parallel Activities:**
    - Recipe Data Retrieval
    - AI Model Processing
    - User Interface Updates
    """)

def show_class_diagram():
    st.header("Class Diagram")
    # Display the class diagram image
    st.image("static/images/class_diagram.png", caption="AI-Based Recipe Recommendation System - Class Diagram", use_column_width=True)
    
    # Add description of the class diagram
    st.markdown("""
    The Class Diagram shows the system's object-oriented structure and relationships:

    **1. User Class:**
    - Attributes:
        - username: string
        - password: string
        - preferences: dictionary
    - Methods:
        - login()
        - signup()
        - update_preferences()
        - save_favorite_recipe()

    **2. Recipe Class:**
    - Attributes:
        - name: string
        - ingredients: list
        - instructions: list
        - cooking_time: string
        - cuisine_type: string
    - Methods:
        - get_details()
        - calculate_nutrition()
        - get_cooking_steps()

    **3. Recommender Class:**
    - Attributes:
        - model: LLaMA
        - dataset: DataFrame
        - user_preferences: dictionary
    - Methods:
        - get_recommendations()
        - filter_recipes()
        - rank_recipes()
        - update_preferences()

    **4. Chatbot Class:**
    - Attributes:
        - model: LLaMA
        - chat_history: list
        - context: dictionary
    - Methods:
        - get_response()
        - process_query()
        - maintain_context()
        - provide_suggestions()

    **5. Authentication Class:**
    - Attributes:
        - user_database: CSV
        - active_sessions: dictionary
    - Methods:
        - verify_credentials()
        - create_user()
        - manage_session()
        - update_user_data()

    **Relationships:**
    - User ---> Recipe (Interacts with)
    - Recommender ---> Recipe (Processes)
    - Chatbot ---> Recipe (References)
    - User ---> Authentication (Validates through)
    - Recommender ---> User (Personalizes for)
    """)