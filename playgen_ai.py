import os
from openai import OpenAI
import streamlit as st
from GameMethods import GameMethods as gm

# Set page title and favicon
st.set_page_config(
    page_title="PlayGen AI",
    page_icon="🎮",
)

# Create an OpenAI client instance using the API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# CSS styles
custom_css = """
<style>
/* Base styles */
body {
    background-color: rgba(234, 242, 248, 0.7); /* Light blue background with transparency */
}

/* Title styles */
h1 {
    color: #2980b9; /* Blue title */
    text-align: center; /* Center align title */
    font-size: 36px; /* Larger font size */
}

/* Input styles */
.stTextInput>div>div>input {
    border-radius: 20px; /* Rounded corners for input fields */
    border: 1px solid #3498db; /* Blue border for input fields */
    padding: 12px; /* Add padding for input fields */
    width: 100%; /* Make input fields 100% width */
}

/* Button styles */
.stButton>button {
    border-radius: 20px; /* Rounded corners for buttons */
    border: 2px solid #3498db; /* Blue border for buttons */
    color: #fff; /* White text color */
    background-color: #3498db; /* Blue background color */
    padding: 12px 20px; /* Add padding to buttons */
    cursor: pointer; /* Show pointer on hover */
    box-sizing: border-box; /* Include padding in width */
}

.stButton>button:hover {
    background-color: #2980b9; /* Darker blue background on hover */
}

/* Header styles */
.stMarkdown h2 {
    color: #2980b9; /* Blue header text */
    font-size: 24px; /* Larger font size */
}

/* Expander styles */
.stExpander>div>div:first-child {
    background-color: #3498db; /* Blue background for expander header */
    color: #fff; /* White text color for expander header */
    border-radius: 20px; /* Rounded corners for expander header */
    padding: 12px 20px; /* Add padding to expander header */
    cursor: pointer; /* Show pointer on hover */
}

.stExpander>div>div:first-child:hover {
    background-color: #2980b9; /* Darker blue background on hover */
}
</style>
"""

# Function to inject custom CSS
def inject_custom_css():
    st.markdown(custom_css, unsafe_allow_html=True)

def main():
    inject_custom_css()
    
    st.title("PlayGen AI")

    # Using columns to layout the input and button
    col1, col2 = st.columns([3, 1])
    with col1:
        num_players = st.number_input("Number of Players (Min: 1)", min_value=1, value=1)
    with col2:
        generate_button = st.button("Generate Game Ideas", key="generate_button")

    if generate_button:
        if num_players:
            try:
                game_1, game_2 = gm().game_ai(client, num_players)

                st.header(f"🎮 Game Ideas for {num_players} Players", anchor=None)
                with st.expander("Game 1"):
                    st.markdown(game_1)
                with st.expander("Game 2"):
                    st.markdown(game_2)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter the number of players before generating ideas.")

if __name__ == "__main__":
    main()
