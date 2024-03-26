import os
from openai import OpenAI
import streamlit as st
from GameMethods import GameMethods as gm


client = OpenAI(
    api_key=st.secrets("OPENAI_API_KEY")
)

def main():

    st.title("AI-powered Game Idea Generator")

# Input for number of players
num_players = st.number_input("Number of Players (Min: 1)", min_value=1)

# Generate button
if st.button("Generate Game Ideas"):
  # Call the game_ai function from your imported GameMethods class
  game_1, game_2 = gm.game_ai(num_players)  # Assuming the function is named game_ai in GameMethods

  # Display generated game ideas with formatting
  st.header(f"Game Ideas for {num_players} Players")
  st.write("**Game 1:**", style="h3")
  st.write(game_1)
  st.write("---")  # Separator line
  st.write("**Game 2:**", style="h3")
  st.write(game_2)


if __name__ == "__main__":
    main()

