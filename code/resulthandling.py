from Machine import Machine
import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib import cm


def fill(a, fillvalue):
    b = np.full([len(a), len(max(a, key=lambda x: len(x)))], fillvalue, dtype='float64')
    for i, j in enumerate(a):
        b[i][0:len(j)] = j
    return b


def normaltests():
    data = []
    for i in range(10):
        a = np.load(r + 'StrongSpecialists/50.50-0' + str(i) + '-2021.12.28.npy', allow_pickle=True)
        a = np.rot90(a)
        data.append(a)

    total_sat = []
    total_acc = []
    total_siz = []
    for d in data:
        temp_sat = []
        temp_acc = []
        temp_siz = []
        for i in d:
            temp_sat.append(np.sum(i[:, 5]))
            temp_acc.append(i[:, 4])
            # temp_siz.append(sum(i[:, 3]/(2*i[0][0]))/100)
            temp_siz.append(i[:, 3])

        # acc.append(np.max(d[-1][:, 5]))
        # a = d[-1][:, 4]
        # b = len(max(a, key=lambda x: len(x.states)).states)
        # print(b)

        total_sat.append(temp_sat)
        total_acc.append(temp_acc)
        total_siz.append(temp_siz)

    total_sat = fill(total_sat, 100)
    # total_acc = fill(total_acc, 1)

    # avg = np.average(total_siz, axis=0)

    fig = plt.figure(1)
    ax = plt.axes()
    plt.title('Size of machines made throughout a simulation (100/0)')
    plt.ylabel('machine size')
    plt.xlabel('iterations')
    for el in total_acc:
        fig = plt.figure(2)
        ax = plt.axes()
        # ax.plot(el)
        plt.title('Accuracy of all machines each iteration (50/50)')
        plt.ylabel('accuracy')
        plt.xlabel('iterations')
        color = iter(cm.rainbow(np.linspace(0, 1, 11)))
        c = next(color)
        for i, elm in enumerate(el):
            c = next(color) if i % 10 == 0 else c
            ax.plot(elm, alpha=0.2, color=c)
            # ax.scatter(np.arange(len(elm)), elm)
        # plt.axhline(y=0.0022, color='r', linestyle='-')
        plt.show()

    # ax.plot(avg, color='black', alpha=0.75, label='average of 10 runs')
    # plt.legend()
    plt.show()


def accuracytests():
    data = []
    all_acc = []
    max_acc = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    acc1 = acc2 = acc3 = acc4 = 0

    for i in range(5):
        d1 = np.load('./results/string-length/10-0' + str(i) + '-2022.01.02.npy', allow_pickle=True)[-1, :, 4]
        d2 = np.load('./results/string-length/50-0' + str(i) + '-2022.01.02.npy', allow_pickle=True)[-1, :, 4]
        d3 = np.load('./results/string-length/99-0' + str(i) + '-2022.01.02.npy', allow_pickle=True)[-1, :, 4]
        d4 = np.load('./results/string-length/30-0' + str(i) + '-2022.01.03.npy', allow_pickle=True)[-1, :, 4]
        acc1 += sum(d1) / 100
        acc2 += sum(d2) / 100
        acc3 += sum(d3) / 100
        acc4 += sum(d4) / 100

        all_acc.extend(np.load('./results/string-length/10-0' + str(i) + '-2022.01.02.npy', allow_pickle=True)[:, :, 4])

        max_acc[0][i] = np.max(d1)
        max_acc[1][i] = np.max(d4)
        max_acc[2][i] = np.max(d2)
        max_acc[3][i] = np.max(d3)

    groups = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in all_acc:
        for y in x:
            if y > 0:
                groups[int(str(y)[2])] += 1
            else:
                groups[0] += 1

    values = [10, 30, 50, 99]
    base = []
    for value in values:
        r = sum([1 / (value + 1) * 0.5 ** x for x in range(0, value + 1)])
        base.append(r)

    print(base)

    acc = [acc1 / 5, acc4 / 5, acc2 / 5, acc3 / 5]
    max_acc = [sum(x) / 5 for x in max_acc]

    print(acc)
    print(max_acc)

    fig = plt.figure()
    ax = plt.axes()
    ax.plot(values, max_acc, label='max accuracy')
    ax.plot(values, base, label='chance')
    ax.plot(values, acc, label='average accuracy')
    ax.legend()
    plt.xlabel('string length')
    plt.ylabel('accuracy')
    plt.title('Different accuracy levels for different string lengths')
    plt.show()

    ax = plt.axes()
    x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    ax.bar(x, groups, width=0.1, align='edge', tick_label=x)
    ax.plot(x, groups, color='orange')
    plt.xlabel('accuracy')
    plt.ylabel('occurrences')
    plt.title('Number of times each accuracy occurred for a max. string length of 10')
    plt.show()


def numbers():
    data = []
    for i in range(10):
        a = np.load('./results/StrongSpecialists/100.0-0' + str(i) + '-2021.12.28.npy', allow_pickle=True)
        # a = np.rot90(a)
        data.append(a)

    num_m = []
    acc_avg = []
    acc_max = []
    acc_min = []
    all_acc = []
    all_max = []
    all_min = []
    prop_siz = []
    not_siz = []
    mac_siz = []
    for d in data:
        # machines = d[-1, :, 2]                    # all machines
        machines = [x[2] for x in d[-1] if x[5]]    # Take the machine if the agent is satisfied
        num_m.append(len(list(set(machines))))
        # prop_siz.append([len(x.states) for x in machines])

        accuracies = [x[4] for x in d[-1] if x[5]]
        b = d[-1, :, 4]
        all_acc.append(np.average(b))
        all_max.append(max(b))
        all_min.append(min(b))

        proper = [len(x[2].states) for x in d[-1] if x[5] and x[2] is not None]         # take machine size if agent is satisfied and the machine is not None
        not_proper = [len(x[2].states) for x in d[-1] if not x[5] and x[2] is not None]
        mac_siz.append(d[-1, 0, 0])

        if proper:
            prop_siz.append(np.average(proper))
        if not_proper:
            not_siz.append(np.average(not_proper))

        if accuracies:
            acc_avg.append(np.average(list(set(accuracies))))
            # acc_avg.append(np.sum(list(set(accuracies)))/10)
            acc_max.append(max(accuracies))
            acc_min.append(min(accuracies))

    # print(num_m)
    # num_m = np.average(num_m)
    # print(num_m)
    #
    # print(acc_avg)
    # # acc_avg = np.average(acc_avg)
    # acc_avg = np.sum(acc_avg)/10
    # print([np.average(acc_min), acc_avg, np.average(acc_max)])
    # all_acc = np.average(all_acc)
    # print([np.average(all_min), all_acc, np.average(all_max)])

    print([np.average(mac_siz), np.average(prop_siz), np.average(not_siz)])


r = 'D:/Documents/Uni/2021-2022/Scriptie/RU2021-thesis/data/'
normaltests()

# acc1 = [[0.225, 0.41791000000000017, 0.593],
#         [0.28500000000000003, 0.4676900000000003, 0.591],
#         [0.38699999999999996, 0.49626000000000037, 0.587],
#         [0.374, 0.5149499999999998, 0.556],
#         [0.542, 0.5547000000000002, 0.567],
#         [0.476, 0.51017, 0.558],
#         [0.35500000000000004, 0.46977000000000035, 0.571],
#         [0.49099999999999994, 0.5231099999999997, 0.552],
#         [0.38, 0.4582600000000001, 0.543],
#         [0.43, 0.47331, 0.5720000000000001],
#         [0.43900000000000006, 0.5094299999999997, 0.574]]
#
# acc2 = [[0.51, 0.5563668430335098, 0.6188888888888889],
#         [0.523, 0.5572666666666668, 0.591],
#         [0.5266666666666667, 0.5561111111111111, 0.5988888888888888],
#         [0.514, 0.5321333333333333, 0.556],
#         [0.542, 0.5535, 0.567],
#         [0.5288888888888889, 0.5487037037037037, 0.578888888888889],
#         [0.5657142857142857, 0.6021428571428571, 0.6414285714285715],
#         [0.5444444444444444, 0.5583333333333333, 0.5722222222222223],
#         [0.52875, 0.5573541666666667, 0.5862499999999999],
#         [0.52625, 0.5689166666666667, 0.6287499999999999],
#         [0.5433333333333334, 0.5680555555555556, 0.5933333333333333]]
#
# acc1 = np.rot90(acc1)
# acc2 = np.rot90(acc2)
#
# mac = [6.4, 4.5, 2.7, 2.4, 2.5, 2.3, 1.5, 1.3, 2, 2.8, 1.4]
# age = [64, 77, 85, 94, 100, 90, 68, 90, 74, 80, 88]
#
# mac_siz = [[8.1, 3.5191358024691355, 5.109508301404853],
#            [8.8, 3.569642857142857, 5.647076023391813],
#            [9.9, 3.4380952380952383, 6.674444444444444],
#            [8.8, 4.5344444444444445, 6.6819819819819815],
#            [9.7, 4.58, None],
#            [8.2, 5.577777777777778, 9.10204081632653],
#            [7.3, 4.953571428571429, 8.474926303854875],
#            [10.5, 5.644444444444444, 8.26],
#            [7.0, 4.4125000000000005, 7.147777777777779],
#            [8.5, 4.9125, 6.535],
#            [7.9, 5.666666666666667, 4.865]]
#
# mac_siz = [[y-x[0] if y is not None else 0 for y in x] for x in mac_siz]
# print(mac_siz)
#
# x = ['0/100', '10/90', '20/80', '30/70', '40/60', '50/50', '60/40', '70/30', '80/20', '90/10', '100/0']
#
# fig = plt.figure()
# ax = plt.axes()
# # ax.fill_between(x, acc1[2], acc1[0], alpha=0.3)
# # ax.plot(x, acc1[1])
# #
# # ax.fill_between(x, acc2[2], acc2[0], alpha=0.3)
# # ax.plot(x, acc2[1])
# # ax.plot(x, mac)
# ax.plot(x, mac_siz)
# plt.title('relative average machine size at the end of a simulation')
# plt.xlabel('population distribution (G/S)')
# plt.ylabel('relative size')
# plt.legend(['world', 'proper machines', 'improper machines'])
#
# #ax.plot(age, color='pink')
#
# plt.show()
