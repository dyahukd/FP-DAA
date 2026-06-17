```
FP/
├── .vscode/
│   └── settings.json
│
├── src/
│   ├── algorithms.py
│   └── maze_gen.py
│
├── game/
│   ├── assets/ 
│   ├── asset_load.py
│   ├── game_state.py
│   ├── ghost_movement.py
│   ├── home_screen.py
│   ├── main.py
│   ├── map.py
│   ├── movement.py
│   ├── renderer.py
│   └── settings.py
│
├── bench/
│   ├── benchmark.py
│   └── plot_results.py
│
├── results/                     # (auto-generated)
│
└── requirements.txt
```

# Cara Menjalankan

`py -3.12 main.py` untuk testing game.
`py -3.12 bench/benchmark.py` untuk membuat file csv di folder results. Ini adalah hasil csv perbandingan BFS dan A*.
`py -3.12 bench/plot_results.py` untuk melihat grafik perbedaan.
