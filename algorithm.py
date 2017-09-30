""" main algorithm: k_means """

def k_means(data, headers, k):
    """ k_means algorithm """
    clusters = init_group(data, k)
    count = 0
    prev_val = -1
    len_data = len(data) - 1
    while True:
        remove_all_members(clusters)
        find_members(data, headers, clusters, k)

        diff = calc_mean(clusters)

        if int(diff) == prev_val:
            count += 1
        else:
            count = 0
            prev_val = int(diff)

        if count == 10:
            break

    out_data = gen_output_data(clusters, headers)
    a = calc_a(clusters)
    percent = ((len_data - a) / len_data) * 100
    percent = round(percent, 2)

    return (out_data, percent)


def remove_all_members(clusters):
    """ remove_all_members """
    for item in clusters:
        del item["members"][:]


def init_group(data, k):
    """ init list of means """
    clusters = []
    for i in range(1, k + 1):
        clusters.append({"mean": [], "members": []})
        index = len(clusters)
        while True:
            if is_difference(clusters, data[index]):
                clusters[i - 1]["mean"] = data[index][:]
                break
            index += 1

    return clusters


def is_difference(clusters, data):
    """ is_difference """
    for item in clusters:
        count = 0
        length = len(item["mean"])

        for i in range(length):
            if item["mean"][i] == data[i]:
                count += 1
        if length != 0 and count == length:
            return False
    return True


def find_members(data, headers, clusters, k):
    """ find members in each group """
    len_data = len(data)
    for i in range(1, len_data):
        calc_dist(clusters, data[i], k)

    return


def calc_dist(clusters, child_data, k):
    max_count = 0
    max_index = 0
    for j in range(k):
        mean = clusters[j]["mean"]
        count = 0

        for i in range(len(mean)):
            if mean[i] == child_data[i]:
                count += 1

        if max_count < count:
            max_count = count
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

        for i in range(len(new_mean)):
            if new_mean[i] < 0.5:
                new_mean[i] = 0
            else:
                new_mean[i] = 1

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
    sum_s = 0
    for i in range(len(clusters)):
        sum_s += len(clusters[i]["members"])
    print(sum_s)
    return


def calc_a(clusters):
    a = 0
    for i in range(len(clusters)):
        for mem in clusters[i]["members"]:
            for j in range(len(clusters)):
                if i == j:
                    continue
                found = False
                for k in range(len(mem)):
                    if mem[k] == 1 and mem[k] == clusters[j]["mean"][k]:
                        a += 1
                        found = True
                        break

                if found:
                    break

    print(a)
    return a


def gen_output_data(clusters, headers):
    """ output_data """
    out_data = []

    for items in clusters:
        dic = {"intances": len(items["members"]), "area": 0, "items": []}
        temp = []
        row = len(items["members"])
        col = len(headers)

        for i in range(row):
            for j in range(col):
                if items["members"][i][j] == 1 and headers[j] not in temp:
                    temp.append(headers[j])

        dic["area"] = len(temp)
        dic["items"] = temp[:]

        out_data.append(dic)
    return out_data
