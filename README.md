# THis is for my Ai labreport- 2

## 📌 Overview 
In this i implemented the **A\*** search algorithm to find the shortest path between a start and target node in a 2D grid. 
A\* is one of the most widely used pathfinding algorithms because it combines: 
  - **Optimality** (always finds the shortest path if one exists) 
  - **Efficiency** (guided by heuristics to reduce search space)

## ⚙️ How It Works 
- The grid is represented as a matrix of `0`s and `1`s: 
      - `0` → free cell (can be traversed) 
      - `1` → blocked cell (obstacle) 
- The algorithm uses: 
      - **g-cost** → actual cost from start to current node 
      - **h-cost** → heuristic (Manhattan distance to target) 
      - **f-cost = g-cost + h-cost** → priority for exploration 
- It returns:
      - The **cost** of the shortest path 
      - The **path (sequence of coordinates)** from start to target
