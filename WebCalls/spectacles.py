def rough_parse_phonebook():
    with open("WebCalls/phonebook.txt", "r") as f:
        lines = [line.rstrip('\n') for line in f]
    content_list = []
    for line in lines:
        if "###" in line:
            content_list.append([])
        else:
            content_list[len(content_list)-1].append(line)
    return content_list


def jsonify(rough_parse):
    content_list = []
    for piece in rough_parse:
        piece_dict = {}
        for line in piece:
            line_parts = line.split("::",)
            key = line_parts[0]
            line_parts.pop(0)
            element = line_parts
            piece_dict.update({key: element})
        content_list.append(piece_dict)
    return content_list


def parse_section_1(input_dict):
    for key in input_dict:
        new_item = input_dict[key][0]
        input_dict[key] = new_item
    return input_dict


def parse_section_2(input_dict):
    for key in input_dict:
        input_dict[key][1] = int(input_dict[key][1])
        input_dict[key][2] = input_dict[key][2].strip('[').strip(']').split(',',)
        if len(input_dict[key][2][0]) == 0:
            input_dict[key][2] = []
    return input_dict


def parse_section_3(input_dict):
    for key in input_dict:
        input_dict[key] = str(input_dict[key][0])
    return input_dict


def parse_section_4(input_dict):
    for key in input_dict:
        new_input = input_dict[key][1].split(',',)
        i = 0
        for piece in new_input:
            if '[' in piece:
                new_input[i] = piece.strip('[').strip(']').split(';',)
            i += 1
        input_dict[key][1] = new_input
    return input_dict


def parse_section_5(input_dict):
    for key in input_dict:
        new_item = input_dict[key][0]
        new_item = new_item.strip('[').strip(']').split(',',)
        input_dict[key] = new_item
    return input_dict


def parse_section_6(input_dict):
    for key in input_dict:
        input_dict[key] = input_dict[key][0]
    return input_dict


def parse():
    content_list = jsonify(rough_parse_phonebook())
    content_list[0] = parse_section_1(content_list[0])
    content_list[1] = parse_section_2(content_list[1])
    content_list[2] = parse_section_3(content_list[2])
    content_list[3] = parse_section_4(content_list[3])
    content_list[4] = parse_section_5(content_list[4])
    content_list[5] = parse_section_6(content_list[5])
    return content_list


# 1 - key words
#   keyword
#   :
#   meaning
# 2 - api call functions
#   api function name
#   :
#   api function url string
#   number of arguments
#   arguments
# 3 - arguments
#   argument name
#   :
#   type
# 4 - api call paths
#   goal
#   :
#   api function to use
#   parse path
# 5 - result interpretations
#   goal
#   :
#   result
