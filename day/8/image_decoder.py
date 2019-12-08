def split_into_layers(data, layer_size):
    layers = []
    while len(data) > layer_size:
        layer = data[:layer_size]
        layers.append(layer)
        data   = data[layer_size:]
    layers.append(data)
    return layers

with open("input", "r") as f:
    image_data = f.read()
    image_width = 25
    image_height = 6
    layer_size = image_width * image_height
    layers = split_into_layers(image_data, layer_size)

    min_zero_count = layer_size
    number_of_ones = 0
    number_of_twos = 0

    for layer in layers:
        zeros = layer.count("0")
        if zeros < min_zero_count:
            min_zero_count = zeros
            number_of_ones = layer.count("1")
            number_of_twos = layer.count("2")

    print("part 1 : {}".format(number_of_ones * number_of_twos))

    for i in range(image_height):
        for j in range(image_width):
            for layer in layers:
                data = layer[j + (i * image_width)]
                if int(data) < 2:
                    if data == "1":
                        print("*", end="")
                    else:
                        print(" ", end="")
                    break
        print("")



