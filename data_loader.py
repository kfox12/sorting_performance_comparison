import csv
import random
from pathlib import Path
from typing import List

from .player import Player


def _to_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def load_players_from_csv(csv_path: str) -> List[Player]:
    """Read a stats CSV and return Player objects."""
    players: List[Player] = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            normalized = {key.lower(): val for key, val in row.items()}

            name = normalized.get("player")
            team = normalized.get("tm", "")
            pts = _to_float(normalized.get("pts", ""))
            ast = _to_float(normalized.get("ast", ""))
            blk = _to_float(normalized.get("blk", ""))
            stl = _to_float(normalized.get("stl", ""))

            if not name:
                continue

            player = Player(
                name=name,
                team=team,
                points_per_game=pts,
                steals_per_game=stl,
                assists_per_game=ast,
                blocks_per_game=blk,
            )

            players.append(player)

    return players


def synthetic_player_data(n: int) -> List[Player]:
    """Create a CSV file with `n` synthetic players and return the loaded Player objects.

    The CSV will be written to the current working directory with the name
    `synthetic_player_data({n}).csv`. Fields written match what
    `load_players_from_csv` expects: `Player, TM, PTS, AST, BLK, STL`.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    filename = f"synthetic_player_data({n}).csv"
    path = Path(filename)

    teams = [
        "ATL",
        "BOS",
        "BKN",
        "CHA",
        "CHI",
        "CLE",
        "DAL",
        "DEN",
        "DET",
        "GSW",
        "HOU",
        "IND",
        "LAC",
        "LAL",
        "MEM",
        "MIA",
        "MIL",
        "MIN",
        "NOP",
        "NYK",
        "OKC",
        "ORL",
        "PHI",
        "PHX",
        "POR",
        "SAC",
        "SAS",
        "TOR",
        "UTA",
        "WAS",
    ]

    # Create CSV with appropriate headers
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Player", "Tm", "PTS", "AST", "BLK", "STL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, n + 1):
            name = f"player_{i}"
            team = random.choice(teams)

            # Reasonable ranges with one decimal place for per-game stats
            pts = round(random.uniform(0.0, 35.0), 1)
            ast = round(random.uniform(0.0, 10.0), 1)
            blk = round(random.uniform(0.0, 3.0), 1)
            stl = round(random.uniform(0.0, 3.0), 1)

            writer.writerow({
                "Player": name,
                "Tm": team,
                "PTS": pts,
                "AST": ast,
                "BLK": blk,
                "STL": stl,
            })

    # Load and return the Player objects using the existing loader
    return load_players_from_csv(str(path))
