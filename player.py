from typing import Optional


class Player:
    """Represents a basketball player with core stats."""

    def __init__(
        self,
        name,
        team,
        points_per_game = 0.0,
        steals_per_game = 0.0,
        assists_per_game = 0.0,
        blocks_per_game = 0.0,
    ) -> None:
        if points_per_game < 0:
            raise ValueError("points_per_game cannot be negative")
        if steals_per_game < 0:
            raise ValueError("steals_per_game cannot be negative")
        if assists_per_game < 0:
            raise ValueError("assists_per_game cannot be negative")
        if blocks_per_game < 0:
            raise ValueError("blocks_per_game cannot be negative")
        
        self.name: str = name
        self.team: str = team
        self.points_per_game: float = points_per_game
        self.steals_per_game: float = steals_per_game
        self.assists_per_game: float = assists_per_game
        self.blocks_per_game: float = blocks_per_game

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.team}) — "
            f"{self.points_per_game:.1f} ppg, "
            f"{self.steals_per_game:.1f} spg, "
            f"{self.assists_per_game:.1f} apg, "
            f"{self.blocks_per_game:.1f} bpg, "
        )

    def __repr__(self) -> str:
        return (
            "Player("
            f"name={self.name!r}, team={self.team!r}, "
            f"points_per_game={self.points_per_game!r}, "
            f"steals_per_game={self.steals_per_game!r}, "
            f"assists_per_game={self.assists_per_game!r}, "
            f"blocks_per_game={self.blocks_per_game!r}, "
        )


def main(csv_path: str, stat_arg: Optional[str] = None, alg_arg: Optional[str] = None) -> None:
    """Quick CLI check to confirm CSV scraping works and test sorting.

    The function accepts optional `stat_arg` and `alg_arg`. If they are not
    provided, it interactively prompts the user. `stat_arg` can be a number
    (as displayed in the numbered list) or the stat key (e.g. `ppg`).
    `alg_arg` should be the first few letters of the algorithm name
    (e.g. `ins` for insertion sort, `np` for numpy, `py` for Python built-in).
    """
    from pathlib import Path
    from .data_loader import load_players_from_csv, synthetic_player_data
    from .sorting_algorithms import (
        numpy_sort,
        insertion_sort,
        heapsort,
        STAT_MAPPING,
    )

    resolved_path = Path(csv_path).expanduser()

    try:
        players = load_players_from_csv(str(resolved_path))
    except FileNotFoundError:
        print(f"Could not find CSV at: {resolved_path}")
        return

    print(f"----------\nLoaded {len(players)} players from {resolved_path}")    


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m final_project.player <csv_path>")
    else:
        main(sys.argv[1])
