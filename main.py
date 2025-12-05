from chessdotcom import get_player_games_by_month, Client
import re

def get_player_game(game_pgn, user_name):
    pass

def get_player_color(game_pgn, username):
    """
    Returns 'white', 'black', or None based on PGN and username

    Args:
        game_pgn (str): The PGN string of the game
        username (str): Your username to find

    Returns:
        str: 'white', 'black', or None
    """
    pattern = rf'\[(\w+)\s+"{re.escape(username)}"\]'
    match = re.search(pattern, game_pgn)

    if match:
        return match.group(1).lower()
    return None


Client.request_config["headers"]["User-Agent"] = ("MeChess/0.1 (Contact: Seancaspy@gmail.com)")

# user_name = input("whats you user name?")


history = get_player_games_by_month("aui129", 2025, 11)
print(history)
# for game in history.games:
#     print(f"you played as: {get_player_color(game.pgn, user_name)} and here's you game {get}")


