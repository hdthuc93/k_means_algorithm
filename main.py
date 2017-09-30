""" main file """
import sys
import io_file
from algorithm import k_means

def main():
    """ Main function """
    lst_argv = sys.argv

    if "-k" not in lst_argv or "-input" not in lst_argv:
        return

    k = int(lst_argv[lst_argv.index("-k") + 1])
    print("Doc file csv...")
    stateabbr = "./data/stateabbr.txt"
    # plants_data = "./data/plants.data"
    plants_csv = lst_argv[lst_argv.index("-input") + 1]
    out_data_path = "./data/26_" + str(k) + "_clustering.txt"

    headers = io_file.read_stateabbr(stateabbr)
    # data = io_file.read_data(plants_data, headers)
    # io_file.write_csv(data, plants_csv)

    data = io_file.read_csv(plants_csv)
    print("Dang chay giai thuat k mean...")
    out_data, percent = k_means(data, headers, k)
    print("Ghi ket qua ra file...")
    io_file.write_txt(out_data, percent, out_data_path)
    print("Ket thuc!")
    return


if __name__ == "__main__":
    main()
