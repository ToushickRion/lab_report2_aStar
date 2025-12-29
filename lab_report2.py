import heapq

# Manhattan distance heuristic
def manhattan(current, target):
    return abs(current[0] - target[0]) + abs(current[1] - target[1])


def astar(grid, start, target):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return g_cost[target], path

        for dr, dc in directions:
            nr = current[0] + dr
            nc = current[1] + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_g_cost
                    f_cost = new_g_cost + manhattan(neighbor, target)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None, None

with open("input.txt", "r") as file:
    R, C = map(int, file.readline().split())

    grid = []
    for _ in range(R):
        grid.append(list(map(int, file.readline().split())))

    sr, sc = map(int, file.readline().split())
    tr, tc = map(int, file.readline().split())

start = (sr, sc)
target = (tr, tc)

cost, path = astar(grid, start, target)

if path:
    print(f"Path found with cost {cost} using A*")
    print(f"Shortest Path: {path}")
else:
    print("No path found")
