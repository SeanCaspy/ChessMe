from chessdotcom import get_player_games_by_month, Client
import re

def get_player_game(game_pgn):
    """
        returns string describes the moves and time of the game
        Args:
             game_pgn(str): all the valibals of the game

        """
    results = re.findall(r'1\.\s*(.*?)(?=\d-\d)', game_pgn)
    results = [f"{i + 1}. {move}" for i, move in enumerate(results)]
    return results


def get_player_color(game_pgn, userName):
    """
    Returns 'white', 'black', or None based on PGN and username

    Args:
        game_pgn (str): The PGN string of the game

    Returns:
        str: 'white', 'black', or None
    """
    pattern = rf'\[(\w+)\s+"{re.escape(userName)}"\]'
    match = re.search(pattern, game_pgn)

    if match:
        return match.group(1).lower()
    return None



Client.request_config["headers"]["User-Agent"] = ("MeChess/0.1 (Contact: Seancaspy@gmail.com)")

user_name = input("enter user name: ")
month = int(input("enter month: "))
year = int(input("enter year: "))


history = get_player_games_by_month(user_name, year, month)
for game in history.games:
    print(f"you played as {get_player_color(game.pgn, user_name)} \n{get_player_game(game.pgn)}")

