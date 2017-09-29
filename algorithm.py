""" main algorithm: k_means """
from threading import Thread

def k_means(data, headers, k):
    """ k_means algorithm """
    clusters = init_group(data, headers, k)
    # i = 0
    while True:
        find_members(data, headers, clusters, k)
        print_clusters(clusters)
        print("---------------------------------------------------------------------")
        diff = calc_mean(clusters)
        # i += 1
        print(diff)
        if diff == 0:
            break

    return

def init_group(data, headers, k):
    """ init list of means """
    clusters = []
    for i in range(1, k + 1):
        clusters.append({"mean": [], "members": []})
        clusters[i - 1]["mean"] = data[i][:]

    return clusters


def find_members(data, headers, clusters, k):
    """ find members in each group """
    lst_thread = []
    for i in range(10):
        lst_thread.append(Thread())

    i_thread = 0
    len_data = len(data)
    for i in range(1, len_data):
        calc_dist(clusters, data[i], k)
        # if lst_thread[i_thread].isAlive():
        #     lst_thread[i_thread].join()
        # lst_thread[i_thread] = Thread(target=calc_dist, args=(clusters, data[i], k))
        # lst_thread[i_thread].start()
        # # print("thread " + str(i_thread) + " start")
        # i_thread += 1

        if i_thread == 10:
            i_thread = 0

    while True:
        alive = 0
        for i in range(10):
            if lst_thread[i].isAlive():
                alive += 1
        if alive == 0:
            break

    return


def calc_dist(clusters, child_data, k):
    max_dist = 0
    max_index = 0
    for j in range(k):
        mean = clusters[j]["mean"]
        dist = 0

        for m in range(len(mean)):
            dist += (mean[m] - child_data[m]) ** 2

        if max_dist < dist:
            max_dist = dist
            max_index = j
    clusters[max_index]["members"].append(child_data[:])
    return


def get_name_from_list(child_data, headers):
    """ get real name """
    lst = []

    for i in range(len(headers)):
        if child_data[i] == 1:
            lst.append(headers[i])

    return lst


def calc_mean(clusters):
    """ calc_mean """
    diff = 0
    for item in clusters:
        old_mean = item["mean"]
        mem = item["members"]
        new_mean = [0] * len(old_mean)

        row = len(mem)
        col = len(old_mean)

        for i in range(row):
            for j in range(col):
                new_mean[j] += mem[i][j]

        if row == 0:
            new_mean = old_mean[:]
        else:
            for i in range(col):
                new_mean[i] = new_mean[i] / row
            diff += calc_difference(old_mean, new_mean)
        del item["mean"][:]
        item["mean"] = new_mean[:]
    return diff


def calc_difference(lst1, lst2):
    """ calc_difference """
    dist = 0
    for i in range(len(lst1)):
        dist += (lst1[i] - lst2[i]) ** 2
    return dist


def print_clusters(clusters):
    """ print_clusters """
    for i in range(len(clusters)):
        print(clusters[i]["mean"])

    return
