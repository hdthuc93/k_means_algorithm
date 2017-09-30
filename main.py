""" main file """
import sys
import io_file
from algorithm import k_means

def main():
    """ Main function """
    lst_argv = sys.argv

    k = int(lst_argv[lst_argv.index("-k") + 1])
    stateabbr = "./data/stateabbr.txt"
    # plants_data = "./data/plants.data"
    plants_csv = lst_argv[lst_argv.index("-input") + 1]
    out_data_path = "./data/26_" + str(k) + "_clustering.txt"

    headers = io_file.read_stateabbr(stateabbr)
    # data = io_file.read_data(plants_data, headers)
    # io_file.write_csv(data, plants_csv)

    data = io_file.read_csv(plants_csv)
    out_data = k_means(data, headers, k)
    io_file.write_txt(out_data, out_data_path)

    return


if __name__ == "__main__":
    main()
