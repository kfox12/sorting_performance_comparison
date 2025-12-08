"""Small runner used by the Makefile `demo` target.

Generates synthetic datasets and runs the timing analysis producing
`timing_results_demo.png` in the workspace root.
"""
from pathlib import Path
import sys

# Ensure package import from workspace root
sys.path.insert(0, str(Path('.').resolve()))

from final_project.data_loader import synthetic_player_data, load_players_from_csv
from final_project import sorting_algorithms as sa
from final_project.timing_analysis import collect_timings, print_results, plot_results


def main() -> None:
    print('Generating synthetic datasets of size 10, 217, and 1000...')
    players_10 = synthetic_player_data(10)
    players_1000 = synthetic_player_data(1000)

    real_csv = Path(__file__).parent / '22:23_raw_player_stats-playoffs.csv'
    players_real = load_players_from_csv(str(real_csv))

    datasets = [
        (Path('synthetic_player_data(10).csv').name, len(players_10), players_10),
        (Path(real_csv).name, len(players_real), players_real),
        (Path('synthetic_player_data(1000).csv').name, len(players_1000), players_1000),
    ]

    algorithms = {
        'numpy_sort': sa.numpy_sort,
        'insertion_sort': sa.insertion_sort,
        'heapsort': sa.heapsort,
    }

    print('Running timing analysis\n\tSorting by points-per-game\nrepeating the sort for each algorithm 5 times and averaging...')
    results = collect_timings(datasets=datasets, algorithms=algorithms, stat='ppg', descending=True, repeats=5)
    print_results(results)
    plot_results(results, 'timing_results_demo.png')
    print('Demo complete. Plot saved to timing_results_demo.png')


if __name__ == '__main__':
    main()
