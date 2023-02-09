# Charles' microservice for Craig

def find_max_x_y(coordinates) -> list:
    max_x = -1
    max_y = -1
    for set in coordinates:
        for coord_pair in set:
            max_x = max(max_x, coord_pair[0])
            max_y = max(max_y, coord_pair[1])
    print(max_x, max_y)
    return [max_x, max_y]

def format_dict_for_grid(coord_dict_scaled, set1, set2):
    res = {}
    for set_num in range(len(coord_dict_scaled)):
        for coord_num in range(len(coord_dict_scaled[set_num])):
            x = str(coord_dict_scaled[set_num][coord_num][0])
            y = str(coord_dict_scaled[set_num][coord_num][1])
            key = str(x[:-2] + "," + y[:-2])
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

def generate_scale_dict(coordinates, max_x, max_y, max_dimension):
    coord_dict_scaled = {}  # ex. {1:[[1,2],[3,4]], 2:[[5,6],[7,8]]}
    # why dict? It's not easy to compare coordinate pairs.
    for set_num in range(len(coordinates)):
        set_scaled = []  # a list of two coordinate pairs
        for coord_pair in coordinates[set_num]:
            x_scaled = (max_dimension * coord_pair[0]) // max_x
            y_scaled = (max_dimension * coord_pair[1]) // max_y
            set_scaled.append([x_scaled, y_scaled])
        coord_dict_scaled[set_num] = set_scaled
    print("scaled_dict: ", coord_dict_scaled)
    return coord_dict_scaled

def microservice(max_dimension, set1, set2):
    coordinates = set1[2:3] + set2[2:3]
    maxes = find_max_x_y(coordinates)
    max_x = maxes[0]
    max_y = maxes[1]

    coord_dict_scaled = generate_scale_dict(coordinates, max_x, max_y, max_dimension)
    formatted_coord_dict = format_dict_for_grid(coord_dict_scaled, set1, set2)

    print("formatted_dict: ", formatted_coord_dict)

    for y in range(max_dimension, -1, -1):
        for x in range(0, max_dimension + 1):
            coor_key = str(x) + "," + str(y)
            if coor_key in formatted_coord_dict:
                obj_str = formatted_coord_dict[coor_key][1] + formatted_coord_dict[coor_key][0]
                print(obj_str, end=" ")
                # print(formatted_coord_dict[coor_key][1]+coor_key, end=" ")

            else:
                print(f"\u001b[30m..", end=" ")
        print()


set1 = ("s", ["01", "02"], [(1.6, 33.2), (82.6, 41.2)], "\033[93m")
set2 = ("r", ["03", "04"], [(353.2, 112.5), (523.9, 5.3)], "\u001b[34m")
# set1 = ("s", ["01", "02"], [(82.6, 41.2),(1.6, 33.2)], "\033[93m")
# set2 = ("r", ["03", "04"], [(523.9, 5.3),(353.2, 112.5)], "\u001b[34m")
grid = microservice(10, set1, set2)
