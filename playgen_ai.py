import os
from openai import OpenAI
import streamlit as st
from GameMethods import GameMethods as gm

# Set page title and favicon
st.set_page_config(
    page_title="PlayGen AI",
    page_icon="",
)

# Create an OpenAI client instance using the API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def main():
    # Add CSS for a cool and catchy UI
    st.write(
        """
<style>
body {
    margin: 0;
    font-family: sans-serif;
    background-color: #f4f4f4;  /* Light gray background */
    text-align: center;
}

/* Title and subtitle */
h1 {
    color: #333;
    font-size: 48px;
    font-weight: bold;
    margin-top: 60px;
}

h2 {
    color: #999;
    font-size: 24px;
    margin-bottom: 40px;
}

/* Number of players input */
.number-input {
    background-color: #fff;
    border: 2px solid #333;
    border-radius: 5px;
    padding: 10px 15px;
    margin: 0 auto;
    width: 200px;
    font-size: 18px;
    text-align: center;
}

/* Generate button */
.generate-button {
    background-color: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    margin-bottom: 30px;
}

.generate-button:hover {
    background-color: #444;
}

/* Game ideas */
.game-idea {
    background-color: #fff;
    border: 2px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    margin: 20px auto;
    max-width: 600px;
}

.game-idea h3 {
    color: #333;
    font-size: 24px;
    margin-bottom: 10px;
}

.game-idea p {
    font-size: 16px;
    line-height: 1.5;
}
</style>
""",
        unsafe_allow_html=True,
    )

    # App content
    st.title(" Unleash Your Creativity")  # Catchy title
    st.subheader("Power up your game nights with AI-generated ideas ")

    num_players = st.number_input("Players ", min_value=1, container_class="number-input")  # Custom class for input

    if st.button("Generate Game Ideas!", class_name="generate-button"):
        try:
            game_1, game_2 = gm().game_ai(client, num_players)

            st.header(f" Games for {num_players} Players")

            for game_index, game_idea in enumerate([game_1, game_2]):
                st.container()  # Clear spacing between game ideas
                st.write(
                    "",
                    unsafe_allow_html=True,
                )  # Add an empty line for visual separation
                st.markdown(f"<div class='game-idea'><h3>Game {game_index + 1}</h3>{game_idea}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
