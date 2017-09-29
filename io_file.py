""" i/o file """

def read_file(file_name):
    """" read file function """
    lst_in = []
    f_open = open(file_name, "r", encoding="ISO-8859-1")
    str_line = ""

    while True:
        str_line = f_open.readline()
        str_line = str_line.replace("\n", "")

        if str_line == "":
            break
        lst_in.append(str_line)

    f_open.close()
    return lst_in


def read_stateabbr(file_name):
    """ read state abbreviation """
    lst_stateabbr = read_file(file_name)
    lst_abbr = []

    for item in lst_stateabbr:
        lst_abbr.append(item.split(" ")[0])

    return lst_abbr


def read_data(file_name, lst_header):
    """ read main data """
    lst_data = read_file(file_name)
    lst_out = []
    lst_out.append(lst_header)

    for line in lst_data:
        lst_inline = line.split(",")
        lst_temp = [0] * len(lst_header)

        for index in range(1, len(lst_inline)):
            if lst_inline[index] in lst_header:
                i = lst_header.index(lst_inline[index])
                lst_temp[i] = 1

        lst_out.append(lst_temp)

    return lst_out
