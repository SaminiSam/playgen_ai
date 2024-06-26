class GameMethods:
    def __init__(self):
        pass

    def game_ai(self, client, num_players):
        if not client:
            raise ValueError("OpenAI client is not provided.")

        if not num_players:
            raise ValueError("Number of players is not provided.")

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

        # Further process the content to extract game details (optional)
        # You can implement logic here to parse the generated content and extract specific
        # information for each game, such as items required, rules, etc.
        # For example:
        # item_list_game1 = []  # List to store items required for game 1
        # rules_game1 = ""     # String to store rules for game 1
        # # Implement logic to parse the content of game_1 and extract items and rules
        # # ...

        return game_1, game_2
