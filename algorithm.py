""" main algorithm: k_means """

def k_means(data, headers, k):
    """ k_means algorithm """
    clusters = init_group(data, headers, k)
    i = 0
    while True:
        find_members(data, headers, clusters, k)
        print_clusters(clusters)
        print("-------------------------------------")
        diff = calc_mean(clusters)
        # i += 1
        if diff == 0:
            break

    return

def init_group(data, headers, k):
    """ init list of means """
    clusters = []
    for i in range(1, k + 1):
        clusters.append({"mean": [], "members": []})
        for j in range(len(data[i])):
            if data[i][j] == 1:
                clusters[i - 1]["mean"].append(headers[j])

    return clusters


def find_members(data, headers, clusters, k):
    """ find members in each group """
    for i in range(1, len(data)):
        child_data = data[i]
        max_c = 0
        max_index = 0
        for j in range(k):
            mean = clusters[j]["mean"]
            count = 0
            index = 0
            for area in mean:
                index = headers.index(area)
                if child_data[index] == 1:
                    count += 1

            if max_c < count:
                max_c = count
                max_index = j

        clusters[max_index]["members"].append(get_name_from_list(child_data, headers))
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
        new_mean = []
        for plant in mem:
            for area in plant:
                if area not in new_mean:
                    new_mean.append(area)
        diff += calc_difference(old_mean, new_mean)
        del item["mean"][:]
        item["mean"] = new_mean[:]
    return diff


def calc_difference(lst1, lst2):
    """ calc_difference """
    count = 0
    for val in lst1:
        if val in lst2:
            count += 1

    return len(lst1) - count + len(lst2) - count


def print_clusters(clusters):
    """ print_clusters """
    for i in range(len(clusters)):
        print(clusters[i]["mean"])

    return
