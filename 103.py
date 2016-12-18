from itertools import combinations

def is_special(sett):
    if 0 in sett: return False
    lst = sorted(sett)
    ratio = lst[-1] / lst[0]
    for i in range(len(lst) // 2):
        # print(lst[:i+2], lst[-(i+1):])
        if( sum(lst[:i+2]) <= sum(lst[-(i+1):]) ):
            return False
    for i in range(2, len(lst) // 2 + 1):
        seen = {}
        for tup in combinations(sett, i):
            if seen.get(sum(tup)): return False
            seen[sum(tup)] = True
        # print(list(combinations(sett, i)))
    return True

def next_suboptimum(sett):
    mid = sorted(sett)[len(sett) // 2]
    result = {mid + n for n in sett}
    result.add(mid)
    return result

s6 = {11, 17, 20, 22, 23, 24}

# add = lambda sett, n: {el+n for el in sett}
combine = lambda lst1, lst2: [lst1[idx] + lst2[idx] for idx in range(len(lst1))]

def search_n(distance, dimension):
    result = [[distance]]
    for _ in range(dimension-1):
        for coord in result[:]:
            coord.append(0)
            for i in range(abs(coord[0])):
                r = coord[:]
                r[-1] = r[0] -  i
                r[0] = i
                result.append(r)
    return result

def points_distance_from(point, distance, dimension):
    distances = search_n(distance, dimension)
    for i in range(dimension):
        for coord in range(len(distances)):
            if distances[coord][i] == 0: continue
            negative = distances[coord][:]
            negative[i] *= -1
            distances.append(negative)
    return list(map(lambda l: combine(l, point), distances))

manhattan = lambda l1, l2: sum([ abs(l1[i] - l2[i]) for i in range(len(l1)) ])

a = [22, 33, 39, 42, 44, 45, 46]
b = [22, 33, 40, 41, 42, 44, 47] #(6, 6)
c = [21, 33, 40, 41, 42, 44, 47] #(1, 7)
d = [20, 33, 40, 41, 42, 44, 47] #(1, 8)
e = [21, 32, 39, 41, 43, 40, 46] #(9, 9)
f = [20, 32, 39, 40, 41, 43, 46] #(7, 10)
g = [20, 31, 38, 39, 40, 42, 45] #(6, 16)

def run(dimension, point=None):
    # s6 = {11, 17, 20, 22, 23, 24}
    # s5 = {6, 9, 11, 12, 13}
    # l = [20, 31, 38, 39, 40, 42, 45]
    if not point:
        point = next_suboptimum({11, 17, 20, 22, 23, 24})
    # while is_special(add(point, -1)):
        # point = add(point, -1)
    point = sorted(point)
    d = sum(point)
    i = 1
    while True:
        print(i)
        a = points_distance_from(point, i, dimension)
        b = [n for n in a if sum(n) < d]

        for c in b:
            if is_special(c):
                d = sum(c)
                print(c, sum(c))
                run(dimension, c)
        i += 1
# [4]

#
# [4, 0]
# [3, 1]
# [2, 2]
# [1, 3]
# [0, 4]
#
# [4, 0, 0] [3, 0, 1] [2, 0, 2] [1, 0, 3] [0, 0, 4]
# [3, 1, 0] [2, 1, 1] [1, 1, 2] [0, 1, 3]
# [2, 2, 0] [1, 2, 1] [0, 2, 2]
# [1, 3, 0] [0, 3, 1]
# [0, 4, 0]
#
# [-4, 0, 0] [-3, 0, 1] [-2, 0, 2] [-1, 0, 3] [-0, 0, 4]
# [-3, 1, 0] [-2, 1, 1] [-1, 1, 2] [-0, 1, 3]
# [-2, 2, 0] [-1, 2, 1] [-0, 2, 2]
# [-1, 3, 0] [-0, 3, 1]
# [-0, 4, 0]
#
# [4, 0, 0] [3, 0, 1] [2, 0, 2] [1, 0, 3] [0, 0, 4]
# [3, 1, 0] [2, 1, 1] [1, 1, 2] [0, 1, 3]
# [2, 2, 0] [1, 2, 1] [0, 2, 2]
# [1, 3, 0] [0, 3, 1]
# [0, 4, 0]
#
# [-4, 0, 0] [-3, 0, 1] [-2, 0, 2] [-1, 0, 3] [-0, 0, 4]
# [-3, 1, 0] [-2, 1, 1] [-1, 1, 2] [-0, 1, 3]
# [-2, 2, 0] [-1, 2, 1] [-0, 2, 2]
# [-1, 3, 0] [-0, 3, 1]
# [-0, 4, 0]
#
#
# # [4, 0, 0, 0] [3, 0, 1, 0] [2, 0, 2, 0] [1, 0, 3, 0] [0, 0, 4, 0]
# # [3, 1, 0, 0] [2, 1, 1, 0] [1, 1, 2, 0] [0, 1, 3, 0]
# # [2, 2, 0, 0] [1, 2, 1, 0] [0, 2, 2, 0]
# # [1, 3, 0, 0] [0, 3, 1, 0]
# # [0, 4, 0, 0]
# #
# # [3, 0, 0, 1] [2, 0, 1, 1] [1, 0, 2, 1] [0, 0, 3, 1]
# # [2, 1, 0, 1] [1, 1, 1, 1] [0, 1, 2, 1]
# # [1, 2, 0, 1] [0, 2, 1, 1]
# # [0, 3, 0, 1]
# #
# # [2, 0, 0, 2] [1, 0, 1, 2] [0, 0, 2, 2]
# # [1, 1, 0, 2] [0, 1, 1, 2]
# # [0, 2, 0, 2]
# #
# # [1, 0, 0, 3] [0, 0, 1, 3]
# # [0, 1, 0, 3]
# #
# # [0, 0, 0, 4]
