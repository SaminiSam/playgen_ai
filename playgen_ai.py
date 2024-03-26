import os
from openai import OpenAI
import streamlit as st
from GameMethods import GameMethods as gm

# Create an OpenAI client instance
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def main():
    st.set_page_config(page_title="AI Game Idea Generator", layout="wide")  # Wide layout for better spacing

    st.title("Spark Your Imagination ", anchor=None)
    st.subheader("Generate unique game ideas powered by AI ")

    col1, col2, col3 = st.columns([1, 4, 1])  # Arrange elements visually

    with col2:
        num_players = st.number_input("Number of Players", min_value=1)
        if num_players > 50:
            st.warning("Generating ideas for very large player counts might be challenging. Consider a smaller group.")

    with col3:
        st.info("ℹ", help="How it works")  # Information icon for help

    if st.button("Generate Game Ideas!", help="Click to create game ideas for the chosen number of players"):
        try:
            game_1, game_2 = gm().game_ai(client, num_players)

            st.header(f"Game Ideas for {num_players} Players")

            for game_index, game_idea in enumerate([game_1, game_2]):
                st.markdown(f"## Game {game_index + 1}")
                st.write("**Description:**", game_idea, unsafe_allow_html=True)  # Allow for basic formatting
                st.markdown("---")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
