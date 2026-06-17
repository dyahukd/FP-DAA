import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import time
import csv
import random
from src.maze_gen import generate_maze
from src.algorithms import bfs, astar
from game.settings import BENCHMARK_SIZES, BENCHMARK_TRIALS, BENCHMARK_SEED

def pick_random_floor(grid):
    size = len(grid)
    floors = [(r,c) for r in range(size) for c in range(size) if grid[r][c] == 0]
    return random.choice(floors) if floors else None

def run_benchmark():
    print("=== BENCHMARK STARTED ===")
    results = []
    total_instances = 0  # <-- DEKLARASI DI SINI

    for size in BENCHMARK_SIZES:
        for trial in range(BENCHMARK_TRIALS):
            print(f"Size {size}, trial {trial+1}/{BENCHMARK_TRIALS}")
            seed = BENCHMARK_SEED + size * 100 + trial
            grid = generate_maze(size, seed)
            start = pick_random_floor(grid)
            goal = pick_random_floor(grid)

            if start is None or goal is None or start == goal:
                print(f"  Skipped: start={start}, goal={goal}")
                continue

            total_instances += 1

            try:
                # BFS
                t0 = time.perf_counter()
                path_bfs, expanded_bfs = bfs(grid, start, goal)
                t_bfs = time.perf_counter() - t0

                # A*
                t0 = time.perf_counter()
                path_astar, expanded_astar = astar(grid, start, goal)
                t_astar = time.perf_counter() - t0

                same_length = (len(path_bfs) == len(path_astar)) if path_bfs and path_astar else False

                results.append({
                    'size': size,
                    'trial': trial,
                    'seed': seed,
                    'bfs_time_ms': t_bfs * 1000,
                    'astar_time_ms': t_astar * 1000,
                    'bfs_expanded': expanded_bfs,
                    'astar_expanded': expanded_astar,
                    'path_len_bfs': len(path_bfs),
                    'path_len_astar': len(path_astar),
                    'same_length': same_length
                })
            except Exception as e:
                print(f"  ERROR at size {size}, trial {trial}: {e}")
                continue

    print(f"Total instances collected: {total_instances}")

    if not results:
        print("No results collected. Exiting without CSV.")
        return

    # Tulis CSV - path absolut berdasarkan direktori script
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
    os.makedirs(results_dir, exist_ok=True)
    csv_path = os.path.join(results_dir, 'benchmark.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"CSV saved to {csv_path}")

if __name__ == '__main__':
    run_benchmark()