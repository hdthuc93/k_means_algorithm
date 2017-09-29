""" main file """
import io_file
from algorithm import k_means

def main():
    """ Main function """
    k = 70

    headers = io_file.read_stateabbr("./data/stateabbr.txt")
    data = io_file.read_data("./data/plants.data", headers)
    k_means(data, headers, k)
    return


if __name__ == "__main__":
    main()
