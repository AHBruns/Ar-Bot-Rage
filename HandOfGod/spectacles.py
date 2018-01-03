def read():
    position_data = {}
    with open("HandOfGod/positions.txt", "r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for line in content:
        line_parts = line.split('::',)
        pos_key = line_parts[0]
        pos_x = int(line_parts[1])
        pos_y = int(line_parts[2])
        position_data[pos_key] = [pos_x, pos_y]
    return position_data