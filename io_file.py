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


def read_csv(path):
    """ read_csv """
    lst_data = read_file(path)
    data = []
    data.append(lst_data[0].split(","))

    for i in range(1, len(lst_data)):
        data.append(list(map(int, lst_data[i].split(","))))

    return data


def write_csv(data, path):
    """ write_csv """
    f_open = open(path, "w")
    for item in data:
        f_open.write(",".join(list(map(str, item))))
        f_open.write("\n")
    return


def write_txt(data, percent, path):
    """ write_txt """
    f_open = open(path, "w")
    f_open.write("Cluster:\t" + str(len(data)) + "\n")
    f_open.write("Precision:\t" + str(percent) + "%\n")

    for i in range(len(data)):
        f_open.write("\tCluster " + str(i) + ":\n")
        f_open.write("\t\tIntances: " + str(data[i]["intances"]) + "\n")
        f_open.write("\t\tArea: " + str(data[i]["area"]) + "\n")
        f_open.write("\t\t" + ", ".join(data[i]["items"]) + "\n")
    return
