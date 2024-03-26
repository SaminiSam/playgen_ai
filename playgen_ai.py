import os
from openai import OpenAI
import streamlit as st
from GameMethods import GameMethods as gm


# Create an OpenAI client instance using the API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def main():

    st.title("AI-powered Game Idea Generator")

    # Input for number of players
    num_players = st.number_input("Number of Players (Min: 1)", min_value=1)

    # Print the variables for debugging (optional)
    # print(f"Client: {client}, Num Players: {num_players}")  # Uncomment for debugging

    # Generate button
    if st.button("Generate Game Ideas"):
        # Ensure num_players is defined and has a value before calling game_ai
        if num_players:
            game_1, game_2 = gm.game_ai(client, num_players)

            # Display generated game ideas with formatting
            st.header(f"Game Ideas for {num_players} Players")
            st.write("**Game 1:**", style="h3")
            st.write(game_1)
            st.write("---")  # Separator line
            st.write("**Game 2:**", style="h3")
            st.write(game_2)
        else:
            st.error("Please enter the number of players before generating ideas.")


if __name__ == "__main__":
    main()
