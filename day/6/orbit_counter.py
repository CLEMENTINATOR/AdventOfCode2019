def build_path_to_center(map, point, center="COM"):
    temp = point
    path = []
    while True:
        for orbit_center, orbitees in space_map.items():
            if temp in orbitees:
                path.append(orbit_center)
                temp = orbit_center
                break
        if temp == center:
            break
    return path

with open("input", "r") as f:
    space_map = {}
    space_objects = []
    orbit_list = f.read().split("\n")
    for orbit in orbit_list:
        objects = orbit.split(")")
        center = objects[0]
        in_orbit = objects[1]

        if center not in space_objects:
            space_objects.append(center)

        if in_orbit not in space_objects:
            space_objects.append(in_orbit)

        if not space_map.get(center):
            space_map[center] = []
        space_map[center].append(in_orbit)

    # part 1
    orbit_counts = 0

    for space_object in space_objects:
        path = build_path_to_center(space_map, space_object)
        orbit_counts += len(path)

    print("part1: {}".format(orbit_counts))

    # part 2:
    you_path = build_path_to_center(space_map, "YOU")
    san_path = build_path_to_center(space_map, "SAN")

    for point in you_path:
        if point in san_path:
            break
    print("part2: {}".format(you_path.index(point) + san_path.index(point)))
