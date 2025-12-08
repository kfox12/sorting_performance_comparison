"""Timing comparisons for sorting algorithms with optional plotting."""

import argparse
import statistics
import time
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Tuple

import matplotlib.pyplot as plt

from .data_loader import load_players_from_csv
from . import sorting_algorithms as sa
from .sorting_algorithms import STAT_MAPPING
from .player import Player


SortFn = Callable[[List[Player], str, bool], List[Player]]


def parse_sizes(raw: Iterable[str]) -> List[int]:
    """Parse comma- or space-separated size inputs into ints, keeping order and uniqueness."""
    sizes: List[int] = []
    for chunk in raw:
        for part in chunk.split(","):
            part = part.strip()
            if not part:
                continue
            value = int(part)
            if value not in sizes:
                sizes.append(value)
    return sizes


def build_datasets(csv_paths: List[str], sizes: List[int]) -> List[Tuple[str, int, List[Player]]]:
    """Load players for each CSV and slice into the requested sample sizes."""
    datasets: List[Tuple[str, int, List[Player]]] = []
    for path in csv_paths:
        players = load_players_from_csv(path)
        base = Path(path).name
        for size in sizes:
            subset = players[: min(size, len(players))]
            if not subset:
                continue
            datasets.append((base, len(subset), subset))
    return datasets


def time_algorithm(players: List[Player], func: SortFn, stat: str, descending: bool, repeats: int,) -> Tuple[float, float]:
    """Return (avg_ms, stdev_ms) for a sorting function over repeated runs."""
    timings: List[float] = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(players.copy(), stat, descending)
        end = time.perf_counter()
        timings.append((end - start) * 1000.0)

    avg = statistics.mean(timings)
    stdev = statistics.stdev(timings) if len(timings) > 1 else 0.0
    return avg, stdev


def collect_timings(datasets: List[Tuple[str, int, List[Player]]], algorithms: Dict[str, SortFn], stat: str, descending: bool, repeats: int):
    results = []
    for dataset_name, size, players in datasets:
        for alg_name, func in algorithms.items():
            avg_ms, stdev_ms = time_algorithm(players, func, stat, descending, repeats)
            results.append(
                {
                    "dataset": dataset_name,
                    "size": size,
                    "algorithm": alg_name,
                    "avg_ms": avg_ms,
                    "stdev_ms": stdev_ms,
                }
            )
    return results


def print_results(results) -> None:
    print("\nTiming results (ms):")
    header = f"{'Dataset':25} {'Size':>8} {'Algorithm':20} {'Avg':>10} {'Stdev':>10}"
    print(header)
    print("-" * len(header))
    for row in sorted(results, key=lambda r: (r["size"], r["algorithm"])):
        print(
            f"{row['dataset'][:25]:25} "
            f"{row['size']:>8} "
            f"{row['algorithm']:20} "
            f"{row['avg_ms']:>10.3f} "
            f"{row['stdev_ms']:>10.3f}"
        )


def plot_results(results, output_path: str) -> None:
    sizes = sorted({row["size"] for row in results})
    algs = sorted({row["algorithm"] for row in results})

    for alg in algs:
        xs: List[int] = []
        ys: List[float] = []
        for size in sizes:
            matches = [r for r in results if r["algorithm"] == alg and r["size"] == size]
            if not matches:
                continue
            avg = statistics.mean(r["avg_ms"] for r in matches)
            xs.append(size)
            ys.append(avg)
        if xs and ys:
            plt.plot(xs, ys, marker="o", label=alg)

    plt.xlabel("Dataset size (players)")
    plt.ylabel("Time (ms)")
    plt.title("Sorting algorithm timing")
    plt.legend()
    plt.grid(True, linestyle=":", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()
    print(f"Saved plot to {output_path}")



def main() -> None:
    # Configuration dictionary
    config = {
        "stat": "ppg",
        "descending": True,
        "repeats": 3,
        "sizes": [100, 500, 1000],
        "plot_out": "timing_results.png",
    }

    # Parse only CSV file(s) from command line
    parser = argparse.ArgumentParser(description="Timing analysis for sorting algorithms.")
    parser.add_argument(
        "csv",
        nargs="+",
        help="One or more CSV files containing player stats.",
    )
    args = parser.parse_args()

    # Define algorithms
    algorithms: Dict[str, SortFn] = {
        "numpy_sort": sa.numpy_sort,
        "insertion_sort": sa.insertion_sort,
        "heapsort": sa.heapsort,
    }

    # Load datasets
    datasets = build_datasets(args.csv, config["sizes"])
    if not datasets:
        raise SystemExit("No data loaded from provided CSV(s).")

    # Collect and display results
    results = collect_timings(
        datasets=datasets,
        algorithms=algorithms,
        stat=config["stat"],
        descending=config["descending"],
        repeats=config["repeats"],
    )

    print_results(results)
    plot_results(results, config["plot_out"])


if __name__ == "__main__":
    main()
