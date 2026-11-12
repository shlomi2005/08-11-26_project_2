import json
from pathlib import Path


def load_game_history():
    path = Path(__file__).parent / "game_history.json"
    with open(path, "r+") as file:
        history = json.load(file)
        return history


def write_json(all):
    history = load_game_history()
    history.append(all)
    path = Path(__file__).parent / "game_history.json"
    with open(path, "r+") as file:
        json.dump(history, file, indent=2)
