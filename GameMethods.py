class GameMethods:

    def game_ai(num_players):
        # Define the prompt for generating game ideas
        prompt = f"""
        You are a creative game designer. Please generate two game ideas for {num_players} players. 

        Game 1 should require specific items to play, and include a list of these items, along with the game rules and how to play.

        Game 2 should not require any items to play. Please include the game rules and how to play.

        Both games should be suitable for a casual setting and encourage teamwork or friendly competition.
        """

        # Generate the game ideas
        game_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": ""
                }
            ],
            max_tokens=800,  # You may adjust this value based on the length of response you need
            temperature=0.7  # Adjust for creativity; lower might be better for more structured output
        )

        # Extract the generated content
        generated_content = game_response.choices[0].message.content.strip()

        # Process the generated content to split into two games
        # This is a basic split; consider improving it to better match your output format
        split_token = "\n\nGame 2"
        games = generated_content.split(split_token)
        game_1 = games[0].strip()
        game_2 = "Game 2" + split_token.join(games[1:]).strip()

        return game_1, game_2

    # Example usage
    num_players = 3  # Example: 3 players
    game_1, game_2 = game_ai(num_players)

    # Print the generated game ideas
    print("Game 1 (With Items Required):")
    print(game_1)
    print("\nGame 2 (No Items Required):")
    print(game_2)
