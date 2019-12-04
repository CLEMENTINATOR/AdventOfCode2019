import collections

with open("input", "r") as f:
    wires = f.read().split("\n")
    full_grid = collections.defaultdict(int)
    grid_list = []
    for wire in wires:
        grid = collections.defaultdict(int)
        wire_path = wire.split(",")
        pos = (0, 0)
        step = 0
        for path in wire_path:
            direction = path[0]
            count = int(path[1:])
            vector_x = 0
            vector_y = 0

            if direction == "R":
                vector_x = 1
            elif direction == "L":
                vector_x = -1
            elif direction == "U":
                vector_y = 1
            elif direction == "D":
                vector_y = -1

            for i in range(count):
                if not grid[pos]:
                    grid[pos] = step
                step += 1
                pos_x, pos_y = pos
                pos = (pos_x + vector_x, pos_y + vector_y)

        grid_list.append(grid)

        for pos, data in grid.items():
            if data:
                full_grid[pos] += 1

    min_distance = None
    min_steps = None
    for pos, data in full_grid.items():
        if data >= 2:
            pos_x, pos_y = pos
            distance = abs(pos_x) + abs(pos_y)
            if not distance:
                continue
            if not min_distance or distance < min_distance:
                min_distance = distance

            steps = 0
            for grid in grid_list:
                steps += grid[pos]

            if not min_steps or steps < min_steps:
                min_steps = steps

    print(f"minimal knot distance: {min_distance}")
    print(f"minimal knot steps: {min_steps}")
