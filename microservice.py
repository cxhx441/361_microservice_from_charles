# Charles' microservice for Craig

def get_max_from_origin(coordinates) -> tuple:
    max_from_origin = -1
    for data_set in coordinates:
        for coord_pair in data_set:
            max_from_origin = max(max_from_origin, coord_pair[0], coord_pair[1])
    print(max_from_origin)
    return max_from_origin

def format_dict_for_grid(coord_dict_scaled, set1, set2):
    res = {}
    for set_num in range(len(coord_dict_scaled)):
        for coord_num in range(len(coord_dict_scaled[set_num])):
            x = str(coord_dict_scaled[set_num][coord_num][0])
            y = str(coord_dict_scaled[set_num][coord_num][1])
            key = str(x + "," + y)
            if key not in res:
                value = None
                if set_num == 0:
                    value = [set1[1][coord_num], set1[3]] # [string, color]
                elif set_num == 1:
                    value = [set2[1][coord_num], set2[3]] # [string, color]
                res[key] = value
            else:
                print(f"Warning: there is already an object on ({key})!")
    return res

def generate_scaled_dict(coordinates, max_from_origin, max_dimension):
    coord_dict_scaled = {}  # ex. {1:[[1,2],[3,4]], 2:[[5,6],[7,8]]}
    # why dict? It's not easy to compare coordinate pairs.
    max_x_scaled = max_y_scaled = -1
    for set_num in range(len(coordinates)):
        set_coords_scaled = []  # a list of two coordinate pairs
        for coord_pair in coordinates[set_num]:
            x_scaled = int(((max_dimension-1) * coord_pair[0]) / max_from_origin)
            y_scaled = int(((max_dimension-1) * coord_pair[1]) / max_from_origin)
            max_x_scaled = max(max_x_scaled, x_scaled)
            max_y_scaled = max(max_y_scaled, y_scaled)
            set_coords_scaled.append((x_scaled, y_scaled))
        coord_dict_scaled[set_num] = set_coords_scaled
    print("scaled_dict: ", coord_dict_scaled)
    return coord_dict_scaled, max_x_scaled, max_y_scaled

def print_grid(formatted_coord_dict, max_x_scaled, max_y_scaled):
    ''' origin is top-left (0, 0) '''
    for x in range(0, max_x_scaled+1):
        for y in range(0, max_y_scaled+1):
            coor_key = str(x) + "," + str(y)
            if coor_key in formatted_coord_dict:
                obj_str = formatted_coord_dict[coor_key][1] + formatted_coord_dict[coor_key][0]
                print(obj_str, end=" ")
            else:
                print(f"\u001b[30m..", end=" ")
        print()


def microservice(max_print_dimension, data_1, data_2):
    coordinates = data_1[2:3] + data_2[2:3]
    max_from_origin = get_max_from_origin(coordinates)

    coord_dict_scaled, max_x_scaled, max_y_scaled = generate_scaled_dict(coordinates, max_from_origin, max_print_dimension)
    formatted_coord_dict = format_dict_for_grid(coord_dict_scaled, data_1, data_2)

    print("formatted_dict: ", formatted_coord_dict)

    print_grid(formatted_coord_dict, max_x_scaled, max_y_scaled)


if __name__ == '__main__':
    # data_1 = ("s", ["01", "02"], [(1.6, 33.2), (1.6, 33.2)], "\033[93m")
    data_1 = ("s", ["01", "02"], [(1.6, 33.2), (82.6, 41.2)], "\033[93m")
    # data_1 = ("s", ["01", "02"], [(1.6, 33.2), (82.6, 423.9)], "\033[93m")
    data_2 = ("r", ["03", "04"], [(353.2, 112.5), (523.9, 5.3)], "\u001b[34m")
    # set1 = ("s", ["01", "02"], [(82.6, 41.2),(1.6, 33.2)], "\033[93m")
    # set2 = ("r", ["03", "04"], [(523.9, 5.3),(353.2, 112.5)], "\u001b[34m")
    grid = microservice(max_print_dimension=10, data_1=data_1, data_2=data_2)
