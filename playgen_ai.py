import os
from openai import OpenAI
import streamlit as st
from GameMethods import GameMethods as gm

# Set page title and favicon
st.set_page_config(
    page_title="PlayGen AI",
    page_icon="🎮",
    layout="wide",  # Ensures the page takes the entire width
)

# Create an OpenAI client instance using the API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #11141C;
    }
    .container {
        padding: 2rem;
        background-color: #5FC1E3;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #E63946;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    st.title("PlayGen AI")

    # Centered container for content
    with st.container() as container:
        # Input for number of players
        num_players = st.number_input("Number of Players (Min: 1)", min_value=1)

        # Generate button
        if st.button("Generate Game Ideas"):
            # Check if num_players has a value before calling game_ai
            if num_players:
                try:
                    # Pass both client and num_players to game_ai function
                    game_1, game_2 = gm().game_ai(client, num_players)

                    # Display generated game ideas with formatting
                    st.header(f"🎮 Game Ideas for {num_players} Players")
                    st.subheader("**Game 1:**")
                    st.markdown(game_1)
                    st.subheader("**Game 2:**")
                    st.markdown(game_2)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter the number of players before generating ideas.")


if __name__ == "__main__":
    main()
