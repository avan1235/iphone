import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as ticker
from act_time import get_minute, get_second


def create_plot(name_files, out_plot_name):
    markers = [".", "o", "^", "s", "8", "*", "x"]

    plt.clf()
    style.use("seaborn-talk")
    plt.title("Ceny iPhone 8")
    plt.xlabel("czas", fontsize='medium')
    plt.ylabel("cena [zł]", fontsize='medium')

    max_lines_size = 0

    for file in name_files:
        data = open('data/' + file + '.txt', 'r')
        graph_data = data.read()
        lines = graph_data.split("\n")

        if len(lines) > max_lines_size:
            max_lines_size = len(lines)

        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(float(y))
        plt.plot(xs, ys, label=file, marker=markers[name_files.index(file)], markersize=4, linewidth=1)
        plt.xticks(rotation='vertical', fontsize='small')
        plt.yticks(fontsize='small')
        plt.legend(loc=2, fontsize='x-small')
        data.close()

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(max_lines_size/10))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

    plt.savefig('server/'+out_plot_name, bbox_inches='tight', dpi=1000)


def create_plot_thread(name_files, out_plot_name, write_minutes, operation_minutes):
    DONE = False
    CAN_BE_DONE = True

    state = CAN_BE_DONE

    while True:

        if get_minute() == write_minutes and state == CAN_BE_DONE:
            create_plot(name_files, out_plot_name)
            state = DONE
        elif get_minute() == (write_minutes + operation_minutes) % 60 and state == DONE:
            state = CAN_BE_DONE
        else:
            print("Waiting for plot")