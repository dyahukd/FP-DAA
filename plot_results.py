import os
import pandas as pd
import matplotlib.pyplot as plt

# Path absolut ke CSV
csv_path = os.path.join(os.path.dirname(__file__), '..', 'results', 'benchmark.csv')
df = pd.read_csv(csv_path)

grouped = df.groupby('size').mean()

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(grouped.index, grouped['bfs_time_ms'], 'o-', label='BFS')
plt.plot(grouped.index, grouped['astar_time_ms'], 's-', label='A*')
plt.xlabel('Grid Size (N)')
plt.ylabel('Runtime (ms)')
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(grouped.index, grouped['bfs_expanded'], 'o-', label='BFS')
plt.plot(grouped.index, grouped['astar_expanded'], 's-', label='A*')
plt.xlabel('Grid Size (N)')
plt.ylabel('Expanded Nodes')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'results', 'plot.png'))
plt.show()