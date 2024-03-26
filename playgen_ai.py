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
}

/* Title */
h1 {
    color: #333;
    font-size: 48px;
    font-weight: bold;
    margin-top: 60px;
    text-align: center;
}

/* Input for number of players */
.number-input {
    background-color: #fff;
    border: 2px solid #333;
    border-radius: 5px;
    padding: 10px 15px;
    margin: 0 auto 20px;
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
}

.generate-button:hover {
    background-color: #444;
}

/* Game ideas header */
.game-ideas-header {
    color: #333;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
}

/* Game idea container */
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
    st.title("PlayGen AI")

    num_players = st.number_input("Number of Players (Min: 1)", min_value=1, container_class="number-input")

    if st.button("Generate Game Ideas!", class_name="generate-button"):
        try:
            game_1, game_2 = gm().game_ai(client, num_players)

            st.header(f" Game Ideas for {num_players} Players")

            for game_index, game_idea in enumerate([game_1, game_2]):
                st.write(
                    "",
                    unsafe_allow_html=True,
                )  # Add an empty line for visual separation
                with st.container():
                    st.subheader(f"**Game {game_index + 1}**")
                    st.markdown(game_idea)

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
